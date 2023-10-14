import copy
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
        exclude: List[str],
        project_name: str,
        project_version: str,
        **kwargs: Dict[str, Any],
    ):
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project_name: Project name.
        :param project_version: Project version.
        """
        super().__init__(
            rasa_path,
            output_path,
            project_name,
            project_version,
            actions_path=actions_path,
        )

        self._total_num_elements: int = 0
        self._total_num_not_covered: int = 0
        self._total_num_excluded: int = 0
        self._items: Dict[str, Union[float, List[str]]] = {
            item: [] for item in ["intents", "actions"]
        }
        self._not_covered_items: Dict[str, Union[float, List[str]]] = {
            item: [] for item in ["intents", "actions"]
        }
        self._rate_items: Dict[str, Union[float, List[str]]] = {}
        self._total_rate: float = 0
        self._excluded_items = exclude
        self.json: JsonController = JsonController(
            rasa_path, output_path, project_name, project_version
        )

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
            f"{self.rasa_path}/*.yml",
        ]
        for path in paths:
            files.extend(glob.glob(path))
        for file in files:
            file_data = utils.load_yaml_file(file)
            if file_data:
                for element in ["intents", "responses", "actions"]:
                    data = []
                    for item in file_data.get(element, []):
                        if isinstance(item, str):
                            data.append(item)
                        else:
                            data.append(list(item.keys())[0])
                    if element == "responses":
                        self._items["actions"] += data
                    else:
                        self._items[element] += data
        self._items["actions"] = list(dict.fromkeys(self._items["actions"]))
        self._update_not_covered_actions()

    def _generate(self) -> None:
        """
        Generate E2E tests coverage report string.
        """
        report_data = [item["name"] for item in self.json.core]
        for element in ["intents", "actions"]:
            self._not_covered_items[element] = utils.list_diff(
                self._not_covered_items[element], report_data
            )
            self._rate_items[element] = 0
            if self._items[element]:
                self._rate_items[element] = 1 - len(
                    self._not_covered_items[element]
                ) / (
                    len(self._items[element]) + self._total_num_excluded
                    if element == "actions"
                    else len(self._items[element])
                )
            self._total_num_elements += len(self._items[element])
            self._total_num_not_covered += len(self._not_covered_items[element])
        if self._total_num_elements - self._total_num_excluded:
            self._total_rate = 1 - self._total_num_not_covered / (
                self._total_num_elements - self._total_num_excluded
            )

    def _exclude_special_actions(self) -> List[str]:
        """
        Exclude special actions from coverage report, like actions_ask_slot and validates.

        :return: Actions list without special actions.
        """
        actions = []
        for item in self._items["actions"]:
            patterns_to_exclude = [
                item.startswith("action_ask_"),
                item.startswith("utter_ask_"),
                item.startswith("validate_"),
            ]
            if True not in patterns_to_exclude:
                actions.append(item)
        self._total_num_excluded += len(self._items["actions"]) - len(actions)
        return actions

    def get_utters_in_actions(self) -> List[str]:
        """
        Get all utters in actions code.

        :return: Found utter list.
        """
        result = []
        pattern = (
            r"(\"(utter|action)_[a-zA-Z0-9_-]+\")|((\'(utter|action)_[a-zA-Z0-9_-]+\'))"
        )
        actions_data = glob.glob(f"{self.actions_path}/**/*.py") + glob.glob(
            f"{self.actions_path}/*.py"
        )
        actions_files = [open(file).read() for file in actions_data]
        for file in actions_files:
            strings = re.findall(pattern, file, re.UNICODE)
            if strings:
                for string in strings:
                    for element in string:
                        if element and ("utter_" in element or "action_" in element):
                            utter = element.replace("'", "").replace('"', "")
                            if utter not in result:
                                result.append(utter)
        return result

    def _update_not_covered_actions(self) -> None:
        """
        Update not covered actions list.
        """
        self._not_covered_items = copy.deepcopy(self._items)
        self._not_covered_items["actions"] = self._exclude_special_actions()
        self._total_num_excluded += len(self._not_covered_items["actions"]) - len(
            utils.list_diff(self._not_covered_items["actions"], self._excluded_items)
        )
        self._not_covered_items["actions"] = utils.list_diff(
            self._not_covered_items["actions"], self._excluded_items
        )
        self._not_covered_items["actions"] = utils.list_diff(
            self._not_covered_items["actions"], self.get_utters_in_actions()
        )

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
                for element in self._not_covered_items:
                    file.write(f" + {element.capitalize()}\n")
                    if self._not_covered_items[element]:
                        for item in self._not_covered_items[element]:
                            file.write(f"   - {item}\n")
                    else:
                        file.write("   - (no elements not covered)\n")
                file.write("\n")
                file.write(f"Total number of elements: {self.total_num_elements}\n")
                file.write(
                    f"Total number of not covered elements: {self.total_num_not_covered}\n"
                )
                file.write(
                    f"Total number of excluded elements: {self.total_num_excluded}\n"
                )
                file.write(f"Coverage rate: {self.total_rate * 100:.1f}%\n")
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
    def items(self) -> List[str]:
        """
        Get E2E tests elements data.

        :return: Copy of E2E tests elements data.
        """
        return copy.deepcopy(self._items)

    @property
    def not_covered_items(self) -> Dict[str, Union[List[str], float]]:
        """
        Get E2E tests not covered elements data.

        :return: Copy of E2E tests not covered elements data.
        """
        return copy.deepcopy(self._not_covered_items)

    @property
    def total_rate(self) -> float:
        """
        Get E2E tests coverage rate.

        :return float: Copy of E2E tests coverage rate.
        """
        return self._total_rate

    @property
    def total_num_elements(self, with_excluded_items: bool = False) -> int:
        """
        Get total number of E2E tests elements.

        :return int: Total number of E2E tests elements.
        """
        return (
            self._total_num_elements
            if with_excluded_items
            else self._total_num_elements - self._total_num_excluded
        )

    @property
    def total_num_not_covered(self) -> int:
        """
        Get total number of E2E tests not covered elements.

        :return int: Total number of E2E tests not covered elements.
        """
        return self._total_num_not_covered

    @property
    def total_num_excluded(self) -> int:
        """
        Get total number of E2E tests excluded elements.

        :return int: Total number of E2E tests excluded elements.
        """
        return self._total_num_excluded
