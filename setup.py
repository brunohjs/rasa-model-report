from pathlib import Path

from setuptools import setup


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="rasa-model-report",
    version="1.0.0",
    author="Bruno Justo",
    author_email="brunohjs@gmail.com",
    license="Apache 2.0",
    description="Simple open-source Rasa command-line add-on that "
                "generates training model health reports for your projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    url="https://github.com/brunohjs/rasa-model-report",
    packages=[
        "src.rasa_model_report",
        "src.rasa_model_report.controllers",
        "src.rasa_model_report.helpers"
    ],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        rasa-model-report=src.rasa_model_report.main:main
    """,
)
