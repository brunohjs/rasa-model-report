import glob
from typing import Dict
from typing import List
from typing import Union

from rasa_model_report.controllers.controller import Controller
from rasa_model_report.controllers.json_controller import JsonController
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
        self.domain_path: str = f"{self.rasa_path}/domain.yml".replace("//", "/")
        self.json: JsonController = JsonController(rasa_path, output_path, project_name, project_version)

        self._load_domain_elements()

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
        self._generate()

    def _generate(self) -> Dict[str, Union[List[str], float]]:
        not_covered = {}
        report_data = [item["name"] for item in self.json.responses]
        for element in ["intents", "entities", "actions"]:
            element_list = getattr(self, f"_{element}")
            not_covered[element] = {
                "items": self.diff(element_list, report_data)
            }
            not_covered[element]["rate"] = 0
            if element_list:
                not_covered[element]["rate"] = 1 - len(not_covered[element]["items"]) / len(element_list)
            self._total_num_elements += len(element_list)
            self._total_num_not_covered += len(not_covered[element]["items"])
        if True in [bool(element["items"]) for element in not_covered.values()]:
            self._data = not_covered
            self._total_rate = 1 - self._total_num_not_covered / self._total_num_elements
        else:
            self._data = {}
            self._total_rate = 0

    @staticmethod
    def diff(l1: List[str], l2: List[str]) -> List[str]:
        return [element for element in l1 if element not in l2]

    @property
    def data(self):
        return self._data.copy()

    @property
    def total_rate(self):
        return self._total_rate

    @property
    def total_num_elements(self):
        return self._total_num_elements

    @property
    def total_num_not_covered(self):
        return self._total_num_not_covered
