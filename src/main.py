import logging

import click
from controllers.ModelReport import ModelReport

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
    "--output-dir",
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
    "--disable-nlu",
    is_flag=True,
    required=False,
    default=False,
    help="Disable NLU section of report. (default: false)"
)
def main(path, output_dir, project, version, disable_nlu):
    """
    Description
    """
    report = ModelReport(path, output_dir, project, version, disable_nlu=disable_nlu)
    return report


if __name__ == '__main__':
    main()
