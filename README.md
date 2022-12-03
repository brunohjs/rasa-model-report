<div align="center">
<h1>Rasa Model Report</h1>
<img
    height="180"
    alt="logo"
    src="docs/images/logo.png"
/>
<h4>Simple Rasa add-on command-line that generates training model health reports for your projects.</h4>
<br />
<!-- [**Read The Docs**](https://testing-library.com/react) | -->
<!-- [Edit the docs](https://github.com/testing-library/testing-library-docs) -->
<br />
</div>
<hr />


<!-- Badges -->
![Python version](https://img.shields.io/static/v1?label=python&message=v3.10&color=3776AB)
![Code coverage](https://img.shields.io/static/v1?label=coverage&message=100%&color=success)
![Apache 2.0 License](https://img.shields.io/static/v1?label=license&message=Apache%202.0&color=yellowgreen)
![Contributors](https://img.shields.io/github/contributors/brunohjs/rasa-model-report)
<!--  -->


## 📦 Installation

This module is distributed via [Pypi](https://pypi.org/) and is required to use **Python v3.10** or higher. To install the package, use the command:
```
pip install rasa-model-report
```

## 🚀 Execution
Before anything, is necessary to have the reports generated by the `rasa test` command. To run the program, use the command:
```
rasa-model-report
```
This command must be used in the root of your Rasa project. Otherwise, you can use `--path` parameter to pass the project path.

## ⚙️ Options
Available options are below:

|Parameter|Description|Type|
|-|-|-|
|`--path`|Rasa project path. (default: ./)|string|
|`--output-path`|Report output path. (default: ./)|string|
|`--project`|Rasa project name. It's only displayed in the report. (default: My project)|string|
|`--version`|Rasa project version. It's only displayed in the report for project versioning. (default: not-identified)|string|
|`--rasa-api`|Rasa API URL. Is needed to create NLU section of report. (default: http://localhost:5005)|string|
|`--disable-nlu`|Disable NLU section of report.|-|
|`--help`|Show help message.|-|


## 🐞 Bugs
Please file an issue for bugs, missing documentation, or unexpected behavior.

[See open issues](https://github.com/brunohjs/rasa-model-report/issues?q=is%3Aopen+is%3Aissue+label%3Abug)


## 💬 Discussions
Please file an issue to suggest new features. Vote on feature requests. This helps maintainers prioritize what to work on.

[See new ideas discussion](https://github.com/brunohjs/rasa-model-report/discussions/categories/ideas)


## ❓ Questions
For questions related to using the add-on, please ask the community on Q&A.

[See Q&A](https://github.com/brunohjs/rasa-model-report/discussions/categories/q-a)
