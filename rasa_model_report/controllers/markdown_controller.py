import logging
import os.path
from typing import Any
from typing import Dict
from typing import List
from typing import Union

from rasa_model_report.controllers.output_controller import OutputController
from rasa_model_report.helpers import utils


class MarkdownController(OutputController):
    """
    Controller responsible for markdown files.
    """
    def __init__(
        self,
        rasa_path: str,
        output_path: str,
        project_name: str,
        rasa_version: str,
        project_version: str,
        **kwargs: Dict[str, Any]
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

        self.output_report_path: str = utils.remove_duplicate_slashs(f"{self.output_path}/model_report.md")

    def add_text(self, text: str) -> None:
        """
        Concatenates a text to the result text.

        :param text: Text that concatenates.
        """
        if isinstance(text, str):
            self.result += f"\n{text}"

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
            self.result += f"### {title}\n![{title}]({image_path} '{title}')\n"
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
        title = f"{'#'*heading_level} {title}"
        if tag:
            self.result += f"\n{title} <a name='{tag}'></a>\n"
        else:
            self.result += f"\n{title}\n"
        if isinstance(description, str):
            self.result += f"{description}\n"

    def build_summary(self) -> str:
        """
        Build the report model summary.

        :return: Report model summary.
        """
        sections = [
            " - [Overview](#overview)\n",
            " - [Intents](#intents)\n",
            " - [Entities](#entities)\n",
            " - [Core](#core)\n",
            " - [E2E Coverage](#e2e)\n"
        ]
        if os.path.isfile(self.config_report_path):
            sections.insert(1, " - [Config](#configs)\n")
        if self.nlu.is_connected():
            sections.insert(3, " - [NLU](#nlu)\n")

        return f"## Index\n{''.join(sections)}\n"

    def build_table(self, data: List[Union[str, float]]) -> str:
        """
        Build a table in markdown format.

        :param data: List representing the table data.
        :return: Table in markdown format.
        """
        header = "|" + "|".join(data[0]) + "|\n"
        header += "|-" * len(data[0]) + "|\n"
        content = ""
        for row in data[1:]:
            text_row = "|" + "|".join(row) + "|\n"
            content += text_row
        return header + content

    def build_overview(self) -> str:
        """
        Build the text block responsible for the summary of the report.

        :return: Overview report in markdown format.
        """
        overview = self.json.overview
        for item in ["intent", "entity", "core", "nlu"]:
            overview[item] = overview[item] if isinstance(overview.get(item), (float, int)) else "-"
        style = "style='font-size:16px'"
        data = [
            ["Bot name", self.project_name]
        ]
        if self.project_version:
            data.append(["Bot version", self.project_version])
        if self.rasa_version:
            data.append(["Rasa version", self.rasa_version])
        data.extend([
            ["Creation date", overview["created_at"]],
            ["Updated date", overview["updated_at"]]
        ])
        if self.model_link:
            data.append(["Model", f"[Download]({self.model_link})"])
        text = "|" + "|".join([item[0] for item in data]) + "|\n"
        text += "|" + "|".join([":-:" for i in range(len(data))]) + "|\n"
        text += "|" + "|".join([f"<span {style}>{item[1]}</span>" for item in data]) + "|\n\n"
        style = "style='font-size:20px'"
        text += f"|Intent|Entity|NLU|Core|E2E Coverage|<span {style}>General</span>|\n"
        text += "|:-:|:-:|:-:|:-:|:-:|:-:|\n"
        text += f"|{utils.change_scale(overview['intent'], 10, self.precision)}\
            |{utils.change_scale(overview['entity'], 10, self.precision)}\
            |{utils.change_scale(overview['nlu'], 10, self.precision)}\
            |{utils.change_scale(overview['core'], 10, self.precision)}\
            |{utils.change_scale(overview['e2e_coverage'], 10, self.precision)}\
            |<span {style}>**{utils.change_scale(overview['overall'], 10, self.precision)}**</span>|\n"
        text += f"{utils.get_color(overview['intent'])}\
            |{utils.get_color(overview['entity'])}\
            |{utils.get_color(overview['nlu'])}\
            |{utils.get_color(overview['core'])}\
            |{utils.get_color(overview['e2e_coverage'])}\
            |<span {style}>{utils.get_color(overview['overall'])}</span>|"
        return text

    def build_intent_overview(self) -> str:
        """
        Build the report intent overview block.

        :return: Overview block in markdown format.
        """
        intent_overview = self.json.intent_overview.get("macro avg")
        text = "|Precision|Recall|F1 Score|Examples|\n"
        text += "|:-:|:-:|:-:|:-:|\n"
        text += f"|{intent_overview['precision'] * 100:.1f}%\
            |{intent_overview['recall'] * 100:.1f}%\
            |{intent_overview['f1-score'] * 100:.1f}%\
            |{intent_overview['support']}|\n"
        text += f"|{utils.get_color(intent_overview['precision'])}\
            |{utils.get_color(intent_overview['recall'])}\
            |{utils.get_color(intent_overview['f1-score'])}\
            ||\n"
        return text

    def build_entity_overview(self) -> str:
        """
        Build the report entity overview block.

        :return: Overview block in markdown format.
        """
        entity_overview = self.json.entity_overview.get("macro avg")
        text = "|Precision|Recall|F1 Score|Examples|\n"
        text += "|:-:|:-:|:-:|:-:|\n"
        text += f"|{entity_overview['precision'] * 100:.1f}%\
            |{entity_overview['recall'] * 100:.1f}%\
            |{entity_overview['f1-score'] * 100:.1f}%\
            |{entity_overview['support']}|\n"
        text += f"|{utils.get_color(entity_overview['precision'])}\
            |{utils.get_color(entity_overview['recall'])}\
            |{utils.get_color(entity_overview['f1-score'])}\
            ||\n"
        return text

    def build_core_overview(self) -> str:
        """
        Build the report response and actions overview block.

        :return: Overview block in markdown format.
        """
        core_overview = self.json.core_overview.get("macro avg")
        text = "|Precision|Recall|F1 Score|Examples|\n"
        text += "|:-:|:-:|:-:|:-:|\n"
        text += f"|{core_overview['precision'] * 100:.1f}%\
            |{core_overview['recall'] * 100:.1f}%\
            |{core_overview['f1-score'] * 100:.1f}%\
            |{core_overview['support']}|\n"
        text += f"|{utils.get_color(core_overview['precision'])}\
            |{utils.get_color(core_overview['recall'])}\
            |{utils.get_color(core_overview['f1-score'])}\
            ||\n"
        return text

    def build_config_report(self) -> str:
        """
        Build the report config block.

        :return: Text block in markdown format.
        """
        if os.path.isfile(self.config_report_path):
            data = open(self.config_report_path, encoding="utf-8").read()
            logging.info(f"{self.config_report_path} file successfully loaded.")
            return f"```yaml\n{data}\n```"
        else:
            logging.warning("Configuration block will not be generated, as the file was not found.")
            return ""

    def build_e2e_coverage_list(self) -> str:
        """
        Build the report E2E coverage list block.

        :return: List block in markdown format.
        """
        text = ""
        data = self.e2e_coverage.data
        rate = self.e2e_coverage.total_rate
        total_num_elements = self.e2e_coverage.total_num_elements
        total_num_not_covered = self.e2e_coverage.total_num_not_covered
        if data:
            for element in data:
                text += f"#### {element.capitalize()}\n"
                if data[element]["items"]:
                    for item in data[element]["items"]:
                        text += f" - {item}\n"
                else:
                    text += " - (no elements not covered)\n"
                text += "\n"
            text += f"Total number of elements: {total_num_elements}\n\n"
            text += f"Total number of not covered elements: {total_num_not_covered}\n\n"
            text += f"Coverage rate: {rate * 100:.1f}% ({utils.get_color(rate)})\n\n"
        else:
            text = "\nThere are no end-to-end tests coverage.\n"
        return text
