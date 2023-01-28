import glob
import logging
from typing import Dict
from typing import List
from typing import Union

from rasa_model_report.controllers.controller import Controller
from rasa_model_report.controllers.json_controller import JsonController
from rasa_model_report.helpers.utils import list_diff
from rasa_model_report.helpers.utils import load_yaml_file


class E2ECoverageController(Controller):
    def __init__(
        self,
        rasa_path: str,
        output_path: str,
        project_name: str,
        project_version: str,
        **kwargs: dict
    ):
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project_name: Project name.
        :param project_version: Project version.
        """
        super().__init__(rasa_path, output_path, project_name, project_version)

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
            file_data = load_yaml_file(file)
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

    def _generate(self) -> None:
        """
        Generate E2E tests coverage report string.
        """
        not_covered = {}
        report_data = [item["name"] for item in self.json.core]
        for element in ["intents", "entities", "actions"]:
            element_list = getattr(self, f"_{element}")
            not_covered[element] = {
                "items": list_diff(element_list, report_data)
            }
            not_covered[element]["rate"] = 0
            if element_list:
                not_covered[element]["rate"] = 1 - len(not_covered[element]["items"]) / len(element_list)
            self._total_num_elements += len(element_list)
            self._total_num_not_covered += len(not_covered[element]["items"])
        self._data = not_covered
        if self.have_not_covered_items():
            self._total_rate = 1 - self._total_num_not_covered / self._total_num_elements

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
        return True in [bool(element["items"]) for element in self._data.values()]

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
