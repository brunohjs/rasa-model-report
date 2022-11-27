import logging
import os.path
from typing import Dict
from typing import List
from typing import Union

from src.rasa_model_report.controllers.Controller import Controller
from src.rasa_model_report.controllers.CsvController import CsvController
from src.rasa_model_report.controllers.JsonController import JsonController
from src.rasa_model_report.controllers.NluController import NluController
from src.rasa_model_report.helpers.utils import check
from src.rasa_model_report.helpers.utils import get_color
from src.rasa_model_report.helpers.utils import scale


class MarkdownController(Controller):
    def __init__(self, rasa_path, output_dir, project, version, **kwargs) -> None:
        super().__init__(rasa_path, output_dir, project, version)
        self.result = ""
        self.title = "# Relatório da saúde do modelo"
        self.json = JsonController(rasa_path, output_dir, self.project, self.version)
        self.csv = CsvController(rasa_path, output_dir, self.project, self.version)
        self.nlu = NluController(
            rasa_path,
            output_dir,
            self.project,
            self.version,
            url=kwargs.get("rasa_api_url"),
            disable_nlu=kwargs.get("disable_nlu")
        )
        self.json.update_overview({"nlu": self.nlu.get_general_grade()})
        self._set_dirs()

    def _set_dirs(self):
        self.OUTPUT_REPORT_FILE = f"{self.OUTPUT_DIR}/model_report.md"
        self.README_PATH = "README.md"

    def add_text(self, text: str) -> None:
        """
        Função que concatena um texto ao texto final
        """
        if isinstance(text, str):
            self.result += "\n" + text

    def add_image(self, image: str, title: str) -> None:
        """
        Função que concatena um bloco de texto com um bloco de imagem.
        """
        if os.path.isfile(f"{self.RESULTS_PATH}/{image}"):
            self.result += f"### {title}\n![{title}]({self.RESULTS_PATH}/{image} '{title}')" + "\n"
            logging.info(f"A imagem {image} foi adicionada com sucesso")
        else:
            logging.warning(f"A imagem {image} não foi encontrada")

    def break_line(self) -> None:
        """
        Função que insere uma quebra de linha ao texto final
        """
        self.result += "\n"

    def build_line_entity(self, entities) -> None:
        if not entities:
            return "-"
        return "\n\t\t\t\t\t\t\t".join([f"""<details>
                            <summary>{entity['entity']}</summary>
                            <pre>início: {entity['start']}
                            <br>fim: {entity['end']}
                            <br>valor: {entity['value']}
                            </pre>
                        </details>""" for entity in entities])

    def build_summary(self) -> None:
        text = "## Índice\n"
        text += " - [Overview](#overview)\n"
        if os.path.isfile(self.CONFIG_REPORT):
            text += " - [Configurações](#configs)\n"
        text += " - [Intenções](#intents)\n"
        text += " - [Entidades](#entities)\n"
        if self.nlu.is_connected():
            text += " - [NLU](#nlu)\n"
        text += " - [Respostas](#responses)\n"
        text += "\n"
        return text

    def build_table(self, data: list) -> str:
        """
        Função para auxiliar na construção de uma tabela em markdown.
        """
        header = "|" + "|".join(data[0]) + "|\n"
        header += "|-" * len(data[0]) + "|\n"
        content = ""
        for row in data[1:]:
            text_row = "|" + "|".join(row) + "|\n"
            content += text_row
        return header + content

    def build_overview(self) -> str:
        """
        Função que monta o bloco de texto responsável pelo resumo do relatório.
        """
        overview = self.json.get_overview()
        for item in ["intent", "entity", "response", "nlu"]:
            overview[item] = overview[item] if isinstance(overview.get(item), (float, int)) else 0
        text = "## Overview <a name='overview'></a>\n"
        style = "style='font-size:16px'"
        text += "|Bot|Versão|Data de criação|Data de atualização|\n"
        text += "|:-:|:-:|:-:|:-:|\n"
        text += f"|<span {style}>**{self.project}**</span>|\
            <span {style}>{self.version if self.version else 'not identified'}</span>|\
            <span {style}>{overview['created_at']}</span>|\
            <span {style}>{overview['updated_at']}</span>|\n\n"
        style = "style='font-size:20px'"
        text += f"|Intenção|Entidade|NLU|Resposta|<span {style}>Geral</span>|\n"
        text += "|:-:|:-:|:-:|:-:|:-:|\n"
        text += f"|{scale(overview['intent'], 10)}\
            |{scale(overview['entity'], 10)}\
            |{scale(overview['nlu'], 10)}\
            |{scale(overview['response'], 10)}\
            |<span {style}>**{scale(overview['overall'], 10)}**</span>|\n"
        text += f"{get_color(overview['intent'])}\
            |{get_color(overview['entity'])}\
            |{get_color(overview['nlu'])}\
            |{get_color(overview['response'])}\
            |<span {style}>{get_color(overview['overall'])}</span>|"
        return text

    def build_intent_title(self) -> str:
        title = "## Intenções <a name='intents'></a>\n"
        description = "Seção que aborda métricas sobre as intenções do modelo.\n"
        return title + description

    def build_intent_overview(self) -> str:
        intent_overview = self.json.get_intent_overview().get("macro avg")
        text = "|Precisão|Recall|F1 Score|Exemplos|\n"
        text += "|:-:|:-:|:-:|:-:|\n"
        text += f"|{intent_overview['precision'] * 100:.1f}%\
            |{intent_overview['recall'] * 100:.1f}%\
            |{intent_overview['f1-score'] * 100:.1f}%\
            |{intent_overview['support']}|\n"
        text += f"|{get_color(intent_overview['precision'])}\
            |{get_color(intent_overview['recall'])}\
            |{get_color(intent_overview['f1-score'])}\
            ||\n"
        return text

    def build_intent_table(self) -> str:
        """
        Função que monta o bloco de texto sobre intenções no relatório.
        """
        title = "### Métricas\n"
        description = "Tabela com as métricas das intenções.\n"
        title += description
        data = self.json.get_intents()
        table_data = [[
            "",
            "Intenção",
            "Precisão",
            "Recall",
            "F1 Score",
            "Número de exemplos"
        ]]
        for item in data:
            table_data.append(self._build_line_table(item))
        if len(table_data) > 1:
            self.csv.save(table_data, "intent_report.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNão foram encontradas intenções nesse modelo.\n"
            return title + text

    def build_intent_errors_table(self) -> str:
        """
        Função que monta o bloco de texto 'Intenções confusas' no relatório.
        """
        title = "### Intenções confusas\n"
        description = "Aqui vão constar todas as frases confusas ou erradas do modelo.\n"
        title += description
        data = self.json.get_intent_errors()
        table_data = [[
            "Texto",
            "Intenção",
            "Intenção prevista",
            "Confiança"
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
            return title + self.build_table(table_data)
        else:
            text = "\nNão foram encontradas confusões ou erros de intenções nesse modelo.\n"
            return title + text

    def build_entity_title(self) -> str:
        title = "## Entidades <a name='entities'></a>\n"
        description = "Seção que aborda métricas sobre as entidades do modelo.\n"
        return title + description

    def build_entity_overview(self) -> str:
        entity_overview = self.json.get_entity_overview().get("macro avg")
        text = "|Precisão|Recall|F1 Score|Exemplos|\n"
        text += "|:-:|:-:|:-:|:-:|\n"
        text += f"|{entity_overview['precision'] * 100:.1f}%\
            |{entity_overview['recall'] * 100:.1f}%\
            |{entity_overview['f1-score'] * 100:.1f}%\
            |{entity_overview['support']}|\n"
        text += f"|{get_color(entity_overview['precision'])}\
            |{get_color(entity_overview['recall'])}\
            |{get_color(entity_overview['f1-score'])}\
            ||\n"
        return text

    def build_entity_table(self) -> str:
        """
        Função que monta o bloco de texto das entidades no relatório.
        """
        title = "### Métricas\n"
        description = "Tabela com as métricas das entidades.\n"
        title += description + "\n"
        data = self.json.get_entities()
        table_data = [[
            "",
            "Entidade",
            "Precisão",
            "Recall",
            "F1 Score",
            "Número de exemplos"
        ]]
        for item in data:
            table_data.append(self._build_line_table(item))
        if len(table_data) > 1:
            self.csv.save(table_data, "DIETClassifier_report.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNão foram encontradas entidades nesse modelo.\n"
            return title + text

    def build_entity_errors_table(self) -> str:
        """
        Função que monta o bloco de texto 'Intenções confusas' no relatório.
        """
        title = "### Entidades confusas\n"
        description = "Aqui vão constar todas as entidades confusas ou erradas do modelo.\n"
        title += description
        data = self.json.get_entity_errors()
        table_data = """<table>
            <thead>
                <tr>
                    <th>Texto</th>
                    <th>Entidades</th>
                    <th>Entidades previstas</th>
                </tr>
            </thead>
            <tbody>"""
        for row in data:
            table_data += f"""
                <tr>
                    <td>{row['text']}</td>
                    <td>
                        {self.build_line_entity(row['entities'])}
                    </td>
                    <td>
                        {self.build_line_entity(row['predicted_entities'])}
                    </td>
                </tr>"""
        table_data += """
            </tbody>
        </table>\n\n"""
        if data:
            return title + table_data
        else:
            text = "\nNão foram encontradas confusões ou erros de intenções nesse modelo.\n"
            return title + text

    def build_response_title(self) -> str:
        title = "## Respostas <a name='responses'></a>\n"
        description = "Seção que aborda métricas sobre as respostas e histórias do bot.\n"
        return title + description

    def build_response_overview(self) -> str:
        response_overview = self.json.get_response_overview().get("macro avg")
        text = "|Precisão|Recall|F1 Score|Exemplos|\n"
        text += "|:-:|:-:|:-:|:-:|\n"
        text += f"|{response_overview['precision'] * 100:.1f}%\
            |{response_overview['recall'] * 100:.1f}%\
            |{response_overview['f1-score'] * 100:.1f}%\
            |{response_overview['support']}|\n"
        text += f"|{get_color(response_overview['precision'])}\
            |{get_color(response_overview['recall'])}\
            |{get_color(response_overview['f1-score'])}\
            ||\n"
        return text

    def build_response_table(self) -> str:
        """
        Função que monta o bloco de texto das histórias no relatório.
        """
        title = "### Métricas\n"
        description = "Tabela com as métricas das respostas do bot.\n"
        title += description + "\n"
        data = self.json.get_responses()
        table_data = [[
            "",
            "Resposta",
            "Precisão",
            "Recall",
            "F1 Score",
            "Número de ocorrências"
        ]]
        for item in data:
            if item["name"].startswith("[") or not \
                    (item["name"].startswith("utter_") or item["name"].startswith("action_")):
                continue
            table_data.append(self._build_line_table(item))
        if len(table_data) > 1:
            self.csv.save(table_data, "story_report.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNão foram encontradas respostas nesse modelo.\n"
            return title + text

    def build_nlu_title(self) -> str:
        title = "## NLU <a name='nlu'></a>\n"
        description = "Seção que aborda métricas sobre a NLU e suas frases de exemplos.\n"
        return title + description

    def build_nlu_table(self) -> str:
        title = "### Sentenças\n"
        description = "Tabela com as métricas das frases de treinamento do bot.\n"
        title += description + "\n"
        data = self.nlu.get_data()
        table_data = [[
            "",
            "Texto",
            "Intenção",
            "Intenção prevista",
            "Confiança",
            "Compreendido"
        ]]
        for item in data:
            new_item = {
                "text": item["text"],
                "intent": item["intent"],
                "predicted_intent": item["predicted_intent"],
            }
            color = get_color(item["confidence"])
            new_item["confidence"] = f"{item['confidence'] * 100:.1f}%"
            new_item["understood"] = check(not item["understood"])
            table_data.append([color] + list(new_item.values()))
        if len(table_data) > 1:
            self.csv.save(table_data, "nlu_report.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNão foram encontradas frases de exemplos nesse modelo.\n"
            return title + text

    def build_nlu_errors_table(self) -> str:
        title = "### Sentenças com problemas\n"
        description = "Tabela com as sentenças que não foram compreendidas corretamente pelo modelo.\n"
        title += description + "\n"
        data = self.nlu.get_problem_sentences()
        table_data = [[
            "",
            "Texto",
            "Intenção",
            "Intenção prevista",
            "Confiança",
            "Compreendido"
        ]]
        for item in data:
            new_item = {
                "text": item["text"],
                "intent": item["intent"],
                "predicted_intent": item["predicted_intent"],
            }
            color = get_color(item["confidence"])
            new_item["confidence"] = f"{item['confidence'] * 100:.1f}%"
            new_item["understood"] = check(not item["understood"])
            table_data.append([color] + list(new_item.values()))
        if len(table_data) > 1:
            self.csv.save(table_data, "nlu_report.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNão há sentenças que não foram compreendidas nesse modelo.\n"
            return title + text

    def build_config_report(self) -> str:
        """
        Função que monta o bloco de texto responsável pela configuração do modelo do relatório.
        """
        if os.path.isfile(self.CONFIG_REPORT):
            title = "## Configurações <a name='configs'></a>\n"
            description = "Configurações que foram utilizadas na *pipeline* de treinamento e nas *policies*.\n"
            title += description
            data = open(self.CONFIG_REPORT).read()
            logging.info(f"Arquivo {self.CONFIG_REPORT} carregado com sucesso")
            return f"{title}```yaml\n{data}\n```"
        else:
            logging.warning("O bloco de configuração não será gerado, pois o arquivo não foi encontrado")
            return ""

    def _build_line_table(self, data: Dict[str, Union[float, Dict]]) -> List[str]:
        return [
            get_color(data["f1-score"]),
            data["name"],
            f"{data['precision'] * 100:.1f}%",
            f"{data['recall'] * 100:.1f}%",
            f"{data['f1-score'] * 100:.1f}%",
            str(data['support'])
        ]

    def save_report(self) -> None:
        """
        Função que salva os dados do relatório em um arquivo.
        """
        if os.path.isfile(self.OUTPUT_REPORT_FILE):
            text = f"Arquivo {self.OUTPUT_REPORT_FILE} alterado com sucesso"
        else:
            text = f"Arquivo {self.OUTPUT_REPORT_FILE} criado com sucesso"
        file = open(self.OUTPUT_REPORT_FILE, "w")
        file.write(self.result)
        file.close()
        logging.info(text)

    def save_overview(self) -> None:
        self.json.save_overview()
