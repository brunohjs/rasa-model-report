import glob
import json
import logging
import sys


def get_params():
    params = {}
    if len(sys.argv) > 1:
        params["project"] = sys.argv[1]
        params["version"] = sys.argv[2]
        return params
    else:
        logging.error(
            "É necessário informar os parâmetros: bot e versão. "
            "Exemplo: formatter.py ps-chatbot-botweb 0.0.1-rc.8"
        )
        exit(1)


def get_json_data(filename):
    file = open(filename)
    json_data = json.load(file)
    file.close()
    return json_data


def save_json_data(filename, data):
    file = open(filename, "w", encoding="utf-8")
    json.dump(data, file, indent=4, ensure_ascii=False)
    file.writelines("\n")
    file.close()


def format_json_file(filename):
    data = get_json_data(filename)
    save_json_data(filename, data)
    logging.info(f"Arquivo {filename} formatado.")


def get_all_json_files(project, version):
    files = glob.glob(f"reports/{project}/{version}/*.json")
    if files:
        for file in files:
            format_json_file(file)
    else:
        logging.error(f"Nenhum arquivo foi encontrado no diretório {project}/{version}/")
        exit(1)


if __name__ == "__main__":
    params = get_params()
    get_all_json_files(params["project"], params["version"])
