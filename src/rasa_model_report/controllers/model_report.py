import logging
import os.path

from src.rasa_model_report.controllers.markdown_controller import MarkdownController
from src.rasa_model_report.helpers.utils import get_project_name


class ModelReport:
    """
    Class responsible to generate report.
    """
    def __init__(self, rasa_path: str, output_path: str, project: str, version: str, **kwargs: dict):
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project: Project name.
        :param version: Project version.
        """
        self.project: str = project if project else get_project_name(rasa_path)
        self.version: str = version
        self.markdown: MarkdownController = MarkdownController(
            rasa_path,
            output_path,
            self.project,
            self.version,
            **kwargs
        )
        self.dirs: dict[str, str] = {
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
            f"Starting report creation from {self.project} bot template,"
            f"version {self.version if self.version else 'not identified'}"
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

            # Responses
            self.markdown.add_text(self.markdown.build_response_title())
            self.markdown.add_text(self.markdown.build_response_table())
            self.markdown.add_image(self.dirs['STORY_MATRIX'], "Confusion Matrix")

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
