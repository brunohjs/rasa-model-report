import glob
import logging
import re

import requests.exceptions
from requests.adapters import HTTPAdapter
from requests.adapters import Retry
from yaml import safe_load

from src.rasa_model_report.controllers.controller import Controller
from src.rasa_model_report.helpers.type_aliases import nlu_payload


class NluController(Controller):
    """
    Controller responsible for Rasa NLU.
    """
    def __init__(
        self,
        rasa_path: str,
        output_path: str,
        project: str,
        version: str,
        url: str = "http://localhost:5005",
        **kwargs: dict
    ) -> None:
        super().__init__(rasa_path, output_path, project, version)

        self._data: list[nlu_payload] = []
        self._problem_sentences: list[nlu_payload] = []
        self._general_grade: float | None = None
        self._connected: bool = False
        self._disable_nlu: bool = kwargs.get("disable_nlu")
        self.url: str = url

        if not self._disable_nlu and self.health_check_rasa_api():
            self._load_nlu()
            self._generate_data()
            self._load_problem_sentences()
            self._calculate_general_grade()

    def is_connected(self) -> bool:
        """
        If is connected to the Rasa API.

        :return bool: True if is connected.
        """
        return self._connected

    def health_check_rasa_api(self) -> bool:
        """
        Check if Rasa API is available.

        :return: True if is available or False.
        """
        self._connected = False
        response = self.request_rasa_api(self.url)
        if isinstance(response, requests.Response):
            self._connected = response.status_code == 200
            if self._connected:
                logging.info("Rasa API is enabled.")
            else:
                logging.warning("Rasa API has some problem. NLU section will not be generated.")
        return self._connected

    def _load_nlu(self) -> dict[str, str | list[str]]:
        """
        Load all NLU sentences from project of Rasa files.

        :return: A dictionary that contains the sentences separeted by intent.
        """
        logging.info("Looking for Rasa's NLU files.")
        files = glob.glob(f"{self.nlu_path}/**/*.yml") + glob.glob(f"{self.nlu_path}/*.yml")
        nlu = {}
        for filename in files:
            file = safe_load(open(filename, encoding="utf-8"))
            if file.get("nlu"):
                data = {i["intent"]: i["examples"] for i in file["nlu"] if i.get("intent")}
                if data:
                    logging.info(f"Found sentences in {filename} file.")
                    for intent, text in data.items():
                        data[intent] = self._extract_sentences(text)
                        logging.info(f" - Intent {intent}: {len(data[intent])} sentence(s).")
                    nlu.update(data)
        self._data = nlu
        return nlu

    def _generate_data(self) -> list[nlu_payload]:
        logging.info("Formatting extracted data.")
        data = []
        for intent, examples in self._data.items():
            for text in examples:
                text = self.remove_entities_from_text(text)
                nlu_requested = self.request_nlu(text)
                predicted_intent = self.select_intent(nlu_requested)
                item = {
                    "intent": intent,
                    "text": text,
                    "confidence": predicted_intent.get("confidence"),
                    "predicted_intent": predicted_intent.get("name"),
                    "intent_ranking": nlu_requested.get("intent_ranking", [])[:4]
                }
                item["understood"] = predicted_intent.get("nlu_fallback", False) or intent != predicted_intent["name"]
                data.append(item)
        logging.info("Ordering phrases.")
        data = sorted(data, key=lambda item: item["confidence"], reverse=True)
        logging.info(f"Total of {len(data)} extracted sentences.")
        self._data = data
        return data

    def _load_problem_sentences(self) -> list[nlu_payload]:
        self._problem_sentences = [
            sentence for sentence in self._data if sentence.get("understood", False)
        ]
        return self._problem_sentences

    @property
    def data(self) -> list[nlu_payload]:
        """
        Return a copy of the generated data.

        :return: Generated data.
        """
        return self._data.copy()

    @property
    def problem_sentences(self) -> list[nlu_payload]:
        """
        Return a copy of the generated problem sentences.

        :return: Generated data.
        """
        return self._problem_sentences.copy()

    @property
    def general_grade(self) -> float | None:
        return self._general_grade

    def _calculate_general_grade(self) -> float | None:
        total_sentences = len(self._data)
        if total_sentences:
            total_problem_sentences = len(self._problem_sentences)
            self._general_grade = 1 - total_problem_sentences / total_sentences
            return self._general_grade

    def request_nlu(self, text: str) -> nlu_payload:
        response = requests.request(
            method="POST",
            url=f"{self.url}/model/parse",
            json={"text": text}
        )
        if response and response.status_code == 200:
            data = response.json()
            return data
        return {}

    @staticmethod
    def _extract_sentences(text: str) -> str:
        text = text.split("\n")
        text = [item[2:] for item in text if item != ""]
        return text

    @staticmethod
    def remove_entities_from_text(text: str) -> str:
        letter = "[A-Za-z0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ_\\-'\"\\s]"
        regex = f"(\\[{letter}+\\](\\({letter}+\\)|{{\"entity\":{letter}+,(\\s+)?\"value\":{letter}+}}))"
        matched = re.findall(regex, text)
        if matched:
            for match in matched:
                word = re.findall(f"\\[{letter}+\\]", match[0])[0]
                word = word.replace("[", "").replace("]", "")
                text = text.replace(match[0], word)
        return text

    @staticmethod
    def select_intent(payload: nlu_payload, retrieval_intent: bool = False) -> dict[str, str]:
        if payload.get("intent", {}).get("name") == "nlu_fallback":
            payload["intent_ranking"][1]["nlu_fallback"] = True
            return payload.get("intent_ranking")[1]
        else:
            return payload.get("intent", {})

    @staticmethod
    def request_rasa_api(url: str, method: str = "GET", json: dict = {}) -> requests.Response | None:
        message = "NLU section will not be generated."
        response = None
        try:
            session = requests.Session()
            retries = Retry(total=2, backoff_factor=3)
            session.mount("http://", HTTPAdapter(max_retries=retries))
            response = session.request(method=method, url=url, json=json)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            logging.warning(f"Rasa API is disabled. {message}")
        except requests.exceptions.RequestException:
            logging.warning(f"Rasa API has some problem. {message}")
        return response
