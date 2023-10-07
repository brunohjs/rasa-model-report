import logging
from typing import Any
from typing import Dict

from rasa_model_report.controllers.output_controller import OutputController
from rasa_model_report.helpers import constants
from rasa_model_report.helpers import utils


class ModelReport:
    """
    Class responsible to generate report.
    """
    def __init__(
        self,
        rasa_path: str,
        output_path: str,
        project_name: str,
        rasa_version: str,
        project_version: str,
        **kwargs: Dict[str, Any]
    ):
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project_name: Project name.
        :param rasa_version: Rasa version.
        :param project_version: Project version.
        """
        self.project_name: str = project_name if project_name else utils.get_project_name(rasa_path)
        self.project_version: str = project_version
        self.rasa_version: str = rasa_version
        self.output_format = kwargs.get("output_format", constants.OUTPUT_FORMAT)
        logging.info("---")
        logging.info(
            f"Starting report creation from {self.project_name} bot template, "
            f"version {self.project_version if self.project_version else 'not identified'}"
        )
        self.generator: OutputController = OutputController(
            rasa_path,
            output_path,
            self.project_name,
            self.rasa_version,
            self.project_version,
            **kwargs
        )
        self.generator.generate_report()
