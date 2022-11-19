class Controller:
    def __init__(self, rasa_path, output_dir, project, version) -> None:
        self.project = project
        self.version = version
        self.RASA_PATH = rasa_path
        self.OUTPUT_DIR = output_dir
        self.NLU_PATH = f"{self.RASA_PATH}/data/**/**.yml".replace("//", "/")
        self.RESULTS_PATH = f"{self.RASA_PATH}/results".replace("//", "/")
        self.CONFIG_REPORT = f"{self.RASA_PATH}/config.yml".replace("//", "/")
