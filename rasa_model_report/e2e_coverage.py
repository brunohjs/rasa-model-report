import glob
import json
import logging
import os.path
import re
import sys
from typing import Any
from typing import List
from typing import Optional

from yaml import safe_load


logging.basicConfig(level=logging.INFO)

env = {
    "DEFAULT_THRESHOLD": 0.8,
    "BOT_PATH": ".."
}


def change_base_dir(new_dir: Optional[str] = None) -> None:
    env["BOT_PATH"] = new_dir if new_dir else env["BOT_PATH"]
    env.update({
        "RASA_DOMAIN_PATH": f"{env['BOT_PATH']}/rasa/domain.yml",
        "STORY_REPORT_PATH": f"{env['BOT_PATH']}/rasa/results/story_report.json",
        "ACTIONS_PATH": f"{env['BOT_PATH']}/actions"
    })


def export_coverage(not_coveraged: List[str], total_count: int, coveraged_count: int) -> None:
    with open("e2e_coverage_report.txt", "w") as file:
        file.write("-------------------------------------------------\n")
        file.write("Relatório de cobertura dos testes end-to-end\n")
        file.write("-------------------------------------------------\n")
        if not_coveraged:
            file.write("Utters e actions que não estão cobertas:\n\n")
            for item in not_coveraged:
                file.write(f"- {item}\n")
            file.write("\n")
        else:
            file.write("Todas as utters e actions estão contempladas nos testes end-to-end.\n\n")
        file.write(f"Número total de utters/actions: {total_count}\n")
        file.write(f"Número total de utters/actions cobertas: {coveraged_count}\n")
        coverage_rate = coveraged_count / total_count
        file.write(f"Taxa de cobertura: {coverage_rate*100:.2f}%\n")
        file.write("-------------------------------------------------\n")
    return None


def show(domain: List[str], report: List[str]) -> float:
    num_total = len(domain)
    templates = check_templates(domain)
    domain = diff(domain, templates)
    utter_forms = check_utter_forms(domain)
    domain = diff(domain, utter_forms)
    validate_forms = check_validate_forms(domain)
    domain = diff(domain, validate_forms)
    not_coveraged = diff(domain, report)
    num_coveraged = num_total - len(not_coveraged)
    coverage_rate = num_coveraged / num_total
    export_coverage(not_coveraged, num_total, num_coveraged)
    logging.info("---------------------------------------------")
    logging.info("Relatório de cobertura dos testes end-to-end")
    logging.info("---------------------------------------------")
    if not_coveraged:
        logging.info("Utters e actions que não estão cobertas:")
        for element in not_coveraged:
            logging.info(f"  - {element}")
    else:
        logging.info("Todas as utters e actions estão contempladas nos testes end-to-end.")
    logging.info(f"Número total de utters/actions: \t\t{num_total}")
    logging.info(f"Número total de utters/actions cobertas: \t{num_coveraged}")
    logging.info(f"Taxa de cobertura: \t\t\t\t{coverage_rate*100:.2f}%")
    return coverage_rate


def get_params():
    params = {
        "t": env["DEFAULT_THRESHOLD"],
        "nt": False,
        "botname": None
    }
    if sys.argv and len(sys.argv) > 1:
        for arg in sys.argv:
            search = re.search("ps-chatbot-[a-zA-Z-]*", arg)
            if search:
                params["botname"] = search.string
                break
        if "-t" in sys.argv:
            index = sys.argv.index("-t")
            value = sys.argv[index + 1]
            params["t"] = float(value)
        params["nt"] = "-nt" in sys.argv
    return params


def diff(list1: List[Any], list2: List[Any]) -> List[Any]:
    return [element for element in list1 if element not in list2]


def get_domain_responses():
    domain = safe_load(open(env["RASA_DOMAIN_PATH"]))
    actions = domain["actions"]
    if "action_default_fallback" in actions:
        actions.remove("action_default_fallback")
    if "action_session_start" in actions:
        actions.remove("action_session_start")
    if "action_unlikely_intent" in actions:
        actions.remove("action_unlikely_intent")
    return actions


def check_templates(domain: List[str]) -> List[str]:
    result = []
    actions_data = glob.glob(f"{env['ACTIONS_PATH']}/**/*.py")
    actions_files = [open(file).read() for file in actions_data]
    for response in domain:
        is_template = False
        for file in actions_files:
            if re.search(r"(template|response)\s?=\s?[\'|\"]" + response + r"[\'|\"]", file) \
            or re.search(r"FollowupAction\(\"" + response + r"\"\)", file) \
            or re.search(r"ActionExecuted\(\"" + response + r"\"\)", file):
                is_template = True
                break
        if is_template:
            result.append(response)
    return result


def check_utter_forms(domain: List[str]) -> List[str]:
    return [utter for utter in domain if utter.startswith("utter_ask") or utter.startswith("action_ask")]


def check_validate_forms(domain: List[str]) -> List[str]:
    return [item for item in domain if item.startswith("validate_") and item.endswith("_form")]


def get_report_responses() -> List[str]:
    json_file = open(env["STORY_REPORT_PATH"])
    data = json.load(json_file)
    data = [response for response in data.keys() if response.startswith("utter_") or response.startswith("action_")]
    if "action_listen" in data:
        data.remove("action_listen")
    return data


def check_directory(botname: str) -> None:
    if not os.path.isfile(env["RASA_DOMAIN_PATH"]):
        change_base_dir(f"../{botname}")


def main() -> None:
    logging.info("Inicializando verificação de cobertura dos testes end-to-end")
    params = get_params()
    change_base_dir()
    threshold = params["t"]
    check_directory(params["botname"])
    report = get_report_responses()
    domain = get_domain_responses()
    result = show(domain, report)
    if params["nt"]:
        logging.info("Parâmetro -nt identificado. O threshold será ignorado.")
        exit(0)
    else:
        logging.info(f"Threshold identificado. Valor de {threshold * 100:.2f}%")
        if threshold > result:
            logging.error(
                "Verificação de cobertura falhou. "
                f"Cobertura deve ser maior que {threshold * 100:.2f}%. Resultado: {result * 100:.2f}%"
            )
            exit(1)
        else:
            logging.info(f"Verificação de cobertura passou! Resultado: {result*100:.2f}%")
            exit(0)


if __name__ == "__main__":
    main()
