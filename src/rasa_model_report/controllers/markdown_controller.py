import logging
import os.path

from src.rasa_model_report.controllers.controller import Controller
from src.rasa_model_report.controllers.csv_controller import CsvController
from src.rasa_model_report.controllers.json_controller import JsonController
from src.rasa_model_report.controllers.nlu_controller import NluController
from src.rasa_model_report.helpers.type_aliases import entity
from src.rasa_model_report.helpers.utils import change_scale
from src.rasa_model_report.helpers.utils import check
from src.rasa_model_report.helpers.utils import get_color


class MarkdownController(Controller):
    """
    Controller responsible for markdown files.
    """
    def __init__(self, rasa_path: str, output_path: str, project: str, version: str, **kwargs: dict) -> None:
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project: Project name.
        :param version: Project version.
        """
        super().__init__(rasa_path, output_path, project, version)

        self.result: str = ""
        self.title: str = "# Model health report"
        self.output_report_path: str = f"{self.output_path}/model_report.md".replace("//", "/")
        self.readme_path: str = "README.md"
        self.json: JsonController = JsonController(rasa_path, output_path, self.project, self.version)
        self.csv: CsvController = CsvController(rasa_path, output_path, self.project, self.version)
        self.nlu: NluController = NluController(
            rasa_path,
            output_path,
            self.project,
            self.version,
            url=kwargs.get("rasa_api_url"),
            disable_nlu=kwargs.get("disable_nlu")
        )

        self.json.update_overview({"nlu": self.nlu.general_grade})

    def add_text(self, text: str) -> None:
        """
        Concatenates a text to the result text.

        :param text: Text that concatenates.
        """
        if isinstance(text, str):
            self.result += "\n" + text

    def add_image(self, image: str, title: str) -> None:
        """
        Concatenates image (markdown format) into the result text.

        :param image: Image path.
        :param title: Image title.
        """
        if os.path.isfile(f"{self.results_path}/{image}"):
            self.result += f"### {title}\n![{title}]({self.results_path}/{image} '{title}')" + "\n"
            logging.info(f"Image {image} has been successfully added.")
        else:
            logging.warning(f"Image {image} was not found.")

    def break_line(self) -> None:
        """
        Inserts a line break to the result text.
        """
        self.result += "\n"

    def build_line_entity(self, entities: list[entity]) -> str:
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
        text += " - [Responses](#responses)\n"
        text += "\n"
        return text

    def build_table(self, data: list[str | float]) -> str:
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
        for item in ["intent", "entity", "response", "nlu"]:
            overview[item] = overview[item] if isinstance(overview.get(item), (float, int)) else 0
        text = "## Overview <a name='overview'></a>\n"
        style = "style='font-size:16px'"
        text += "|Bot|Version|Creation date|Updated date|\n"
        text += "|:-:|:-:|:-:|:-:|\n"
        text += f"|<span {style}>**{self.project}**</span>|\
            <span {style}>{self.version if self.version else 'not identified'}</span>|\
            <span {style}>{overview['created_at']}</span>|\
            <span {style}>{overview['updated_at']}</span>|\n\n"
        style = "style='font-size:20px'"
        text += f"|Intent|Entity|NLU|Response|<span {style}>General</span>|\n"
        text += "|:-:|:-:|:-:|:-:|:-:|\n"
        text += f"|{change_scale(overview['intent'], 10)}\
            |{change_scale(overview['entity'], 10)}\
            |{change_scale(overview['nlu'], 10)}\
            |{change_scale(overview['response'], 10)}\
            |<span {style}>**{change_scale(overview['overall'], 10)}**</span>|\n"
        text += f"{get_color(overview['intent'])}\
            |{get_color(overview['entity'])}\
            |{get_color(overview['nlu'])}\
            |{get_color(overview['response'])}\
            |<span {style}>{get_color(overview['overall'])}</span>|"
        return text

    def build_intent_title(self) -> str:
        """
        Build the report intent title block.

        :return: Title block in markdown format.
        """
        title = "## Intents <a name='intents'></a>\n"
        description = "Section that discusses metrics on model intents.\n"
        return title + description

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
        text += f"|{get_color(intent_overview['precision'])}\
            |{get_color(intent_overview['recall'])}\
            |{get_color(intent_overview['f1-score'])}\
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

    def build_entity_title(self) -> str:
        """
        Build the report entity title block.

        :return: Title block in markdown format.
        """
        title = "## Entities <a name='entities'></a>\n"
        description = "Section that discusses metrics about the model entities.\n"
        return title + description

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
        text += f"|{get_color(entity_overview['precision'])}\
            |{get_color(entity_overview['recall'])}\
            |{get_color(entity_overview['f1-score'])}\
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

    def build_response_title(self) -> str:
        """
        Build the report response title block.

        :return: Title block in markdown format.
        """
        title = "## Responses <a name='responses'></a>\n"
        description = "Section that discusses metrics about bot responses and stories.\n"
        return title + description

    def build_response_overview(self) -> str:
        """
        Build the report response overview block.

        :return: Overview block in markdown format.
        """
        response_overview = self.json.response_overview.get("macro avg")
        text = "|Precision|Recall|F1 Score|Examples|\n"
        text += "|:-:|:-:|:-:|:-:|\n"
        text += f"|{response_overview['precision'] * 100:.1f}%\
            |{response_overview['recall'] * 100:.1f}%\
            |{response_overview['f1-score'] * 100:.1f}%\
            |{response_overview['support']}|\n"
        text += f"|{get_color(response_overview['precision'])}\
            |{get_color(response_overview['recall'])}\
            |{get_color(response_overview['f1-score'])}\
            ||\n"
        return text

    def build_response_table(self) -> str:
        """
        Função que monta o bloco de texto das histórias no relatório.
        """
        title = "### Metrics\n"
        description = "Table with bot response metrics.\n"
        title += description + "\n"
        data = self.json.responses
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
            text = "\nNo responses were found for this model.\n"
            return title + text

    def build_nlu_title(self) -> str:
        """
        Build the report NLU title block.

        :return: Title block in markdown format.
        """
        title = "## NLU <a name='nlu'></a>\n"
        description = "Section that discusses metrics about NLU and its example phrases.\n"
        return title + description

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
            color = get_color(item["confidence"])
            new_item["confidence"] = f"{item['confidence'] * 100:.1f}%"
            new_item["understood"] = check(not item["understood"])
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
            color = get_color(item["confidence"])
            new_item["confidence"] = f"{item['confidence'] * 100:.1f}%"
            new_item["understood"] = check(not item["understood"])
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
            title = "## Configs <a name='configs'></a>\n"
            description = "Settings that were used in the training *pipeline* and *policies*.\n"
            title += description
            data = open(self.config_report_path, encoding="utf-8").read()
            logging.info(f"{self.config_report_path} file successfully loaded.")
            return f"{title}```yaml\n{data}\n```"
        else:
            logging.warning("Configuration block will not be generated, as the file was not found.")
            return ""

    def build_credits(self) -> str:
        """
        Build the report credits block.

        :return str: Text block in markdown format.
        """
        repository_url = "https://github.com/brunohjs/rasa-model-report"
        text = "##### Generated by rasa-model-report, collaborative open-source project for Rasa projects. "
        text += f"Github repository at this [link]({repository_url})."
        return text

    def _build_line_table(self, data: dict[str, str | float | dict]) -> list[str]:
        """
        Returns list representing a line table in markdown format.

        :param data: Data object to be converted.
        :return: Line table.
        """
        return [
            get_color(data["f1-score"]),
            data["name"],
            f"{data['precision'] * 100:.1f}%",
            f"{data['recall'] * 100:.1f}%",
            f"{data['f1-score'] * 100:.1f}%",
            str(data['support'])
        ]

    def save_report(self) -> None:
        """
        Save the report data to file.
        """
        if os.path.isfile(self.output_report_path):
            text = f"{self.output_report_path} file successfully changed."
        else:
            text = f"{self.output_report_path} file successfully created."
        file = open(self.output_report_path, "w", encoding="utf-8")
        file.write(self.result)
        file.close()
        logging.info(text)

    def save_overview(self) -> None:
        """
        Save the overview report to JSON file.
        """
        self.json.save_overview()
