import os.path

import responses
from click.testing import CliRunner

from rasa_model_report.main import main
from tests import utils


@responses.activate
def test_main_with_valid_path(rasa_path):
    runner = CliRunner()
    result = runner.invoke(main, ["--path", rasa_path])
    assert os.path.isfile("model_report.md")
    assert result.exit_code == 0
    assert result.output == ""


@responses.activate
def test_main_with_invalid_path():
    utils.load_mock_payloads()
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert not os.path.isfile("model_report.md")
    assert result.exit_code == 0
    assert result.output == ""
