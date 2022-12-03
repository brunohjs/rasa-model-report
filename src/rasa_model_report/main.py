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
    help="Rasa path. (default: ./)"
)
@click.option(
    "--output-path",
    type=str,
    required=False,
    default="./",
    help="Report output directory. (default: ./)"
)
@click.option(
    "--project",
    type=str,
    required=False,
    default="My Project",
    help="Rasa project name. (default: My project)"
)
@click.option(
    "--version",
    type=str,
    required=False,
    default=None,
    help="Rasa project version. (default: not identified)"
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
    help="Disable NLU section of report. (default: false)"
)
def main(path, output_path, project, version, rasa_api, disable_nlu):
    """
    Description
    """
    report = ModelReport(path, output_path, project, version, disable_nlu=disable_nlu, rasa_api_url=rasa_api)
    return report
