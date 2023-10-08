import glob
import json
import os.path
import shutil

import responses


MOCK_PAYLOADS = json.load(open("tests/mocks/mock_payloads.json"))


def create_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def remove_dir(dir_name):
    if os.path.isdir(dir_name):
        shutil.rmtree(dir_name)


def remove_generated_files(rasa_path):
    files_to_find = (
        f"{rasa_path}/results/overview.json",
        f"{rasa_path}/results/e2e_coverage_report.txt",
        "tests/model_report.md",
        "model_report.md",
        "test.csv",
        f"{rasa_path}/results/*.csv"
    )
    files = []
    for file in files_to_find:
        files.extend(glob.glob(file))
    for file in files:
        if os.path.isfile(file):
            os.remove(file)


def check_string_in_file(string, filename):
    file = open(filename, encoding="utf-8")
    file_data = file.read()
    return string in file_data


def load_mock_payloads():
    current_test_name = (
        os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]
    )
    current_test_name = current_test_name.split("[")[0]
    tests = MOCK_PAYLOADS.get(current_test_name, []) + MOCK_PAYLOADS["default"]
    for test in tests:
        responses.add(**test)
    return True


def check_model_report_sections(model_report_path):
    file = open(model_report_path, encoding="utf-8")
    file_data = file.read()
    file.close()
    return "# Model health report" in file_data and \
        "## Index" in file_data and \
        "## Overview" in file_data and \
        "## Config" in file_data and \
        "## Intents" in file_data and \
        "## Entities" in file_data and \
        "## Core" in file_data and \
        "## E2E Coverage" in file_data


def check_model_report_images(model_report_path):
    file = open(model_report_path, encoding="utf-8")
    file_data = file.read()
    file.close()
    return "/intent_histogram.png" in file_data and \
        "/intent_confusion_matrix.png" in file_data and \
        "/DIETClassifier_histogram.png" in file_data and \
        "/DIETClassifier_confusion_matrix.png" in file_data and \
        "/story_confusion_matrix.png" in file_data and \
        "/intent_histogram.png" in file_data


def check_model_report_text(model_report_path, texts):
    file = open(model_report_path, encoding="utf-8")
    file_data = file.read()
    file.close()
    if isinstance(texts, str):
        return texts in file_data
    else:
        return all([text in file_data for text in texts])
