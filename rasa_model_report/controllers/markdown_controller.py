import logging
import os.path
from typing import Any
from typing import Dict
from typing import List
from typing import Union

from rasa_model_report.controllers.output_controller import OutputController
from rasa_model_report.helpers import type_aliases
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

    def build_line_entity(self, entities: List[type_aliases.entity]) -> str:
        """
        Create a entity lines table in markdown format.

        :param entities: List of entities.
        :return: entity lines table in markdown format.
        """
        if not entities:
            return "-"
        return "\n\t\t\t\t\t\t\t".join([f"""<details>
                            <summary>{entity['entity']}</summary>
                            <pre>start: {entity['start']}
                            <br>end: {entity['end']}
                            <br>value: {entity['value']}
                            </pre>
                        </details>""" for entity in entities])

    def build_summary(self) -> str:
        """
        Build the report model summary.

        :return: Report model summary.
        """
        text = "## Index\n"
        text += " - [Overview](#overview)\n"
        if os.path.isfile(self.config_report_path):
            text += " - [Config](#configs)\n"
        text += " - [Intents](#intents)\n"
        text += " - [Entities](#entities)\n"
        if self.nlu.is_connected():
            text += " - [NLU](#nlu)\n"
        text += " - [Core](#core)\n"
        text += " - [E2E Coverage](#e2e)\n"
        text += "\n"
        return text

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
        text = "## Overview <a name='overview'></a>\n"
        style = "style='font-size:16px'"
        data = [
            ["Bot Name", self.project_name]
        ]
        if self.project_version:
            data.append(["Bot Version", self.project_version])
        if self.rasa_version:
            data.append(["Rasa Version", self.rasa_version])
        data.extend([
            ["Creation date", overview["created_at"]],
            ["Updated date", overview["updated_at"]]
        ])
        if self.model_link:
            data.append(["Model", f"[Download]({self.model_link})"])
        text += "|" + "|".join([item[0] for item in data]) + "|\n"
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

    def build_intent_table(self) -> str:
        """
        Build the report intent table block.

        :return: Table block in markdown format.
        """
        title = "### Metrics\n"
        description = "Table with the metrics of intentions.\n"
        title += description
        data = self.json.intents
        table_data = [[
            "",
            "intent",
            "Precision",
            "Recall",
            "F1 Score",
            "Examples"
        ]]
        for item in data:
            table_data.append(self._build_line_table(item))
        if len(table_data) > 1:
            self.csv.save(table_data, "intent_report.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNo intentions were found in this model.\n"
            return title + text

    def build_intent_errors_table(self) -> str:
        """
        Build the report intent errors table block.

        :return: Table block in markdown format.
        """
        title = "### Confused intentions\n"
        description = "Where all the confusing or wrong sentences of the model are listed.\n"
        title += description
        data = self.json.intent_errors
        table_data = [[
            "Text",
            "Intent",
            "Predicted Intent",
            "Confidence"
        ]]
        for row in data:
            if row["intent_prediction"]["confidence"] >= 0.001:
                confidence = f"{row['intent_prediction']['confidence'] * 100:.1f}%"
                table_data.append([
                    row["text"],
                    row["intent"],
                    row["intent_prediction"]["name"],
                    confidence
                ])
        if len(table_data) > 1:
            self.csv.save(table_data, "intent_errors.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNo confusions or errors of intent were found in this model.\n"
            return title + text

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

    def build_entity_table(self) -> str:
        """
        Build the report entity table block.

        :return: Table block in markdown format.
        """
        title = "### Metrics\n"
        description = "Table with entity metrics.\n"
        title += description + "\n"
        data = self.json.entities
        table_data = [[
            "",
            "Entity",
            "Precision",
            "Recall",
            "F1 Score",
            "Examples"
        ]]
        for item in data:
            table_data.append(self._build_line_table(item))
        if len(table_data) > 1:
            self.csv.save(table_data, "DIETClassifier_report.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNo entities were found in this model.\n"
            return title + text

    def build_entity_errors_table(self) -> str:
        """
        Build the report entity errors table block.

        :return: Table block in markdown format.
        """
        title = "### Confused entities\n"
        description = "Where all the confusing or wrong entities of the model are listed.\n"
        title += description
        data = self.json.entity_errors
        table_data = """<table>
            <thead>
                <tr>
                    <th>Text</th>
                    <th>Entity</th>
                    <th>Predicted entities</th>
                </tr>
            </thead>
            <tbody>"""
        for row in data:
            table_data += f"""
                <tr>
                    <td>{row['text']}</td>
                    <td>
                        {self.build_line_entity(row['entities'])}
                    </td>
                    <td>
                        {self.build_line_entity(row['predicted_entities'])}
                    </td>
                </tr>"""
        table_data += """
            </tbody>
        </table>\n\n"""
        if data:
            return title + table_data
        else:
            text = "\nNo confusions of entities were found in this model.\n"
            return title + text

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

    def build_core_table(self) -> str:
        """
        Build the report core table block.
        """
        title = "### Metrics\n"
        description = "Table with bot core metrics.\n"
        title += description + "\n"
        data = self.json.core
        table_data = [[
            "",
            "Response",
            "Precision",
            "Recall",
            "F1 Score",
            "Number of occurrences"
        ]]
        for item in data:
            if item["name"].startswith("[") or not \
                    (item["name"].startswith("utter_") or item["name"].startswith("action_")):
                continue
            table_data.append(self._build_line_table(item))
        if len(table_data) > 1:
            self.csv.save(table_data, "story_report.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNo responses or actions were found for this model.\n"
            return title + text

    def build_nlu_table(self) -> str:
        """
        Build the report NLU table block.

        :return: Table block in markdown format.
        """
        title = "### Sentences\n"
        description = "Table with metrics for bot training phrases.\n"
        title += description + "\n"
        data = self.nlu.data
        table_data = [[
            "",
            "Text",
            "Intent",
            "Predicted intent",
            "Confidence",
            "Understood"
        ]]
        for item in data:
            new_item = {
                "text": item["text"],
                "intent": item["intent"],
                "predicted_intent": item["predicted_intent"],
            }
            color = utils.get_color(item["confidence"])
            new_item["confidence"] = f"{item['confidence'] * 100:.1f}%"
            new_item["understood"] = utils.check(not item["understood"])
            table_data.append([color] + list(new_item.values()))
        if len(table_data) > 1:
            self.csv.save(table_data, "nlu_report.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNo example sentences were found in this template.\n"
            return title + text

    def build_nlu_errors_table(self) -> str:
        """
        Build the report NLU errors table block.

        :return: Table block in markdown format.
        """
        title = "### Sentences with problems\n"
        description = "Table with the sentences that were not understood correctly by the model.\n"
        title += description + "\n"
        data = self.nlu.problem_sentences
        table_data = [[
            "",
            "Text",
            "Intent",
            "Predicted intent",
            "Confidence",
            "Understood"
        ]]
        for item in data:
            new_item = {
                "text": item["text"],
                "intent": item["intent"],
                "predicted_intent": item["predicted_intent"],
            }
            color = utils.get_color(item["confidence"])
            new_item["confidence"] = f"{item['confidence'] * 100:.1f}%"
            new_item["understood"] = utils.check(not item["understood"])
            table_data.append([color] + list(new_item.values()))
        if len(table_data) > 1:
            self.csv.save(table_data, "nlu_report.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nThere are no sentences that were not understood in this model.\n"
            return title + text

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
        title = "### Not covered elements\n"
        description = "List with not covered elements by end-to-end tests.\n"
        title += description + "\n"
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
        return title + text

    def _build_line_table(self, data: Dict[str, Union[str, float, dict]]) -> List[str]:
        """
        Returns list representing a line table in markdown format.

        :param data: Data object to be converted.
        :return: Line table.
        """
        return [
            utils.get_color(data["f1-score"]),
            data["name"],
            f"{data['precision'] * 100:.1f}%",
            f"{data['recall'] * 100:.1f}%",
            f"{data['f1-score'] * 100:.1f}%",
            str(data['support'])
        ]
