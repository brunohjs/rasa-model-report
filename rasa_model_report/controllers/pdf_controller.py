import logging
import os.path

from rasa_model_report.controllers.output_controller import OutputController
from rasa_model_report.helpers import utils


class PdfController(OutputController):
    """
    Controller responsible for PDF files.
    """
    def __init__(
        self,
        rasa_path: str,
        output_path: str,
        project_name: str,
        rasa_version: str,
        project_version: str,
        **kwargs
    ) -> None:
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project_name: Project name.
        :param rasa_version: Rasa version.
        :param project_version: Project version.
        """
        super().__init__(
            rasa_path,
            output_path,
            project_name,
            rasa_version,
            project_version,
            **kwargs
        )

        self.output_report_path: str = utils.remove_duplicate_slashs(f"{self.output_path}/model_report.html")

    def add_text(self, text: str) -> None:
        """
        Concatenates a text to the result text.

        :param text: Text that concatenates.
        """
        if isinstance(text, str):
            self.result += f"\n <p>{text}</p>"

    def add_image(self, image_filename: str, title: str) -> None:
        """
        Concatenates image (markdown format) into the result text.

        :param image_filename: Image file name.
        :param title: Image title.
        """
        if self.no_images:
            return None
        if os.path.isfile(f"{self.results_path}/{image_filename}"):
            image_path = utils.path_to(self.output_path, self.results_path) + image_filename
            self.result += f"<h3>{title}</h3>\n<img alt={title} src='{image_path}'>\n"
            logging.info(f"Image {image_filename} has been successfully added.")
        else:
            logging.warning(f"Image {self.results_path}/{image_filename} was not found.")

    def add_title(self, title, description=None, heading_level=2, tag=None):
        """
        Concatenates a title and description to the result text.

        :param title: Title text.
        :param description: Description text (default: None).
        :param int heading_level: Heading level (default: 2).
        :param tag: Tag for an anchor link (default: None).
        """
        title = f"<h{heading_level}>{title}</h{heading_level}>"
        if tag:
            self.result += f"<a href=#{tag}>{title}</a>\n"
        else:
            self.result += f"{title}\n"
        if isinstance(description, str):
            self.result += f"{description}\n"
