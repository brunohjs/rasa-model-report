import glob
import logging
import re
from typing import Any
from typing import Dict
from typing import List
from typing import Union

from rasa_model_report.controllers.controller import Controller
from rasa_model_report.controllers.json_controller import JsonController
from rasa_model_report.helpers import utils


class E2ECoverageController(Controller):
    def __init__(
        self,
        rasa_path: str,
        output_path: str,
        actions_path: str,
        project_name: str,
        project_version: str,
        **kwargs: Dict[str, Any]
    ):
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project_name: Project name.
        :param project_version: Project version.
        """
        super().__init__(rasa_path, output_path, project_name, project_version, actions_path=actions_path)

        self._data: Dict[str, Union[List[str], float]] = {}
        self._total_num_elements: int = 0
        self._total_num_not_covered: int = 0
        self._intents: List[str] = []
        self._entities: List[str] = []
        self._actions: List[str] = []
        self._total_rate: float = 0
        self.json: JsonController = JsonController(rasa_path, output_path, project_name, project_version)

        self._load_domain_elements()
        self._generate()
        self.save()

    def _load_domain_elements(self) -> None:
        """
        Load domain file data.
        """
        files = []
        paths = [
            f"{self.nlu_path}/**/*.yml",
            f"{self.nlu_path}/*.yml",
            f"{self.rasa_path}/*.yml"
        ]
        for path in paths:
            files.extend(glob.glob(path))
        for file in files:
            file_data = utils.load_yaml_file(file)
            if file_data:
                for element in ["intents", "entities", "responses", "actions"]:
                    data = []
                    for item in file_data.get(element, []):
                        if isinstance(item, str):
                            data.append(item)
                        else:
                            data.append(list(item.keys())[0])
                    if element == "responses":
                        setattr(self, "_actions", getattr(self, "_actions") + data)
                    else:
                        setattr(self, f"_{element}", getattr(self, f"_{element}") + data)
        self._actions = list(dict.fromkeys(self._actions))
        self._actions = self._exclude_special_actions()
        self._actions = utils.list_diff(self._actions, self.get_utters_in_actions())

    def _generate(self) -> None:
        """
        Generate E2E tests coverage report string.
        """
        not_covered = {}
        report_data = [self.json.extract_entity_from_string(item["name"]) for item in self.json.core]
        for element in ["intents", "entities", "actions"]:
            element_list = getattr(self, f"_{element}")
            not_covered[element] = {
                "items": utils.list_diff(element_list, report_data)
            }
            not_covered[element]["rate"] = 0
            if element_list:
                not_covered[element]["rate"] = 1 - len(not_covered[element]["items"]) / len(element_list)
            self._total_num_elements += len(element_list)
            self._total_num_not_covered += len(not_covered[element]["items"])
        self._data = not_covered
        if self._total_num_elements:
            self._total_rate = 1 - self._total_num_not_covered / self._total_num_elements

    def _exclude_special_actions(self) -> List[str]:
        """
        Exclude special actions from coverage report, like actions_ask_slot and validates.

        :return: Actions list without special actions.
        """
        actions = []
        for item in self._actions:
            patterns_to_exclude = [
                item.startswith("action_ask_"),
                item.startswith("utter_ask_"),
                item.startswith("validate_")
            ]
            if True not in patterns_to_exclude:
                actions.append(item)
        return actions

    def get_utters_in_actions(self) -> List[str]:
        """
        Get all utters in actions code.

        :return: Found utter list.
        """
        result = []
        patterns = [
            r"template|response\s?=\s?[\'|\"].*[\'|\"]",
            r"FollowupAction\(\s?[\'|\"].*[\'|\"]\s?\)",
            r"ActionExecuted\(\s?[\'|\"].*[\'|\"]\s?\)"
        ]
        actions_data = glob.glob(f"{self.actions_path}/**/*.py") + glob.glob(f"{self.actions_path}/*.py")
        actions_files = [open(file).read() for file in actions_data]
        for file in actions_files:
            for pattern in patterns:
                strings = re.findall(pattern, file)
                if strings:
                    for string in strings:
                        utter = re.search(r"(utter|action)_[a-zA-Z0-9_-]+", string)
                        if utter and utter.group() not in result:
                            result.append(utter.group())
        return result

    def save(self) -> None:
        """
        Save E2E tests coverage report to a text file.
        """
        file_path = f"{self.results_path}/e2e_coverage_report.txt"
        if self.have_not_covered_items():
            with open(file_path, "w") as file:
                file.write("-------------------------------------------------\n")
                file.write("End-to-end tests coverage report\n")
                file.write("-------------------------------------------------\n")
                file.write("Elements that aren't covered:\n")
                for element in self._data:
                    file.write(f" + {element.capitalize()}\n")
                    if self._data[element].get("items"):
                        for item in self._data[element]["items"]:
                            file.write(f"   - {item}\n")
                    else:
                        file.write("   - (no elements not covered)\n")
                file.write("\n")
                file.write(f"Total number of elements: {self._total_num_elements}\n")
                file.write(f"Total number of not covered elements: {self._total_num_not_covered}\n")
                file.write(f"Coverage rate: {self._total_rate * 100:.1f}%\n")
                file.write("-------------------------------------------------\n")
            logging.info(f"{file_path} file successfully saved.")
        else:
            logging.info("All elements are included in end-to-end tests.")

    def have_not_covered_items(self) -> bool:
        """
        Returns 'True' if have some not covered element in model E2E tests.

        :return: Flag that represents if have not covered elements.
        """
        return self._total_num_not_covered > 0

    @property
    def data(self) -> Dict[str, Union[List[str], float]]:
        """
        Get E2E tests not covered elements data.

        :return: Copy of E2E tests not covered elements data.
        """
        return self._data.copy()

    @property
    def total_rate(self) -> float:
        """
        Get E2E tests coverage rate.

        :return float: Copy of E2E tests coverage rate.
        """
        return self._total_rate

    @property
    def total_num_elements(self) -> int:
        """
        Get total number of E2E tests elements.

        :return int: Total number of E2E tests elements.
        """
        return self._total_num_elements

    @property
    def total_num_not_covered(self) -> int:
        """
        Get total number of E2E tests not covered elements.

        :return int: Total number of E2E tests not covered elements.
        """
        return self._total_num_not_covered
