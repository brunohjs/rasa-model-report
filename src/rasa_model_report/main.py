import logging

import click

from src.rasa_model_report.controllers.model_report import ModelReport

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)


@click.command()
@click.option(
    "--path",
    type=str,
    required=False,
    default="./",
    help="Rasa project path. (default: ./)"
)
@click.option(
    "--output-path",
    type=str,
    required=False,
    default="./",
    help="Report output path. (default: ./)"
)
@click.option(
    "--project",
    type=str,
    required=False,
    default="My Project",
    help="Rasa project name. It's only displayed in the report. (default: My project)"
)
@click.option(
    "--version",
    type=str,
    required=False,
    default=None,
    help="Rasa project version. It's only displayed in the report for project versioning. (default: not-identified)"
)
@click.option(
    "--rasa-api",
    type=str,
    required=False,
    default="http://localhost:5005",
    help="Rasa API URL. Is needed to create NLU section of report. (default: http://localhost:5005)"
)
@click.option(
    "--disable-nlu",
    is_flag=True,
    required=False,
    default=False,
    help="Disable processing NLU sentences. NLU section will not be generated "
    "in the report. Required Rasa API. (default: false)"
)
@click.help_option(
    "-h",
    "--help",
    help="Show this help message."
)
def main(path, output_path, project, version, rasa_api, disable_nlu):
    """
    Simple add-on that generates training model health reports for your Rasa projects. 📈🔍🧾🤖🧠
    """
    report = ModelReport(path, output_path, project, version, disable_nlu=disable_nlu, rasa_api_url=rasa_api)
    return report
