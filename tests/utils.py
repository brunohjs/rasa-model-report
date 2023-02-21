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


def load_mock_payloads():
    current_test_name = (
        os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]
    )
    current_test_name = current_test_name.split("[")[0]
    tests = MOCK_PAYLOADS.get(current_test_name, []) + MOCK_PAYLOADS["default"]
    for test in tests:
        responses.add(**test)
    return True
