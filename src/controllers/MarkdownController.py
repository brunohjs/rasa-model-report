import glob
import logging
import os.path

from controllers.Controller import Controller
from controllers.CsvController import CsvController
from controllers.JsonController import JsonController
from controllers.NluController import NluController
from helpers.utils import check
from helpers.utils import convert_to_date
from helpers.utils import get_color
from helpers.utils import scale


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
            disable_nlu=kwargs.get("disable_nlu")
        )
        self.json.update_overview({"nlu": self.nlu.get_general_grade()})
        self._set_dirs()

    def _set_dirs(self):
        self.OUTPUT_REPORT_FILE = f"{self.OUTPUT_DIR}/model_report.md"
        self.README_PATH = "README.md"
        self.INDEX_PATH = "reports/index.md"

    def add_text(self, text: str) -> str:
        """
        Função que concatena um texto ao texto final
        """
        self.result += "\n" + text

    def add_image(self, image: str, title: str) -> str:
        """
        Função que concatena um bloco de texto com um bloco de imagem.
        """
        if os.path.isfile(f"{self.RESULTS_PATH}/{image}"):
            self.result += f"### {title}\n![{title}]({image} 'Teste')" + "\n"
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
        text += " - [Configurações](#config)\n"
        text += " - [Intenções](#intention)\n"
        text += " - [Entidades](#entity)\n"
        text += " - [NLU](#nlu)\n"
        text += " - [Respostas](#response)\n"
        text += "\n"
        text += "[Voltar para o início](../../index.md)\n"
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
        model_link = f"https://ps-nightcity-bucket.s3.amazonaws.com/models/" \
            f"{overview['project']}/{overview['project']}-v{overview['version']}.tar.gz"
        text = "## Overview <a name='overview'></a>\n"
        style = "style='font-size:16px'"
        text += "|Bot|Versão|Rasa|Data de criação|Data de atualização|Modelo|\n"
        text += "|:-:|:-:|:-:|:-:|:-:|:-:|\n"
        text += f"|<span {style}>**{self.project}**</span>|\
            <span {style}>{self.version if self.version else 'not identified'}</span>|\
            <span {style}>{overview['rasa_version']}</span>|\
            <span {style}>{overview['created_at']}</span>|\
            <span {style}>{overview['updated_at']}</span>|\
            [Link]({model_link})|\n\n"
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
        title = "## Intenções <a name='intention'></a>\n"
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
            color = get_color(item["f1-score"])
            item["precision"] = f"{item['precision'] * 100:.1f}%"
            item["recall"] = f"{item['recall'] * 100:.1f}%"
            item["f1-score"] = f"{item['f1-score'] * 100:.1f}%"
            item["support"] = str(item['support'])
            if item.get("confused_with") or item.get("confused_with") == {}:
                del item["confused_with"]
            table_data.append([color] + list(item.values()))
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
                row["intent_prediction"]["confidence"] = f"{row['intent_prediction']['confidence'] * 100:.1f}%"
                table_data.append([
                    row["text"],
                    row["intent"],
                    row["intent_prediction"]["name"],
                    row["intent_prediction"]["confidence"]
                ])
        if len(table_data) > 1:
            self.csv.save(table_data, "intent_errors.csv")
            return title + self.build_table(table_data)
        else:
            text = "\nNão foram encontradas confusões ou erros de intenções nesse modelo.\n"
            return title + text

    def build_entity_title(self) -> str:
        title = "## Entidades <a name='entity'></a>\n"
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
            color = get_color(item["f1-score"])
            item["precision"] = f"{item['precision'] * 100:.1f}%"
            item["recall"] = f"{item['recall'] * 100:.1f}%"
            item["f1-score"] = f"{item['f1-score'] * 100:.1f}%"
            item["support"] = str(item['support'])
            if item.get("confused_with") or item.get("confused_with") == {}:
                del item["confused_with"]
            table_data.append([color] + list(item.values()))
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
        title = "## Respostas <a name='response'></a>\n"
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
            color = get_color(item["f1-score"])
            item["precision"] = f"{item['precision'] * 100:.1f}%"
            item["recall"] = f"{item['recall'] * 100:.1f}%"
            item["f1-score"] = f"{item['f1-score'] * 100:.1f}%"
            item["support"] = str(item['support'])
            if item.get("confused_with") or item.get("confused_with") == {}:
                del item["confused_with"]
            table_data.append([color] + list(item.values()))
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
            title = "## Configurações <a name='config'></a>\n"
            description = "Configurações que foram utilizadas na *pipeline* de treinamento e nas *policies*.\n"
            title += description
            data = open(self.CONFIG_REPORT).read()
            logging.info(f"Arquivo {self.CONFIG_REPORT} carregado com sucesso")
            return f"{title}```yaml\n{data}\n```"
        else:
            logging.warning("O bloco de configuração não será gerado, pois o arquivo não foi encontrado")
            return ""

    def build_bots_overview(self) -> str:
        """
        Retorna o resumo das acurácias dos modelos, que são mostrados no REAMDE.md.
        """
        text_list = []
        versions = self._get_latest_bots(5)
        for bot in versions:
            text = f"## {bot}\n"
            text += "|Versão|Intenção|Entidade|História|Geral|Rasa|Data de criação|\n"
            text += "|-:|-:|-:|-:|-:|-:|-:|\n"
            for version in versions[bot]:
                path = f"reports/{bot}/{version}"
                overview = self.json.get_specific_overview(bot, version)
                if overview:
                    text += f"|**[{version}]({path}/model_report.md)**\
                        |{scale(overview['intent'], 10)} {get_color(overview['intent'], 10)}\
                        |{scale(overview['entity'], 10)} {get_color(overview['entity'], 10)}\
                        |{scale(overview['response'], 10)} {get_color(overview['response'], 10)}\
                        |**{scale(overview['overall'], 10)}** {get_color(overview['overall'], 10)}\
                        |{overview['rasa_version']}\
                        |{overview['created_at']}\n"
            if len(versions[bot]) < 5:
                for i in range(5 - len(versions[bot])):
                    text += "|**-**\
                        |-\
                        |-\
                        |-\
                        |-\
                        |-\n"
            text += "\n"
            text_list.append(text)
        text = self._replace_markdown_file(text_list)
        return text

    def _replace_markdown_file(self, text: str) -> str:
        """
        Função que atualiza o conteúdo do README.md.
        """
        new_markdown = []
        data = open(self.README_PATH).read()
        temp = data.split('\n#')
        report_starts = False
        for item in temp:
            if report_starts and item.startswith("# "):
                report_starts = False
            if not report_starts:
                new_markdown.append(item)
            if item.startswith("# Últimos relatórios"):
                report_starts = True
            if report_starts and not item.startswith("## "):
                new_markdown += text
        new_markdown = "\n#".join(new_markdown)
        return new_markdown

    def _get_latest_bots(self, size: int = 0) -> dict:
        """
        Função que retorna as últimas versões do bot.
        """
        versions = {}
        files = glob.glob("reports/ps-chatbot-*/*")
        files = sorted(files)
        for file in files:
            file = file.split("/")
            bot = file[1]
            version = file[2]
            overview = self.json.get_specific_overview(bot, version)
            if overview:
                if versions.get(bot):
                    versions[bot].append(overview)
                else:
                    versions[bot] = [overview]
        if size:
            versions = {key: self._order_versions(versions[key])[:-(size + 1):-1] for key in versions}
        else:
            versions = {key: self._order_versions(versions[key])[::-1] for key in versions}
        return versions

    def _order_versions(self, versions: list) -> list:
        """
        Função para ordenar as versões
        """
        versions = sorted(versions, key=lambda x: convert_to_date(x["created_at"]))
        return [version["version"] for version in versions]

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

    def update_readme(self) -> None:
        """
        Função que salva dados em um arquivo.
        """
        readme_file = self.README_PATH
        if os.path.isfile(self.README_PATH):
            text = f"Arquivo {readme_file} alterado com sucesso"
        else:
            text = f"Arquivo {readme_file} criado com sucesso"
        data = self.build_bots_overview()
        file = open(readme_file, "w")
        file.write(data)
        file.close()
        logging.info(text)

    def update_index(self) -> None:
        index_file = self.INDEX_PATH
        file = open(index_file, "w")
        if os.path.isfile(self.INDEX_PATH):
            message = f"Arquivo {index_file} alterado com sucesso"
        else:
            message = f"Arquivo {index_file} criado com sucesso"
        versions = self._get_latest_bots()
        if versions:
            file.writelines("# Versões\n")
            for bot in versions:
                if versions.get(bot):
                    file.writelines(f"\n## {bot}\n")
                    for version in versions[bot]:
                        overview = self.json.get_specific_overview(bot, version)
                        if overview:
                            text = f"[[{version}]({bot}/{version}/model_report.md)] {overview['created_at']}\n\n"
                            file.writelines(text)
        file.close()
        logging.info(message)
