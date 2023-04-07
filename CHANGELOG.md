# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.3] - 2023-04-06
### Added
- [#63](https://github.com/brunohjs/rasa-model-report/issues/63) Created `--precision` CLI command parameter. This command is used to change precision of the model report overview grades.
### Fixed
- [#66](https://github.com/brunohjs/rasa-model-report/issues/63) Fixed error when empty NLU file was analyzed NLU analyzer.

## [1.3.2] - 2023-02-26
### Added
- [#26](https://github.com/brunohjs/rasa-model-report/issues/26) Updated release script.
  - Now, it can create release and close milestone on Github automatically.
  - Added docstrings in functions.
- [#57](https://github.com/brunohjs/rasa-model-report/issues/57) Created and updated documentations.
  - Created templates for bug report, feature request and pull request.
  - Created contributing documentation.
  - Updated sample reports.
### Fixed
- [#60](https://github.com/brunohjs/rasa-model-report/issues/60) Bugfix on E2E coverage results that shows incorrect coverage rate value when aren't covered elements.

## [1.3.1] - 2023-02-24
### Fixed
- [#52](https://github.com/brunohjs/rasa-model-report/issues/52) Fixed E2E coverage report not extracting entities correctly.
- [#54](https://github.com/brunohjs/rasa-model-report/issues/54) Fixed broken images paths from report when the output path parameter is informed.

## [1.3.0] - 2023-02-21
### Added
- [#42](https://github.com/brunohjs/rasa-model-report/issues/42) Created `--no-images` CLI command parameter. This command is used to not show images in the report.
- [#49](https://github.com/brunohjs/rasa-model-report/issues/49) Created `--actions-path` CLI command parameter, to inform actions path. In addition, end-to-end coverage can now identify utters or actions that are inside actions code.


## [1.2.0] - 2023-01-28
### Added
- [#43](https://github.com/brunohjs/rasa-model-report/issues/43) End-to-end coverage feature.
- [#46](https://github.com/brunohjs/rasa-model-report/issues/46) Created `--model-link` CLI command parameter. This command is used to inform the model link that will be displayed in the report to download.

### Changed
- [#33](https://github.com/brunohjs/rasa-model-report/issues/33) Change response section title to `Core`.


## [1.1.0] - 2022-12-28
### Added
- [#15](https://github.com/brunohjs/rasa-model-report/issues/15) Added `-p` to abbreviate `--path` parameter.
- [#15](https://github.com/brunohjs/rasa-model-report/issues/15) Created `--rasa-version` CLI command parameter. This command is used to inform the Rasa version that will be displayed in the report.
- [#18](https://github.com/brunohjs/rasa-model-report/issues/18) Created repository social media preview.
- [#31](https://github.com/brunohjs/rasa-model-report/issues/30) Support for python version 3.8 or higher.
- [#38](https://github.com/brunohjs/rasa-model-report/issues/38) Created `--version` CLI command parameter. This command shows installed **rasa-model-report** version.

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

[1.3.3]: https://github.com/brunohjs/rasa-model-report/compare/1.3.2...1.3.3
[1.3.2]: https://github.com/brunohjs/rasa-model-report/compare/1.3.0...1.3.2
[1.3.1]: https://github.com/brunohjs/rasa-model-report/compare/1.3.0...1.3.1
[1.3.0]: https://github.com/brunohjs/rasa-model-report/compare/1.2.0...1.3.0
[1.2.0]: https://github.com/brunohjs/rasa-model-report/compare/1.1.0...1.2.0
[1.1.0]: https://github.com/brunohjs/rasa-model-report/compare/1.0.1...1.1.0
[1.0.1]: https://github.com/brunohjs/rasa-model-report/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/brunohjs/rasa-model-report/releases/tag/1.0.0
