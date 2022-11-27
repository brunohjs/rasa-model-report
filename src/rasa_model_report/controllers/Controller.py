class Controller:
    def __init__(self, rasa_path: str, output_dir: str, project: str, version: str) -> None:
        """
        Controller base class.

        :param rasa_path: Project Rasa path.
        :param output_dir: Output directory.
        :param project: Project name.
        :param version: Project version.
        """
        self.project = project
        self.version = version
        self.RASA_PATH = rasa_path
        self.OUTPUT_DIR = output_dir
        self.NLU_PATH = f"{self.RASA_PATH}/data".replace("//", "/")
        self.RESULTS_PATH = f"{self.RASA_PATH}/results".replace("//", "/")
        self.CONFIG_REPORT = f"{self.RASA_PATH}/config.yml".replace("//", "/")
