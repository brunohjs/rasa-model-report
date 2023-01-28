import json
import logging
import os.path
from typing import Dict
from typing import List
from typing import Union

from rasa_model_report.controllers.controller import Controller
from rasa_model_report.helpers.type_aliases import entity
from rasa_model_report.helpers.type_aliases import intent
from rasa_model_report.helpers.type_aliases import number
from rasa_model_report.helpers.utils import format_date


class JsonController(Controller):
    """
    Controller responsible for JSON files.
    """
    def __init__(self, rasa_path: str, output_path: str, project_name: str, project_version: str) -> None:
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project_name: Project name.
        :param project_version: Project version.
        """
        super().__init__(rasa_path, output_path, project_name, project_version)

        self._intents: List[Dict[str, intent]] = []
        self._intent_overview: Dict[str, float] = {}
        self._intent_errors: List[Dict[str, intent]] = []
        self._entities: List[Dict[str, entity]] = []
        self._entity_overview: Dict[str, float] = {}
        self._entity_errors: List[Dict[str, entity]] = []
        self._core: List[Dict[str, float]] = []
        self._core_overview: Dict[str, float] = {}
        self._overview: Dict[str, Union[str, number]] = {
            "project": project_name,
            "version": project_version
        }
        self.intent_report_path: str = f"{self.results_path}/intent_report.json"
        self.intent_errors_path: str = f"{self.results_path}/intent_errors.json"
        self.entity_report_path: str = f"{self.results_path}/DIETClassifier_report.json"
        self.entity_errors_path: str = f"{self.results_path}/DIETClassifier_errors.json"
        self.story_report_path: str = f"{self.results_path}/story_report.json"
        self.overview_report_path: str = f"{self.results_path}/overview.json"

        self._load_data()

    @staticmethod
    def load_json_file(filename: str, error_flag: bool = True) -> Union[dict, list]:
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
            logging.info(f"{filename} file loaded successfully.")
            return data
        else:
            message = f"{filename} file not found."
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
        self._load_core()
        self._load_overview()

    def _load_intents(self) -> None:
        """
        Load Rasa intent report data.
        """
        self._intents = self.load_json_file(self.intent_report_path, error_flag=False)
        if self._intents:
            self._intent_overview = {
                "accuracy": self._intents.get("accuracy"),
                "macro avg": self._intents.get("macro avg"),
                "weighted avg": self._intents.get("weighted avg")
            }
            del self._intents["accuracy"]
            del self._intents["macro avg"]
            if self._intents.get("micro avg"):
                del self._intents["micro avg"]
            del self._intents["weighted avg"]
        self._intents = self._to_list(self._intents, "f1-score")

    def _load_intent_errors(self) -> None:
        """
        Load Rasa intent errors report data.
        """
        self._intent_errors = self.load_json_file(self.intent_errors_path, error_flag=False)
        self._intent_errors = sorted(
            self._intent_errors,
            key=lambda d: d["intent_prediction"]["confidence"],
            reverse=True
        )

    def _load_entities(self) -> None:
        """
        Load Rasa entity report data.
        """
        self._entities = self.load_json_file(self.entity_report_path, error_flag=False)
        if self._entities:
            self._entity_overview = {
                "macro avg": self._entities.get("macro avg"),
                "micro avg": self._entities.get("micro avg"),
                "weighted avg": self._entities.get("weighted avg")
            }
            del self._entities["macro avg"]
            del self._entities["micro avg"]
            del self._entities["weighted avg"]
        self._entities = self._to_list(self._entities, "f1-score")

    def _load_entity_errors(self) -> None:
        """
        Load Rasa entity errors report data.
        """
        self._entity_errors = self.load_json_file(self.entity_errors_path, error_flag=False)

    def _load_core(self) -> None:
        """
        Load Rasa core report data.
        """
        self._core = self.load_json_file(self.story_report_path, error_flag=False)
        if self._core:
            self._core_overview = {
                "macro avg": self._core.get("macro avg"),
                "weighted avg": self._core.get("weighted avg"),
                "conversation_accuracy": self._core.get("conversation_accuracy")
            }
            del self._core["macro avg"]
            del self._core["weighted avg"]
            if self._core.get("accuracy"):
                del self._core["accuracy"]
            if self._core.get("conversation_accuracy"):
                del self._core["conversation_accuracy"]
            self._core = self._to_list(self._core, "f1-score")

    def _load_overview(self) -> None:
        """
        Load overview report data.
        """
        intent_overview = self._intent_overview.get("macro avg", {}).get("f1-score")
        entity_overview = self._entity_overview.get("macro avg", {}).get("f1-score")
        core_overview = self._core_overview.get("macro avg", {}).get("f1-score")
        nlu_overview = self._overview.get("nlu")
        e2e_coverage_overview = self._overview.get("e2e_coverage")
        self._overview.update({
            "updated_at": format_date(),
            "intent": intent_overview if intent_overview is not None else None,
            "entity": entity_overview if entity_overview is not None else None,
            "core": core_overview if core_overview is not None else None,
            "nlu": nlu_overview,
            "e2e_coverage": e2e_coverage_overview
        })
        self._calculate_overall()
        if os.path.isfile(self.overview_report_path):
            file = open(self.overview_report_path, encoding="utf-8")
            data = json.load(file)
            file.close()
            self._overview.update({
                "created_at": data.get("created_at")
            })
            logging.info(f"{self.overview_report_path} file loaded successfully.")
        else:
            self._overview.update({
                "created_at": format_date()
            })
            logging.warn(f"{self.overview_report_path} file not found.")

    def save_overview(self) -> None:
        """
        Save overview report data.
        """
        logging.info(f"{self.overview_report_path} file successfully saved.")
        file = open(self.overview_report_path, "w", encoding="utf-8")
        json.dump(self._overview, file, indent=4)
        file.write("\n")
        file.close()

    def _calculate_overall(self) -> None:
        weights = {
            "intent": 2,
            "entity": 1,
            "core": 1,
            "nlu": 3,
            "e2e_coverage": 3
        }
        overview_sum = sum(
            self._overview[item] * w for item, w in weights.items()
            if isinstance(self._overview[item], (int, float)) and self._overview[item] >= 0
        )
        weight_sum = sum(
            w for item, w in weights.items()
            if isinstance(self._overview[item], (int, float)) and self._overview[item] >= 0
        )
        overview_rate = overview_sum / weight_sum if weight_sum else 0
        self._overview.update({
            "overall": overview_rate
        })

    def update_overview(self, obj: Dict[str, number]) -> None:
        """
        Update overview report data.

        :param obj: Object that will be used to update the overview object.
        """
        if isinstance(obj, dict):
            obj.update({"updated_at": format_date()})
            self._overview.update(obj)
            self._calculate_overall()

    @property
    def intents(self) -> Dict[str, intent]:
        """
        Get intents data.

        :return: Copy of intents data object.
        """
        return self._intents.copy()

    @property
    def intent_overview(self) -> Dict[str, float]:
        """
        Get intent overview data.

        :return: Copy of intent overview data object.
        """
        return self._intent_overview.copy()

    @property
    def intent_errors(self) -> List[Dict[str, intent]]:
        """
        Get intent errors data.

        :return: Copy of intent errors data object.
        """
        return self._intent_errors.copy()

    @property
    def entities(self) -> List[Dict[str, entity]]:
        """
        Get entities data.

        :return: Copy of entities data object.
        """
        return self._entities.copy()

    @property
    def entity_overview(self) -> Dict[str, float]:
        """
        Get entity overview data.

        :return: Copy of entity overview data object.
        """
        return self._entity_overview.copy()

    @property
    def entity_errors(self) -> List[Dict[str, entity]]:
        """
        Get entity errors data.

        :return: Copy of entity errors data object.
        """
        return self._entity_errors.copy()

    @property
    def core(self) -> List[Dict[str, float]]:
        """
        Get core data.

        :return: Copy of core data object.
        """
        return self._core.copy()

    @property
    def core_overview(self) -> Dict[str, float]:
        """
        Get core overview data.

        :return: Copy of core overview data object.
        """
        return self._core_overview.copy()

    @property
    def overview(self) -> Dict[str, Union[str, float]]:
        """
        Get overview data.

        :return: Copy of overview data object.
        """
        return self._overview.copy()

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
