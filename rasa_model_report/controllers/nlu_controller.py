import glob
import logging
import re
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import requests.exceptions

from rasa_model_report.controllers.controller import Controller
from rasa_model_report.helpers import utils
from rasa_model_report.helpers.type_aliases import nlu_payload


class NluController(Controller):
    """
    Controller responsible for Rasa NLU.
    """
    def __init__(
        self,
        rasa_path: str,
        output_path: str,
        project_name: str,
        project_version: str,
        url: str = "http://localhost:5005",
        **kwargs: dict
    ) -> None:
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project_name: Project name.
        :param project_version: Project version.
        :param url: Rasa API URL (default: "http://localhost:5005")
        """
        super().__init__(rasa_path, output_path, project_name, project_version)
        self._data: List[nlu_payload] = []
        self._problem_sentences: List[nlu_payload] = []
        self._general_grade: Optional[float] = None
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
        response = utils.request(self.url)
        if isinstance(response, requests.Response):
            self._connected = response.status_code == 200
            if self._connected:
                logging.info("Rasa API is enabled.")
            else:
                logging.warning("Rasa API has some problem. NLU section will not be generated.")
        return self._connected

    def _load_nlu(self) -> Dict[str, Union[str, List[str]]]:
        """
        Load all NLU sentences from project of Rasa files.

        :return: A dictionary that contains the sentences separeted by intent.
        """
        logging.info("Looking for Rasa's NLU files.")
        files = glob.glob(f"{self.nlu_path}/**/*.yml") + glob.glob(f"{self.nlu_path}/*.yml")
        nlu = {}
        for filename in files:
            file = utils.load_yaml_file(filename)
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

    def _generate_data(self) -> List[nlu_payload]:
        """
        Load and process the NLU sentences data.

        :return: Processed NLU sentences data.
        """
        logging.info("Formatting extracted data.")
        data = []
        index = 1
        for intent, examples in self._data.items():
            progress = index / len(self._data) * 100
            index += 1
            logging.info(f" - Analyzing NLU of the {intent} intent ({progress:<5.1f}%).")
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

    def _load_problem_sentences(self) -> List[nlu_payload]:
        """
        Load problem sentences list.

        :return: Problem sentences list.
        """
        self._problem_sentences = [
            sentence for sentence in self._data if sentence.get("understood", False)
        ]
        return self._problem_sentences

    @property
    def data(self) -> List[nlu_payload]:
        """
        Return a copy of the generated data.

        :return: Copy of generated data object.
        """
        return self._data.copy()

    @property
    def problem_sentences(self) -> List[nlu_payload]:
        """
        Return a copy of the generated problem sentences.

        :return: Copy of problem sentences object.
        """
        return self._problem_sentences.copy()

    @property
    def general_grade(self) -> Optional[float]:
        """
        Return a copy of the general grade value.

        :return: Copy of general grade value.
        """
        return self._general_grade

    def _calculate_general_grade(self) -> Optional[float]:
        """
        Calculate the general grade value.

        :return: General grade value.
        """
        total_sentences = len(self._data)
        if total_sentences:
            total_problem_sentences = len(self._problem_sentences)
            self._general_grade = 1 - total_problem_sentences / total_sentences
            return self._general_grade

    def request_nlu(self, text: str) -> nlu_payload:
        """
        Function that requests the NLU payload to the Rasa API.

        :param text: Sentence.
        :return: NLU payload.
        """
        response = utils.request(
            method="POST",
            url=f"{self.url}/model/parse",
            json={"text": text}
        )
        if response and response.status_code == 200:
            data = response.json()
            return data
        return {}

    @staticmethod
    def _extract_sentences(text: str) -> List[str]:
        """
        Split and arrange sentences in a list.

        :param text: Sentences string file.
        :return: List of sentences.
        """
        text = text.split("\n")
        return [item[2:] for item in text if item != ""]

    @staticmethod
    def remove_entities_from_text(text: str) -> str:
        """
        Remove Rasa entity syntax from text.

        :param text: Text with Rasa entity syntax.
        :return: Text without Rasa entity syntax.
        """
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
    def select_intent(payload: nlu_payload) -> Dict[str, nlu_payload]:
        """
        From the NLU payload returned from RASA API, the correct intent is selected.

        :param payload: NLU payload returned from RASA API.
        :return: Formatted intent object.
        """
        intent = payload.get("intent", {})
        intent_name = intent.get("name")
        response_selector = payload.get("response_selector", {})
        if intent_name == "nlu_fallback":
            intent = payload["intent_ranking"][1].copy()
            intent["nlu_fallback"] = True
        elif intent_name in response_selector.get("all_retrieval_intents", []):
            response = response_selector.get(intent_name, {})
            for r in response.get("ranking", []):
                r["name"] = r.pop("intent_response_key")
            intent = response.get("response")
            return {
                "id": intent.get("id"),
                "name": intent.get("intent_response_key"),
                "confidence": intent.get("confidence"),
                "intent_ranking": response.get("ranking", [])
            }
        intent["intent_ranking"] = payload.get("intent_ranking", [])
        return intent
