import logging
import os.path

from rasa_model_report.controllers.MarkdownController import MarkdownController
from rasa_model_report.helpers.utils import get_project_name


class ModelReport:
    def __init__(self, rasa_path, output_dir, project, version, **kwargs):
        self.dirs = {}
        self.disable_nlu = False
        self.project = get_project_name(rasa_path)
        if project:
            self.project = project
        self.version = version
        logging.info("---")
        logging.info(
            f"Iniciando criação do relatório do modelo do bot {self.project},"
            "da versão {self.version if self.version else 'not identified'}"
        )
        self.markdown = MarkdownController(rasa_path, output_dir, self.project, self.version, **kwargs)
        self._load_attr(rasa_path, output_dir)
        self.generate_report()

    def _load_attr(self, rasa_path, output_dir):
        self.dirs.update({
            "RASA_PATH": rasa_path,
            "RESULTS_PATH": f"{rasa_path}/results",
            "OUTPUT_DIR": output_dir,
            "INTENT_HISTOGRAM": "intent_histogram.png",
            "INTENT_MATRIX": "intent_confusion_matrix.png",
            "ENTITY_HISTOGRAM": "DIETClassifier_histogram.png",
            "ENTITY_MATRIX": "DIETClassifier_confusion_matrix.png",
            "STORY_MATRIX": "story_confusion_matrix.png"
        })

    def generate_report(self):
        if os.path.isdir(self.dirs["RESULTS_PATH"]):
            # Overview
            self.markdown.add_text(self.markdown.title)
            self.markdown.add_text(self.markdown.build_summary())
            self.markdown.add_text(self.markdown.build_overview())
            self.markdown.break_line()

            # Configuração
            self.markdown.add_text(self.markdown.build_config_report())
            self.markdown.break_line()

            # Intenções
            self.markdown.add_text(self.markdown.build_intent_title())
            self.markdown.add_text(self.markdown.build_intent_table())
            self.markdown.add_text(self.markdown.build_intent_errors_table())
            self.markdown.add_image(self.dirs["INTENT_HISTOGRAM"], "Histograma")
            self.markdown.add_image(self.dirs["INTENT_MATRIX"], "Matriz de Confusão")

            # Entidades
            self.markdown.add_text(self.markdown.build_entity_title())
            self.markdown.add_text(self.markdown.build_entity_table())
            self.markdown.add_text(self.markdown.build_entity_errors_table())
            self.markdown.add_image(self.dirs['ENTITY_HISTOGRAM'], "Histograma")
            self.markdown.add_image(self.dirs['ENTITY_MATRIX'], "Matriz de Confusão")

            # NLU
            if self.markdown.nlu.is_connected():
                self.markdown.add_text(self.markdown.build_nlu_title())
                self.markdown.add_text(self.markdown.build_nlu_table())
                self.markdown.add_text(self.markdown.build_nlu_errors_table())

            # Respostas
            self.markdown.add_text(self.markdown.build_response_title())
            self.markdown.add_text(self.markdown.build_response_table())
            self.markdown.add_image(self.dirs['STORY_MATRIX'], "Matriz de Confusão")

            # Salvar relatório e overview
            self.markdown.save_report()
            self.markdown.save_overview()

            # Atualizar o README.md e index.md
            # self.markdown.update_readme()
            # self.markdown.update_index()
            logging.info("Script finalizado com sucesso")
        else:
            logging.error(f"Diretório {self.dirs['RESULTS_PATH']} não existe")
            logging.error(
                "Para informar p diretório onde contém os arquivo do projeto Rasa, utilize o parâmetro --path"
            )
            logging.error("Script finalizado com erros")
