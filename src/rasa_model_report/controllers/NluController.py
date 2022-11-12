import glob
import logging
import re
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import requests
from rasa_model_report.controllers.Controller import Controller
from requests.adapters import HTTPAdapter
from requests.adapters import Retry
from requests.exceptions import ConnectionError
from requests.exceptions import RequestException
from requests.exceptions import Timeout
from yaml import safe_load


class NluController(Controller):
    def __init__(self, rasa_path, output_dir, project, version, url="http://localhost:5005", **kwargs) -> None:
        super().__init__(rasa_path, output_dir, project, version)
        self._data = []
        self._problem_sentences = []
        self._general_grade = None
        self._connected = False
        self._disable_nlu = kwargs.get("disable_nlu")
        self.url = url
        if not self._disable_nlu and self.health_check_rasa_api():
            self._load_nlu()
            self._generate_data()
            self._get_problem_sentences()
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
        response = self.request(self.url)
        if response:
            self._connected = response.status_code == 200
            if response.status_code == 200:
                logging.info("A API do Rasa está habilitada.")
            else:
                logging.warn("A API do Rasa está com algum problema. A seção de NLU não será gerada.")
        return self._connected

    def _load_nlu(self) -> Dict[str, Any]:
        """
        Load all NLU sentences from project of Rasa files.

        :return: A dictionary that contains the sentences separeted by intent.
        """
        logging.info("Procurando arquivos de NLU do Rasa.")
        files = glob.glob(self.NLU_PATH)
        nlu = {}
        for filename in files:
            file = safe_load(open(filename))
            if file.get("nlu"):
                data = {i["intent"]: i["examples"] for i in file["nlu"] if i.get("intent")}
                if data:
                    logging.info(f"Encontrado sentenças no arquivo {filename}.")
                    for intent, text in data.items():
                        data[intent] = self._extract_sentences(text)
                        logging.info(f" - Intenção {intent}: {len(data[intent])} frase(s).")
                    nlu.update(data)
        self._data = nlu
        return nlu

    def _generate_data(self) -> List[Dict[str, Any]]:
        logging.info("Formatando dados extraídos.")
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
        logging.info("Ordenando frases.")
        data = sorted(data, key=lambda item: item["confidence"], reverse=True)
        logging.info(f"Total de {len(data)} frases extraídas.")
        self._data = data
        return data

    def _get_problem_sentences(self) -> List[Dict[str, Any]]:
        self._problem_sentences = [
            sentence for sentence in self._data if sentence.get("understood", False)
        ]
        return self._problem_sentences

    def get_data(self) -> Dict[str, Any]:
        """
        Return a copy of the generated data.

        :return: Generated data.
        """
        return self._data.copy()

    def get_problem_sentences(self) -> Dict[str, Any]:
        """
        Return a copy of the generated problem sentences.

        :return: Generated data.
        """
        return self._problem_sentences.copy()

    def get_general_grade(self) -> int:
        return self._general_grade

    def _calculate_general_grade(self):
        total_sentences = len(self._data)
        if total_sentences:
            total_problem_sentences = len(self._problem_sentences)
            self._general_grade = 1 - total_problem_sentences / total_sentences
            return self._general_grade

    def request_nlu(self, text: str) -> Dict[str, Any]:
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
    def select_intent(payload: Dict[str, Any]) -> Dict[str, str]:
        if payload.get("intent", {}).get("name") == "nlu_fallback":
            payload["intent_ranking"][1]["nlu_fallback"] = True
            return payload.get("intent_ranking")[1]
        else:
            return payload.get("intent", {})

    @staticmethod
    def request(url: str, method: str = "GET", json: Dict[str, Any] = {}) -> Optional[requests.Response]:
        message = "A seção de NLU não será gerada."
        response = None
        try:
            session = requests.Session()
            retries = Retry(total=2, backoff_factor=3)
            session.mount("http://", HTTPAdapter(max_retries=retries))
            response = session.request(method=method, url=url, json=json)
        except (ConnectionError, Timeout):
            logging.warn(f"A API do Rasa está desabilitada. {message}")
        except RequestException:
            logging.warn(f"A API do Rasa está com algum problema. {message}")
        finally:
            return response
