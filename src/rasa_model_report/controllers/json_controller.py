import json
import logging
import os.path

from src.rasa_model_report.controllers.controller import Controller
from src.rasa_model_report.helpers.type_aliases import entity
from src.rasa_model_report.helpers.type_aliases import intent
from src.rasa_model_report.helpers.type_aliases import number
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

        self._intents: list[dict[str, intent]] = []
        self._intent_overview: dict[str, float] = {}
        self._intent_errors: list[dict[str, intent]] = []
        self._entities: list[dict[str, entity]] = []
        self._entity_overview: dict[str, float] = {}
        self._entity_errors: list[dict[str, entity]] = []
        self._responses: list[dict[str, float]] = []
        self._response_overview: dict[str, float] = {}
        self._overview: dict[str, str | number] = {
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

    def load_json_file(self, filename: str, error_flag: bool = True) -> dict | list:
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
        self._load_responses()
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

    def _load_responses(self) -> None:
        """
        Load Rasa response report data.
        """
        self._responses = self.load_json_file(self.story_report_path, error_flag=False)
        if self._responses:
            self._response_overview = {
                "macro avg": self._responses.get("macro avg"),
                "weighted avg": self._responses.get("weighted avg"),
                "conversation_accuracy": self._responses.get("conversation_accuracy")
            }
            del self._responses["macro avg"]
            del self._responses["weighted avg"]
            if self._responses.get("accuracy"):
                del self._responses["accuracy"]
            if self._responses.get("conversation_accuracy"):
                del self._responses["conversation_accuracy"]
            self._responses = self._to_list(self._responses, "f1-score")

    def _load_overview(self) -> None:
        """
        Load overview report data.
        """
        intent_overview = self._intent_overview.get("macro avg", {}).get("f1-score")
        entity_overview = self._entity_overview.get("macro avg", {}).get("f1-score")
        response_overview = self._response_overview.get("macro avg", {}).get("f1-score")
        nlu_overview = self._overview.get("nlu")
        self._overview.update({
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
            self._overview.update({
                "created_at": data.get("created_at")
            })
            logging.info(f"{self.overview_report_path} file loaded successfully.")
        else:
            self._overview.update({
                "created_at": format_date()
            })
            logging.error(f"{self.overview_report_path} file not found.")

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
            "intent": 3,
            "entity": 2,
            "response": 1,
            "nlu": 4
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

    def update_overview(self, obj: dict[str, number]) -> None:
        """
        Update overview report data.

        :param obj: Object that will be used to update the overview object.
        """
        if isinstance(obj, dict):
            self._overview.update(obj)
            self._calculate_overall()

    @property
    def intents(self) -> dict[str, intent]:
        """
        Get intents data.

        :return: Copy of intents data object.
        """
        return self._intents.copy()

    @property
    def intent_overview(self) -> dict[str, float]:
        """
        Get intent overview data.

        :return: Copy of intent overview data object.
        """
        return self._intent_overview.copy()

    @property
    def intent_errors(self) -> list[dict[str, intent]]:
        """
        Get intent errors data.

        :return: Copy of intent errors data object.
        """
        return self._intent_errors.copy()

    @property
    def entities(self) -> list[dict[str, entity]]:
        """
        Get entities data.

        :return: Copy of entities data object.
        """
        return self._entities.copy()

    @property
    def entity_overview(self) -> dict[str, float]:
        """
        Get entity overview data.

        :return: Copy of entity overview data object.
        """
        return self._entity_overview.copy()

    @property
    def entity_errors(self) -> list[dict[str, entity]]:
        """
        Get entity errors data.

        :return: Copy of entity errors data object.
        """
        return self._entity_errors.copy()

    @property
    def responses(self) -> list[dict[str, float]]:
        """
        Get responses data.

        :return: Copy of responses data object.
        """
        return self._responses.copy()

    @property
    def response_overview(self) -> dict[str, float]:
        """
        Get response overview data.

        :return: Copy of response overview data object.
        """
        return self._response_overview.copy()

    @property
    def overview(self) -> dict[str, str | float]:
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
