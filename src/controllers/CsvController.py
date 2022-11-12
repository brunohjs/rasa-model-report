import logging

from controllers.Controller import Controller


class CsvController(Controller):
    def __init__(self, rasa_path, output_dir, project, version) -> None:
        super().__init__(rasa_path, output_dir, project, version)

    def save(self, data, filename):
        try:
            file = open(f"{self.RESULTS_PATH}/{filename}", "w")
            for line in data:
                line = [f"\"{item}\"" for item in line]
                new_line = ",".join(line)
                file.writelines(new_line + "\n")
            file.close()
            logging.info(f"Arquivo {filename} salvo com sucesso.")
        except Exception as error:
            logging.error(f"Não foi possível salvar o arquivo {filename}. Erro: {error}")
