import logging
import os.path
from typing import Dict
from typing import List
from typing import Union

from rasa_model_report.controllers.controller import Controller
from rasa_model_report.controllers.csv_controller import CsvController
from rasa_model_report.controllers.e2e_coverage_controller import E2ECoverageController
from rasa_model_report.controllers.json_controller import JsonController
from rasa_model_report.controllers.nlu_controller import NluController
from rasa_model_report.helpers import constants
from rasa_model_report.helpers import type_aliases
from rasa_model_report.helpers import utils


class OutputController(Controller):
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
        super().__init__(rasa_path, output_path, project_name, project_version, **kwargs)

        self.result: str = ""
        self.format: str = kwargs.get("output_format", constants.OUTPUT_FORMAT)
        self.title: str = "Model health report"
        self.output_report_path: str = utils.remove_duplicate_slashs(f"{self.output_path}/model_report.html")
        self.readme_path: str = "README.md"
        self.rasa_version: str = rasa_version
        self.model_link: str = kwargs.get("model_link")
        self.no_images: bool = kwargs.get("no_images", constants.NO_IMAGES)
        self.precision: int = kwargs.get("precision", constants.GRADE_PRECISION)
        self.json: JsonController = JsonController(rasa_path, output_path, project_name, project_version)
        self.csv: CsvController = CsvController(rasa_path, output_path, project_name, project_version)
        self.nlu: NluController = NluController(
            rasa_path,
            output_path,
            project_name,
            project_version,
            url=kwargs.get("rasa_api_url", constants.RASA_API_URL),
            disable_nlu=kwargs.get("disable_nlu", constants.DISABLE_NLU)
        )
        self.e2e_coverage: E2ECoverageController = E2ECoverageController(
            rasa_path,
            output_path,
            kwargs.get("actions_path"),
            project_name,
            project_version
        )

        self.json.update_overview({
            "nlu": self.nlu.general_grade,
            "e2e_coverage": self.e2e_coverage.total_rate
        })
        logging.info(f"Model output format: {self.format}")
        if self.no_images:
            logging.info("--no-images activated. Images will not be displayed in the report.")

    def add_text(self, text: str) -> None:
        """
        Concatenates a text to the result text.

        :param text: Text that concatenates.
        """
        raise utils.not_implemented()

    def add_image(self, image_filename: str, title: str) -> None:
        """
        Concatenates image (markdown format) into the result text.

        :param image_filename: Image file name.
        :param title: Image title.
        """
        raise utils.not_implemented()

    def add_title(self, title, description=None, heading_level=2, tag=None):
        """
        Concatenates a title and description to the result text.

        :param title: Title text.
        :param description: Description text (default: None).
        :param int heading_level: Heading level (default: 2).
        :param tag: Tag for an anchor link (default: None).
        """
        raise utils.not_implemented()

    def add_credits(self) -> str:
        """
        Build the report credits block.

        :return str: Text block in markdown format.
        """
        self.result += f"<h6>Generated by rasa-model-report v{self.version}, collaborative open-source project for " \
            "Rasa projects. Github repository at this " \
            "<a href='https://github.com/brunohjs/rasa-model-report'>link</a>.</h6>"

    def build_summary(self):
        """
        Build the report model summary.

        :return: Report model summary.
        """
        return utils.not_implemented()

    def build_overview(self) -> str:
        """
        Build the text block responsible for the summary of the report.

        :return: Overview report in markdown format.
        """
        return utils.not_implemented()

    def build_intent_table(self) -> str:
        """
        Build the report intent table block.

        :return: Table block in markdown format.
        """
        data = self.json.intents
        table_data = [[
            "",
            "Intent",
            "Precision",
            "Recall",
            "F1 Score",
            "Examples"
        ]]
        for item in data:
            table_data.append(self._table_line(item))
        if len(table_data) > 1:
            self.csv.save(table_data, "intent_report.csv")
            return self.build_table(table_data)
        else:
            text = "\nNo intentions were found in this model.\n"
            return text

    def build_intent_errors_table(self) -> str:
        """
        Build the report intent errors table block.

        :return: Table block in markdown format.
        """
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
            return self.build_table(table_data)
        else:
            text = "\nNo confusions or errors of intent were found in this model.\n"
            return text

    def build_entity_overview(self) -> str:
        """
        Build the report entity overview block.

        :return: Overview block in markdown format.
        """
        return utils.not_implemented()

    def build_entity_table(self) -> str:
        """
        Build the report entity table block.

        :return: Table block in markdown format.
        """
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
            table_data.append(self._table_line(item))
        if len(table_data) > 1:
            self.csv.save(table_data, "DIETClassifier_report.csv")
            return self.build_table(table_data)
        else:
            text = "\nNo entities were found in this model.\n"
            return text

    def build_entity_errors_table(self) -> str:
        """
        Build the report entity errors table block.

        :return: Table block in markdown format.
        """
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
            return table_data
        else:
            text = "\nNo confusions of entities were found in this model.\n"
            return text

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

    def build_core_overview(self) -> str:
        """
        Build the report response and actions overview block.

        :return: Overview block in markdown format.
        """
        return utils.not_implemented()

    def build_core_table(self) -> str:
        """
        Build the report core table block.
        """
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
            table_data.append(self._table_line(item))
        if len(table_data) > 1:
            self.csv.save(table_data, "story_report.csv")
            return self.build_table(table_data)
        else:
            text = "\nNo responses or actions were found for this model.\n"
            return text

    def build_nlu_table(self) -> str:
        """
        Build the report NLU table block.

        :return: Table block in markdown format.
        """
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
            color = utils.get_color(item["confidence"], output_format=self.format)
            new_item["confidence"] = f"{item['confidence'] * 100:.1f}%"
            new_item["understood"] = utils.check(not item["understood"])
            table_data.append([color] + list(new_item.values()))
        if len(table_data) > 1:
            self.csv.save(table_data, "nlu_report.csv")
            return self.build_table(table_data)
        else:
            text = "\nNo example sentences were found in this template.\n"
            return text

    def build_nlu_errors_table(self) -> str:
        """
        Build the report NLU errors table block.

        :return: Table block in markdown format.
        """
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
            color = utils.get_color(item["confidence"], output_format=self.format)
            new_item["confidence"] = f"{item['confidence'] * 100:.1f}%"
            new_item["understood"] = utils.check(not item["understood"])
            table_data.append([color] + list(new_item.values()))
        if len(table_data) > 1:
            self.csv.save(table_data, "nlu_report.csv")
            return self.build_table(table_data)
        else:
            text = "\nThere are no sentences that were not understood in this model.\n"
            return text

    def build_config_report(self) -> str:
        """
        Build the report config block.

        :return: Text block in markdown format.
        """
        return utils.not_implemented()

    def build_e2e_coverage_list(self) -> str:
        """
        Build the report E2E coverage list block.

        :return: List block in markdown format.
        """
        return utils.not_implemented()

    def _table_line(self, data: Dict[str, Union[str, float, dict]]) -> List[str]:
        """
        Returns list representing a line table in markdown format.

        :param data: Data object to be converted.
        :return: Line table.
        """
        return [
            utils.get_color(data["f1-score"], output_format=self.format),
            data["name"],
            f"{data['precision'] * 100:.1f}%",
            f"{data['recall'] * 100:.1f}%",
            f"{data['f1-score'] * 100:.1f}%",
            str(data['support'])
        ]

    def build_table(self, data: List[Union[str, float]]) -> str:
        """
        Build a table in markdown format.

        :param data: List representing the table data.
        :return: Table in markdown format.
        """
        return utils.not_implemented()

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

    def generate_report(self) -> None:
        """
        Function that generates the report.
        """
        if os.path.isdir(self.results_path):
            # Overview
            self.add_title(self.title, heading_level=1)
            self.add_title(
                "Index"
            )
            self.add_text(self.build_summary())
            self.add_title(
                "Overview"
            )
            self.add_text(self.build_overview())

            # Config
            if os.path.isfile(self.config_report_path):
                self.add_title(
                    "Configs",
                    "Settings that were used in the training pipeline and policies.",
                    tag="configs"
                )
                self.add_text(self.build_config_report())

            # Intents
            self.add_title(
                "Intents",
                "Section that discusses metrics on model intents.",
                tag="intents"
            )
            self.add_title(
                "Metrics",
                "Table with the metrics of intentions.",
                heading_level=3
            )
            self.add_text(self.build_intent_table())
            self.add_title(
                "Confused intentions",
                "Where all the confusing or wrong sentences of the model are listed.",
                heading_level=3
            )
            self.add_text(self.build_intent_errors_table())
            self.add_image(self.images["INTENT_HISTOGRAM"], "Histogram")
            self.add_image(self.images["INTENT_MATRIX"], "Confusion Matrix")

            # Entities
            self.add_title(
                "Entities",
                "Section that discusses metrics about the model entities.",
                tag="entities"
            )
            self.add_title(
                "Metrics",
                "Table with entity metrics.",
                heading_level=3
            )
            self.add_text(self.build_entity_table())
            self.add_title(
                "Confused entities",
                "Where all the confusing or wrong entities of the model are listed.",
                heading_level=3
            )
            self.add_text(self.build_entity_errors_table())
            self.add_image(self.images['ENTITY_HISTOGRAM'], "Histogram")
            self.add_image(self.images['ENTITY_MATRIX'], "Confusion Matrix")

            # NLU
            if self.nlu.is_connected():
                self.add_title(
                    "NLU",
                    "Section that discusses metrics about NLU and its example phrases.",
                    tag="nlu"
                )
                self.add_title(
                    "Sentences",
                    "Table with metrics for bot training phrases.",
                    heading_level=3
                )
                self.add_text(self.build_nlu_table())
                self.add_title(
                    "Sentences with problems",
                    "Table with the sentences that were not understood correctly by the model.",
                    heading_level=3
                )
                self.add_text(self.build_nlu_errors_table())

            # Core
            self.add_title(
                "Core",
                "Section that discusses metrics about bot responses and actions.",
                tag="core"
            )
            self.add_title(
                "Metrics",
                "Table with bot core metrics.",
                heading_level=3
            )
            self.add_text(self.build_core_table())
            self.add_image(self.images['STORY_MATRIX'], "Confusion Matrix")

            # E2E Coverage
            self.add_title(
                "E2E Coverage",
                "Section that shows data from intents, entities and responses that aren't covered by end-to-end tests.",
                tag="e2e"
            )
            self.add_title(
                "Not covered elements",
                "List with not covered elements by end-to-end tests.",
                heading_level=3
            )
            self.add_text(self.build_e2e_coverage_list())

            # Credits
            self.add_credits()

            if self.format == "pdf":
                self.input_css()

            # Save report and overview files
            self.save_report()
            self.save_overview()

            logging.info("Script successfully completed.")
        else:
            logging.error(f"{self.results_path} directory doesn't exist.")
            logging.error(
                "To inform the directory where the Rasa project files are located, use the --path parameter."
            )
            logging.error("Script finished with errors.")
