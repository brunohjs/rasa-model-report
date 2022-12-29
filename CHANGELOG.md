# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.1.0] - 2022-12-28
### Added
- [#31](https://github.com/brunohjs/rasa-model-report/issues/30) Support for python version 3.8 or higher.
- [#38](https://github.com/brunohjs/rasa-model-report/issues/38) Created `--version` CLI command. This command shows installed **rasa-model-report** version.
- [#15](https://github.com/brunohjs/rasa-model-report/issues/15) Created `--rasa-version` CLI command. This command is used to inform the Rasa version that will be displayed in the report.
- [#15](https://github.com/brunohjs/rasa-model-report/issues/15) Added `-p` to abbreviate `--path` parameter.
- [#18](https://github.com/brunohjs/rasa-model-report/issues/18) Created repository social media preview.

### Changed
- [#15](https://github.com/brunohjs/rasa-model-report/issues/15) Changed CLI parameters to be clearer:
  - `--project` to `--project-name`.
  - `--version` to `--project-version` (this parameter was duplicated).

## [1.0.1] - 2022-12-13
### Added
- [#30](https://github.com/brunohjs/rasa-model-report/issues/30) Added more badges to README.md.

### Fixed
- [#32](https://github.com/brunohjs/rasa-model-report/issues/32) Fixed module not found error.


## [1.0.0] - 2022-12-10
### Added
- [#1](https://github.com/brunohjs/rasa-model-report/issues/1) Created command `rasa-model-report` for the command-line.
- [#2](https://github.com/brunohjs/rasa-model-report/issues/2) Repository creation and initial setup.
- [#3](https://github.com/brunohjs/rasa-model-report/issues/3) Created the README.md and CHANGELOG.md file.
- [#5](https://github.com/brunohjs/rasa-model-report/issues/5) Created unit test and the automation on GitHub action.
  - The automation will execute the tests every time a PR is opened.

### Fixed
- [#16](https://github.com/brunohjs/rasa-model-report/issues/16) Created a handler for retrieval intents in the report.


<!-- [1.1.0]: https://github.com/brunohjs/rasa-model-report/compare/1.1.0...HEAD -->
[1.1.0]: https://github.com/brunohjs/rasa-model-report/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/brunohjs/rasa-model-report/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/brunohjs/rasa-model-report/releases/tag/1.0.0
