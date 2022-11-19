import logging
from typing import List

from rasa_model_report.controllers.Controller import Controller


class CsvController(Controller):
    def __init__(self, rasa_path: str, output_dir: str, project: str, version: str) -> None:
        """
        Controller responsible for CSV files.

        :param rasa_path: Rasa project path.
        :param output_dir: Output directory of CSV files.
        :param project: Project name.
        :param version: Version of project.
        """
        super().__init__(rasa_path, output_dir, project, version)

    def save(self, data: List[List[str]], filename: str) -> None:
        """
        Save data to a CSV file.

        :param data: Data in matrix format. First item is the header.
        :param str filename: Name of the new file.
        """
        try:
            file = open(f"{self.RESULTS_PATH}/{filename}", "w")
            for line in data:
                line = [f"\"{item}\"" for item in line]
                new_line = ",".join(line)
                file.writelines(new_line + "\n")
            file.close()
            logging.info(f"Arquivo {filename} salvo com sucesso.")
        except FileNotFoundError as error:
            logging.error(f"Não foi possível encontrar o arquivo: {self.RESULTS_PATH}/{filename}. Erro: {error}.")
