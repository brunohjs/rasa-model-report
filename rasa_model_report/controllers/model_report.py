import logging
import os.path
from typing import Any
from typing import Dict

from rasa_model_report.controllers.markdown_controller import MarkdownController
from rasa_model_report.helpers.utils import get_project_name


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
        self.project_name: str = project_name if project_name else get_project_name(rasa_path)
        self.project_version: str = project_version
        self.rasa_version: str = rasa_version
        self.markdown: MarkdownController = MarkdownController(
            rasa_path,
            output_path,
            self.project_name,
            self.rasa_version,
            self.project_version,
            **kwargs
        )
        self.dirs: Dict[str, str] = {
            "rasa_path": rasa_path,
            "results_path": f"{rasa_path}/results",
            "output_path": output_path,
            "INTENT_HISTOGRAM": "intent_histogram.png",
            "INTENT_MATRIX": "intent_confusion_matrix.png",
            "ENTITY_HISTOGRAM": "DIETClassifier_histogram.png",
            "ENTITY_MATRIX": "DIETClassifier_confusion_matrix.png",
            "STORY_MATRIX": "story_confusion_matrix.png"
        }

        logging.info("---")
        logging.info(
            f"Starting report creation from {self.project_name} bot template, "
            f"version {self.project_version if self.project_version else 'not identified'}"
        )
        self.generate_report()

    def generate_report(self) -> None:
        """
        Function that generates the report.
        """
        if os.path.isdir(self.dirs["results_path"]):
            # Overview
            self.markdown.add_text(self.markdown.title)
            self.markdown.add_text(self.markdown.build_summary())
            self.markdown.add_text(self.markdown.build_overview())
            self.markdown.break_line()

            # Config
            self.markdown.add_text(self.markdown.build_config_report())
            self.markdown.break_line()

            # Intents
            self.markdown.add_text(self.markdown.build_intent_title())
            self.markdown.add_text(self.markdown.build_intent_table())
            self.markdown.add_text(self.markdown.build_intent_errors_table())
            self.markdown.add_image(self.dirs["INTENT_HISTOGRAM"], "Histogram")
            self.markdown.add_image(self.dirs["INTENT_MATRIX"], "Confusion Matrix")

            # Entities
            self.markdown.add_text(self.markdown.build_entity_title())
            self.markdown.add_text(self.markdown.build_entity_table())
            self.markdown.add_text(self.markdown.build_entity_errors_table())
            self.markdown.add_image(self.dirs['ENTITY_HISTOGRAM'], "Histogram")
            self.markdown.add_image(self.dirs['ENTITY_MATRIX'], "Confusion Matrix")

            # NLU
            if self.markdown.nlu.is_connected():
                self.markdown.add_text(self.markdown.build_nlu_title())
                self.markdown.add_text(self.markdown.build_nlu_table())
                self.markdown.add_text(self.markdown.build_nlu_errors_table())

            # Core
            self.markdown.add_text(self.markdown.build_core_title())
            self.markdown.add_text(self.markdown.build_core_table())
            self.markdown.add_image(self.dirs['STORY_MATRIX'], "Confusion Matrix")

            # E2E Coverage
            self.markdown.add_text(self.markdown.build_e2e_coverage_title())
            self.markdown.add_text(self.markdown.build_e2e_coverage_list())

            # Credits
            self.markdown.add_text(self.markdown.build_credits())

            # Save report and overview files
            self.markdown.save_report()
            self.markdown.save_overview()

            logging.info("Script successfully completed.")
        else:
            logging.error(f"{self.dirs['results_path']} directory doesn't exist.")
            logging.error(
                "To inform the directory where the Rasa project files are located, use the --path parameter."
            )
            logging.error("Script finished with errors.")
