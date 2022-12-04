from setuptools import setup

setup(
    name="rasa-model-report",
    version="1.0.0",
    author="Bruno Justo",
    author_email="brunohjs@gmail.com",
    license="Apache 2.0",
    description="Simple open-source Rasa command-line add-on that "
                "generates training model health reports for your projects.",
    python_requires=">=3.10",
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
