import os.path
import re

import responses
from click.testing import CliRunner

from rasa_model_report.main import main
from tests import utils


@responses.activate
def test_main_with_valid_path(rasa_path):
    runner = CliRunner()
    result = runner.invoke(main, ["--path", rasa_path])
    assert os.path.isfile("model_report.html")
    assert utils.check_model_report_images("model_report.html")
    assert result.exit_code == 0
    assert result.output == ""


@responses.activate
def test_main_with_invalid_path():
    utils.load_mock_payloads()
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert not os.path.isfile("model_report.html")
    assert result.exit_code == 0
    assert result.output == ""


@responses.activate
def test_main_with_pdf_format(rasa_path):
    runner = CliRunner()
    result = runner.invoke(main, ["--path", rasa_path, "--format", "pdf"])
    assert os.path.isfile("model_report.pdf")
    assert not os.path.isfile("model_report.md")
    assert result.exit_code == 0
    assert result.output == ""


@responses.activate
def test_main_with_invalid_format(rasa_path):
    runner = CliRunner()
    result = runner.invoke(main, ["--path", rasa_path, "--format", "mp3"])
    assert not os.path.isfile("model_report.pdf")
    assert not os.path.isfile("model_report.md")
    assert result.exit_code == 2
    assert result.output == "Usage: main [OPTIONS]\n\nError: No such option: --format Did you mean --output-format?\n"


@responses.activate
def test_main_with_no_images(rasa_path):
    utils.load_mock_payloads()
    runner = CliRunner()
    result = runner.invoke(main, ["--path", rasa_path, "--no-images"])
    assert os.path.isfile("model_report.md")
    assert not utils.check_model_report_images("model_report.md")
    assert result.exit_code == 0
    assert result.output == ""


@responses.activate
def test_main_with_default_precision(rasa_path):
    utils.load_mock_payloads()
    runner = CliRunner()
    result = runner.invoke(main, ["--path", rasa_path, "--precision", "2"])
    file = open("model_report.md")
    data = file.read()
    file.close()
    assert os.path.isfile("model_report.md")
    assert re.search(r"\|<span style='font-size:20px'>\*\*(\d{1,2}|\d+\.\d{2})\*\*</span>\|", data)
    assert not re.search(r"\|<span style='font-size:20px'>\*\*(\d{1,2}|\d+\.\d{3})\*\*</span>\|", data)
    assert not re.search(r"\|<span style='font-size:20px'>\*\*(\d{1,2}|\d+\.\d{1})\*\*</span>\|", data)
    assert result.exit_code == 0
    assert result.output == ""


@responses.activate
def test_main_with_4_precision(rasa_path):
    utils.load_mock_payloads()
    runner = CliRunner()
    result = runner.invoke(main, ["--path", rasa_path, "--precision", "4"])
    file = open("model_report.md")
    data = file.read()
    file.close()
    assert os.path.isfile("model_report.md")
    assert re.search(r"\|<span style='font-size:20px'>\*\*(\d{1,2}|\d+\.\d{4})\*\*</span>\|", data)
    assert not re.search(r"\|<span style='font-size:20px'>\*\*(\d{1,2}|\d+\.\d{3})\*\*</span>\|", data)
    assert not re.search(r"\|<span style='font-size:20px'>\*\*(\d{1,2}|\d+\.\d{1})\*\*</span>\|", data)
    assert result.exit_code == 0
    assert result.output == ""


@responses.activate
def test_main_with_invalid_precision(rasa_path):
    utils.load_mock_payloads()
    runner = CliRunner()
    result = runner.invoke(main, ["--path", rasa_path, "--precision", "6"])
    assert not os.path.isfile("model_report.md")
    assert result.exit_code == 2
    assert result.output == "Usage: main [OPTIONS]\n\n" \
        "Error: Invalid value for '--precision': 6 is not in the range 0<=x<=5.\n"


def test_main_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert result.output
