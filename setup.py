from setuptools import setup

setup(
    name="Rasa Model Report",
    version="1.0.0",
    author="Bruno Justo",
    author_email="brunohjs@gmail.com",
    license="Apache 2.0",
    packages=["rasa_model_report", "rasa_model_report.controllers", "rasa_model_report.helpers"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        rasa-model-report=rasa_model_report.main:main
    """,
)
