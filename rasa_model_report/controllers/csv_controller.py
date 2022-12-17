import logging
from typing import List

from rasa_model_report.controllers.controller import Controller


class CsvController(Controller):
    """
    Controller responsible for CSV files.
    """
    def __init__(self, rasa_path: str, output_path: str, project_name: str, project_version: str) -> None:
        """
        __init__ method.

        :param rasa_path: Rasa project path.
        :param output_path: Output directory of CSV files.
        :param project_name: Project name.
        :param project_version: Project version.
        """
        super().__init__(rasa_path, output_path, project_name, project_version)

    def save(self, data: List[List[str]], filename: str) -> None:
        """
        Save data to a CSV file.

        :param data: Data in matrix format. First item is the header.
        :param filename: Name of the new file.
        """
        try:
            file = open(f"{self.results_path}/{filename}", "w", encoding="utf-8")
            for line in data:
                line = [f"\"{item}\"" for item in line]
                new_line = ",".join(line)
                file.writelines(new_line + "\n")
            file.close()
            logging.info(f"{filename} file successfully saved.")
        except FileNotFoundError as error:
            logging.error(f"Could not find the file: {self.results_path}/{filename}. Error: {error}.")
