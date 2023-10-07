import logging
import os.path
from importlib.resources import files
from typing import Dict
from typing import List
from typing import Union

from airium import Airium
from weasyprint import HTML

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

        self.result: Airium = Airium(
            base_indent="\t"
        )
        self.format: str = kwargs.get("output_format", constants.OUTPUT_FORMAT)
        self.title: str = "Model health report"
        self.output_html_report_path: str = utils.remove_duplicate_slashs(f"{self.output_path}/model_report.html")
        self.output_pdf_report_path: str = utils.remove_duplicate_slashs(f"{self.output_path}/model_report.pdf")
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
        if isinstance(text, str):
            self.result(text)

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
            with self.result.h3():
                self.result(title)
            self.result.img(src=image_path, alt=title)
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
        with getattr(self.result, f'h{heading_level}')(id=tag) if tag else getattr(self.result, f'h{heading_level}')():
            self.result(title)
        if heading_level <= 2:
            self.result.hr()
        if description:
            self.result(description)

    def add_credits(self) -> str:
        """
        Build the report credits block.

        :return str: Text block in markdown format.
        """
        with self.result.div(klass="credits"):
            self.result("Generated by ")
            with self.result.b():
                self.result(f"rasa-model-report v{self.version}")
            self.result(", collaborative open-source project for Rasa projects. Github repository at this ")
            with self.result.a(href="https://github.com/brunohjs/rasa-model-report"):
                self.result("link")
            self.result(".")

    def add_css(self):
        """
        Input CSS style code on HTML output result.
        """
        data = files("rasa_model_report.assets.css").joinpath("pdf.css").read_text()
        self.result.style(_t=data)

    def build_summary(self):
        """
        Build the report model summary.

        :return: Report model summary.
        """
        sections = [
            "Overview",
            "Configs",
            "Intents",
            "Entities",
            "Core",
            "NLU",
            "E2E Coverage"
        ]
        if not os.path.isfile(self.config_report_path):
            sections.remove("Configs")
        if not self.nlu.is_connected():
            sections.remove("NLU")
        with self.result.ul():
            for section in sections:
                if section == "E2E Coverage":
                    with self.result.li(), self.result.a(href="#e2e"):
                        self.result(section)
                else:
                    with self.result.li(), self.result.a(href=f"#{section.lower()}"):
                        self.result(section)

    def build_overview(self):
        """
        Build the text block responsible for the summary of the report.

        :return: Overview report in markdown format.
        """
        overview = self.json.overview
        for item in ["intent", "entity", "core", "nlu"]:
            overview[item] = overview[item] if isinstance(overview.get(item), (float, int)) else "-"
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
            data.append(["Model", self.model_link])

        with self.result.table(klass="info"):
            with self.result.tr():
                for item in data:
                    self.result.th(_t=item[0])
            with self.result.tr():
                for item in data:
                    self.result.td(_t=item[1])

        items = ["Intents", "Entity", "NLU", "Core", "E2E Coverage", "General"]
        with self.result.table():
            with self.result.tr():
                for item in items:
                    self.result.th(_t=item)

            items = ["intent", "entity", "nlu", "core", "e2e_coverage", "overall"]
            with self.result.tr():
                for item in items:
                    self.result.td(_t=utils.change_scale(overview[item], 10, self.precision), klass=item)
            with self.result.tr():
                for item in items:
                    self.result.td(_t=utils.get_color(overview[item], output_format="pdf"), klass=item)

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
            return self.build_table(table_data, klass="data-table")
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
            return self.build_table(table_data, klass="error-data-table")
        else:
            text = "\nNo confusions or errors of intent were found in this model.\n"
            return text

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
            return self.build_table(table_data, klass="data-table")
        else:
            text = "\nNo entities were found in this model.\n"
            return text

    def build_entity_errors_table(self) -> str:
        """
        Build the report entity errors table block.

        :return: Table block in markdown format.
        """
        data = self.json.entity_errors
        if data:
            with self.result.table():
                with self.result.tr():
                    for item in ["Text", "Entity", "Predicted entities"]:
                        self.result.th(_t=item)
                for row in data:
                    with self.result.tr():
                        self.result.td(_t=row["text"])
                        with self.result.td():
                            self.build_line_entity(row["entities"])
                        with self.result.td():
                            self.build_line_entity(row["predicted_entities"])
        else:
            self.result.p(_t="No confusions of entities were found in this model.")

    def build_line_entity(self, entities: List[type_aliases.entity]) -> str:
        """
        Create a entity lines table in markdown format.

        :param entities: List of entities.
        :return: entity lines table in markdown format.
        """
        if not entities:
            self.result("-")
        else:
            for entity in entities:
                with self.result.details():
                    with self.result.summary():
                        self.result(entity['entity'])
                    with self.result.pre():
                        self.result(f"start: {entity['start']}")
                        self.result.br()
                        self.result(f"end: {entity['end']}")
                        self.result.br()
                        self.result(f"value: {entity['value']}")

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
            return self.build_table(table_data, klass="data-table")
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
            return self.build_table(table_data, klass="data-table")
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
            return self.build_table(table_data, klass="error-data-table")
        else:
            text = "\nThere are no sentences that were not understood in this model.\n"
            return text

    def build_config_report(self):
        """
        Build the report config block.

        :return: Text block in markdown format.
        """
        if os.path.isfile(self.config_report_path):
            data = open(self.config_report_path, encoding="utf-8").read()
            data = data.replace("\n", "<br>")
            logging.info(f"{self.config_report_path} file successfully loaded.")
            self.result.br()
            self.result.code(_t=data)
        else:
            logging.warning("Configuration block will not be generated, as the file was not found.")

    def build_e2e_coverage_list(self) -> str:
        """
        Build the report E2E coverage list block.

        :return: List block in markdown format.
        """
        data = self.e2e_coverage.data
        rate = self.e2e_coverage.total_rate
        total_num_elements = self.e2e_coverage.total_num_elements
        total_num_not_covered = self.e2e_coverage.total_num_not_covered
        if data:
            for element in data:
                self.result.h4(_t=element.capitalize())
                with self.result.ul():
                    if data[element]["items"]:
                        for item in data[element]["items"]:
                            self.result.li(_t=item)
                    else:
                        self.result.li(_t="(no elements not covered)")
            self.result.p(_t=f"Total number of elements: {total_num_elements}")
            self.result.p(_t=f"Total number of not covered elements: {total_num_not_covered}")
            self.result.p(_t=f"Coverage rate: {rate * 100:.1f}% ({utils.get_color(rate, output_format='pdf')})")
        else:
            self.result.p(_t="There are no end-to-end tests coverage.")

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

    def build_table(self, data: List[Union[str, float]], klass="") -> str:
        """
        Build a table in markdown format.

        :param data: List representing the table data.
        :return: Table in markdown format.
        """
        with self.result.table(klass=klass):
            with self.result.tr():
                for row in data[0]:
                    self.result.th(_t=row)
            for row in data[1:]:
                with self.result.tr():
                    for text in row:
                        self.result.td(_t=text)

    def convert_to_pdf(self):
        if os.path.isfile(self.output_pdf_report_path):
            text = f"{self.output_pdf_report_path} file successfully changed."
        else:
            text = f"{self.output_pdf_report_path} file successfully created."
        HTML(self.output_html_report_path).write_pdf(self.output_pdf_report_path)
        logging.info(text)

    def save_report(self) -> None:
        """
        Save the report data to file.
        """
        if os.path.isfile(self.output_html_report_path):
            text = f"{self.output_html_report_path} file successfully changed."
        else:
            text = f"{self.output_html_report_path} file successfully created."
        file = open(self.output_html_report_path, "w", encoding="utf-8")
        file.write(str(self.result))
        file.close()
        self.convert_to_pdf()
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
            with self.result.html():
                with self.result.head():
                    self.result.link(
                        rel="stylesheet",
                        href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
                    )
                with self.result.body(klass="container"):
                    self.add_css()
                    self.add_title(self.title, heading_level=1)

                    # Index
                    self.add_title(
                        "Index"
                    )
                    self.build_summary()

                    # Overview
                    self.add_title(
                        "Overview"
                    )
                    self.build_overview()

                    # Config
                    if os.path.isfile(self.config_report_path):
                        self.add_title(
                            "Configs",
                            "Settings that were used in the training pipeline and policies.",
                            tag="configs"
                        )
                        self.build_config_report()

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
                    self.build_intent_table()
                    self.add_title(
                        "Confused intentions",
                        "Where all the confusing or wrong sentences of the model are listed.",
                        heading_level=3
                    )
                    self.build_intent_errors_table()
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
                    self.build_entity_table()
                    self.add_title(
                        "Confused entities",
                        "Where all the confusing or wrong entities of the model are listed.",
                        heading_level=3
                    )
                    self.build_entity_errors_table()
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
                        self.build_nlu_table()
                        self.add_title(
                            "Sentences with problems",
                            "Table with the sentences that were not understood correctly by the model.",
                            heading_level=3
                        )
                        self.build_nlu_errors_table()

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
                    self.build_core_table()
                    self.add_image(self.images['STORY_MATRIX'], "Confusion Matrix")

                    # E2E Coverage
                    self.add_title(
                        "E2E Coverage",
                        "Section that shows data from intents, entities and responses that aren't covered by "
                        "end-to-end tests.",
                        tag="e2e"
                    )
                    self.add_title(
                        "Not covered elements",
                        "List with not covered elements by end-to-end tests.",
                        heading_level=3
                    )
                    self.build_e2e_coverage_list()

                    # Credits
                    self.add_credits()

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
