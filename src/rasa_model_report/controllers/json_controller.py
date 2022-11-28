import json
import logging
import os.path
from typing import Any
from typing import Dict
from typing import List
from typing import Union

from src.rasa_model_report.controllers.controller import Controller
from src.rasa_model_report.helpers.utils import format_date


class JsonController(Controller):
    """
    Controller responsible for JSON files.
    """
    def __init__(self, rasa_path: str, output_path: str, project: str, version: str) -> None:
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project: Project name.
        :param version: Project version.
        """
        super().__init__(rasa_path, output_path, project, version)

        self.intents: List[Dict[str, Any]] = []
        self.intent_overview: Dict[str, float] = {}
        self.intent_errors: List[Dict[str, Any]] = []
        self.entities: List[Dict[str, Any]] = []
        self.entity_overview: Dict[str, float] = {}
        self.entity_errors: List[Dict[str, Any]] = []
        self.responses: List[Dict[str, Any]] = []
        self.response_overview: Dict[str, float] = {}
        self.overview: Dict[str, Union[str, float, int]] = {
            "project": self.project,
            "version": self.version
        }
        self.intent_report_path: str = f"{self.results_path}/intent_report.json"
        self.intent_errors_path: str = f"{self.results_path}/intent_errors.json"
        self.entity_report_path: str = f"{self.results_path}/DIETClassifier_report.json"
        self.entity_errors_path: str = f"{self.results_path}/DIETClassifier_errors.json"
        self.story_report_path: str = f"{self.results_path}/story_report.json"
        self.overview_report_path: str = f"{self.results_path}/overview.json"

        self._load_data()

    def load_json_file(self, filename: str, error_flag: bool = True) -> Union[Dict[Any, Any], List[Any]]:
        """
        Loads data from a JSON file.

        :param filename: Filename.
        :param error_flag: If True, an exception will be raised when the file isn't found (default: True).
        :return: Data in list or dict format.
        """
        if os.path.isfile(filename):
            file = open(filename, encoding="utf-8")
            data = json.load(file)
            file.close()
            logging.info(f"Arquivo {filename} carregado com sucesso")
            return data
        else:
            message = f"Arquivo {filename} não encontrado"
            if error_flag:
                logging.error(message)
                raise Exception(message)
            else:
                logging.warning(message)
                return {}

    def _load_data(self) -> None:
        """
        Load Rasa report data.
        """
        self._load_intents()
        self._load_intent_errors()
        self._load_entities()
        self._load_entity_errors()
        self._load_responses()
        self._load_overview()

    def _load_intents(self) -> None:
        """
        Load Rasa intent report data.
        """
        self.intents = self.load_json_file(self.intent_report_path, error_flag=False)
        if self.intents:
            self.intent_overview = {
                "accuracy": self.intents.get("accuracy"),
                "macro avg": self.intents.get("macro avg"),
                "weighted avg": self.intents.get("weighted avg")
            }
            del self.intents["accuracy"]
            del self.intents["macro avg"]
            del self.intents["weighted avg"]
        self.intents = self._to_list(self.intents, "f1-score")

    def _load_intent_errors(self) -> None:
        """
        Load Rasa intent errors report data.
        """
        self.intent_errors = self.load_json_file(self.intent_errors_path, error_flag=False)
        self.intent_errors = sorted(
            self.intent_errors,
            key=lambda d: d["intent_prediction"]["confidence"],
            reverse=True
        )

    def _load_entities(self) -> None:
        """
        Load Rasa entity report data.
        """
        self.entities = self.load_json_file(self.entity_report_path, error_flag=False)
        if self.entities:
            self.entity_overview = {
                "macro avg": self.entities.get("macro avg"),
                "micro avg": self.entities.get("micro avg"),
                "weighted avg": self.entities.get("weighted avg")
            }
            del self.entities["macro avg"]
            del self.entities["micro avg"]
            del self.entities["weighted avg"]
        self.entities = self._to_list(self.entities, "f1-score")

    def _load_entity_errors(self) -> None:
        """
        Load Rasa entity errors report data.
        """
        self.entity_errors = self.load_json_file(self.entity_errors_path, error_flag=False)

    def _load_responses(self) -> None:
        """
        Load Rasa response report data.
        """
        self.responses = self.load_json_file(self.story_report_path, error_flag=False)
        if self.responses:
            self.response_overview = {
                "macro avg": self.responses.get("macro avg"),
                "weighted avg": self.responses.get("weighted avg"),
                "conversation_accuracy": self.responses.get("conversation_accuracy")
            }
            del self.responses["macro avg"]
            del self.responses["weighted avg"]
            if self.responses.get("accuracy"):
                del self.responses["accuracy"]
            if self.responses.get("conversation_accuracy"):
                del self.responses["conversation_accuracy"]
            self.responses = self._to_list(self.responses, "f1-score")

    def _load_overview(self) -> None:
        """
        Load overview report data.
        """
        intent_overview = self.intent_overview.get("macro avg", {}).get("f1-score")
        entity_overview = self.entity_overview.get("macro avg", {}).get("f1-score")
        response_overview = self.response_overview.get("macro avg", {}).get("f1-score")
        nlu_overview = self.overview.get("nlu")
        self.overview.update({
            "updated_at": format_date(),
            "intent": intent_overview if intent_overview is not None else None,
            "entity": entity_overview if entity_overview is not None else None,
            "response": response_overview if response_overview is not None else None,
            "nlu": nlu_overview
        })
        self._calculate_overall()
        if os.path.isfile(self.overview_report_path):
            file = open(self.overview_report_path, encoding="utf-8")
            data = json.load(file)
            file.close()
            self.overview.update({
                "created_at": data.get("created_at")
            })
            logging.info(f"Arquivo {self.overview_report_path} carregado com sucesso")
        else:
            self.overview.update({
                "created_at": format_date()
            })
            logging.error(f"Arquivo {self.overview_report_path} não foi localizado")

    def save_overview(self) -> None:
        """
        Save overview report data.
        """
        logging.info(f"Arquivo {self.overview_report_path} salvo com sucesso")
        file = open(self.overview_report_path, "w", encoding="utf-8")
        json.dump(self.overview, file, indent=4)
        file.write("\n")
        file.close()

    def _calculate_overall(self) -> None:
        weights = {
            "intent": 3,
            "entity": 2,
            "response": 1,
            "nlu": 4
        }
        overview_sum = sum(
            self.overview[item] * w for item, w in weights.items()
            if isinstance(self.overview[item], (int, float)) and self.overview[item] >= 0
        )
        weight_sum = sum(
            w for item, w in weights.items()
            if isinstance(self.overview[item], (int, float)) and self.overview[item] >= 0
        )
        overview_rate = overview_sum / weight_sum if weight_sum else 0
        self.overview.update({
            "overall": overview_rate
        })

    def update_overview(self, obj: Dict[Any, Any]) -> None:
        """
        Update overview report data.

        :param obj: Object that will be used to update the overview object.
        """
        if isinstance(obj, dict):
            self.overview.update(obj)
            self._calculate_overall()

    def get_intents(self) -> Dict[str, Any]:
        """
        Get intents data.

        :return: Copy of intents data object.
        """
        return self.intents.copy()

    def get_intent_overview(self) -> Dict[str, float]:
        """
        Get intent overview data.

        :return: Copy of intent overview data object.
        """
        return self.intent_overview.copy()

    def get_intent_errors(self) -> List[Dict[str, Any]]:
        """
        Get intent errors data.

        :return: Copy of intent errors data object.
        """
        return self.intent_errors.copy()

    def get_entities(self) -> List[Dict[str, Any]]:
        """
        Get entities data.

        :return: Copy of entities data object.
        """
        return self.entities.copy()

    def get_entity_overview(self) -> Dict[str, float]:
        """
        Get entity overview data.

        :return: Copy of entity overview data object.
        """
        return self.entity_overview.copy()

    def get_entity_errors(self) -> List[Dict[str, Any]]:
        """
        Get entity errors data.

        :return: Copy of entity errors data object.
        """
        return self.entity_errors.copy()

    def get_responses(self) -> List[Dict[str, Any]]:
        """
        Get responses data.

        :return: Copy of responses data object.
        """
        return self.responses.copy()

    def get_response_overview(self) -> Dict[str, float]:
        """
        Get response overview data.

        :return: Copy of response overview data object.
        """
        return self.response_overview.copy()

    def get_overview(self) -> Dict[str, Union[str, float, int]]:
        """
        Get overview data.

        :return: Copy of overview data object.
        """
        return self.overview.copy()

    def _to_list(self, data, sort_field=None) -> list:
        """
        Transforma o JSON dos reports em lista.
        """
        new_list = []
        for item in data:
            if isinstance(data[item], dict):
                element = {}
                element["name"] = item
                element.update(data[item])
                new_list.append(element)
        if sort_field:
            new_list = sorted(new_list, key=lambda x: x[sort_field], reverse=True)
        return new_list
