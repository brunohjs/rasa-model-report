class Controller:
    """
    Controller base class.
    """
    def __init__(self, rasa_path: str, output_path: str, project: str, version: str) -> None:
        """
        __init__ method.

        :param rasa_path: Project Rasa path.
        :param output_path: Output directory.
        :param project: Project name.
        :param version: Project version.
        """
        self.project: str = project
        self.version: str = version
        self.rasa_path: str = rasa_path
        self.output_path: str = output_path.replace("//", "/")
        self.nlu_path: str = f"{self.rasa_path}/data".replace("//", "/")
        self.results_path: str = f"{self.rasa_path}/results".replace("//", "/")
        self.config_report_path: str = f"{self.rasa_path}/config.yml".replace("//", "/")
