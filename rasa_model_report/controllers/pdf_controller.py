import logging
import os.path
from typing import List
from typing import Union

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
            self.result += f"<h3>{title}</h3>\n<img alt='{title}' src='{image_path}'>\n"
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
        title_component = f"\n<h{heading_level}>{title}</h{heading_level}>\n"
        if tag:
            title_component = f"\n<h{heading_level} id='{tag}'>{title}</h{heading_level}>\n"
        self.result += title_component
        if isinstance(description, str):
            self.result += f"{description}\n"

    def build_table(self, data: List[Union[str, float]]) -> str:
        """
        Build a table in markdown format.

        :param data: List representing the table data.
        :return: Table in markdown format.
        """
        content = "<table>\n"
        content += " <tr>\n"
        for row in data[0]:
            content += f"   <th>{row}</th>\n"
        content += " </tr>\n"
        for row in data[1:]:
            content += " <tr>\n"
            for text in row:
                content += f"  <td>{text}</td>\n"
            content += " </tr>\n"
        content += "</table>\n"
        return content

    def build_summary(self):
        """
        Build the report model summary.

        :return: Report model summary.
        """
        text = "<ul>\n"
        text += " <li><a href=#overview>Overview</a></li>\n"
        if os.path.isfile(self.config_report_path):
            text += " <li><a href=#configs>Config</a></li>\n"
        text += " <li><a href=#intents>Intents</a></li>\n"
        text += " <li><a href=#entities>Entities</a></li>\n"
        if self.nlu.is_connected():
            text += " <li><a href=#nlu>NLU</a></li>\n"
        text += " <li><a href=#core>Core</a></li>\n"
        text += " <li><a href=#e2e>E2E Coverage</a></li>\n"
        text += "</ul>\n"
        text += "\n"
        return text

    def build_overview(self):
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
        items = ["intent", "entity", "nlu", "core", "e2e_coverage"]
        text = "<table>\n"
        text += " <tr>\n"
        text += "".join([f"  <th>{item[0]}</th>\n" for item in data])
        text += " </tr>\n"
        text += " <tr>\n"
        text += "".join([f"  <td>{item[1]}</td>\n" for item in data])
        text += " </tr>\n"
        text += "</table>\n\n"
        text += "<table>\n"
        text += " <tr>\n"
        text += "  <th>Intent</th>\n"
        text += "  <th>Entity</th>\n"
        text += "  <th>NLU</th>\n"
        text += "  <th>Core</th>\n"
        text += "  <th>E2E Coverage</th>\n"
        text += f"  <th {style}>General</th>\n"
        text += " </tr>\n"
        text += " <tr>\n"
        for item in items:
            text += f"  <td>{utils.change_scale(overview[item], 10, self.precision)}</td>\n"
        text += f"  <td {style}><b>{utils.change_scale(overview['overall'], 10, self.precision)}</b></td>\n"
        text += " </tr>\n"
        text += " <tr>\n"
        for item in items:
            text += f"  <td>{utils.get_color(overview[item], output_format='pdf')}</td>\n"
        text += f"  <td {style}>{utils.get_color(overview['overall'], output_format='pdf')}</td>\n"
        text += " </tr>\n"
        text += "</table>\n\n"
        return text

    def input_css(self):
        """
        Input CSS style code on HTML output result.
        """
        file = open("assets/css/pdf.css")
        data = file.read()
        file.close()
        self.result = f"<style>\n{data}\n</style>\n{self.result}"

    def convert_to_pdf(self):
        import pdfkit
        pdfkit.from_file('model_report.html', 'model_report.pdf', options={
            "encoding": "UTF-8"
        })

    def convert_to_pdf2(self):
        from xhtml2pdf import pisa
        # open output file for writing (truncated binary)
        result_file = open("model_report.pdf", "w+b")

        # convert HTML to PDF
        pisa.CreatePDF(
            self.result,                # the HTML to convert
            dest=result_file,
            encoding="UTF-8",
            default_css="assets/css/pdf.css"
        )           # file handle to recieve result

        # close output file
        result_file.close()

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
        self.convert_to_pdf()
        logging.info(text)

    def build_config_report(self):
        """
        Build the report config block.

        :return: Text block in markdown format.
        """
        if os.path.isfile(self.config_report_path):
            data = open(self.config_report_path, encoding="utf-8").read()
            data = data.replace("\n", "<br>")
            logging.info(f"{self.config_report_path} file successfully loaded.")
            return f"<code>\n{data}\n</code>"
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
                text += f"<h4>{element.capitalize()}</h4>\n"
                text += "<ul>\n"
                if data[element]["items"]:
                    for item in data[element]["items"]:
                        text += f" <li>{item}</li>\n"
                else:
                    text += " <li>(no elements not covered)</li>\n"
                text += "</ul>\n"
                text += "\n"
            text += f"Total number of elements: {total_num_elements}\n\n"
            text += f"Total number of not covered elements: {total_num_not_covered}\n\n"
            text += f"Coverage rate: {rate * 100:.1f}% ({utils.get_color(rate, output_format='pdf')})\n\n"
        else:
            text = "\nThere are no end-to-end tests coverage.\n"
        return text
