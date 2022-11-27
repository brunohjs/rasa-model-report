class Controller:
    def __init__(self, rasa_path: str, output_dir: str, project: str, version: str) -> None:
        """
        Controller base class.

        :param rasa_path: Project Rasa path.
        :param output_dir: Output directory.
        :param project: Project name.
        :param version: Project version.
        """
        self.project: str = project
        self.version: str = version
        self.RASA_PATH: str = rasa_path
        self.OUTPUT_DIR: str = output_dir
        self.NLU_PATH: str = f"{self.RASA_PATH}/data".replace("//", "/")
        self.RESULTS_PATH: str = f"{self.RASA_PATH}/results".replace("//", "/")
        self.CONFIG_REPORT: str = f"{self.RASA_PATH}/config.yml".replace("//", "/")
