# Contributing Guide
Contributing to `rasa-model-report` is fairly easy. This document shows you how to get the project, run all provided tests and generate a production-ready build.

It also covers provided grunt tasks that help you develop with `rasa-model-report`.


## 📦 Installation
For development, it's suggested to create an environment using the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation). To create new environment, use the command:
```
mkvirtualenv rasa-model-report --python 3.8
```
After that, your new environment will already be activated. If not, to activate just use the command:
```
workon rasa-model-report
```

To install the development environment, use *make* command:
```
make install-dev
```
or use `pip install`:
```
pip install . -r requirements.dev.txt
```

### Pre-commit
Pre-commit is a important tool that helps maintain project code and commit patterns. To configure in your local machine, use these commands:
```
pip install pre-commit
pre-commit install
pre-commit install --hook-type commit-msg
```


## 🧪 Testing
Before test any changes you've made, you need to install the package again to update package files. Use the command:
```
pip install .
```
After that, you can test using `rasa-model-report` command with or without parameters.

To run unit tests, use:
```
make test
```
or
```
pytest
```
At the end, the coverage report will be displayed.

To run linter, use:
```
flake8
```


## 📝 Contributing/Submitting changes
- Check out a new branch based on `main` and name it with issue ID:
    ```
    git checkout -b BRANCH_NAME origin/main
    ```
    - Example:

        This [issue](https://github.com/brunohjs/rasa-model-report/issues/57) have ID `57`, so, the branch name is `#57`.

    If you get an error, you may need to fetch `main` first by using:
    ```
    git remote update && git fetch
    ```
  - Use one branch per fix/feature

- Make your changes
  - Make sure to create unit tests for new code.
  - Make sure to check if have failing tests.
  - Make sure to check if have 100% code coverage.
  - When all tests pass and have 100% code coverage, everything's fine. 😉
- Commit your changes
  - This project uses a code pattern defined by `pre-commit`, so please make sure your commits follow the conventions.
    - To configure `pre-commit`, read above. It will help you with your commits and code patterns.
    - Commit message patterns is: `[issue_id] - [message]`
      - Example:
        - `57 - Update README.md file`
        - `123 - Change the test variable value`
        - `29 - Fix name_example() function`
  - Don't forget to update the [CHANGELOG.md](CHANGELOG.md) file. Follow the conventions described on file.
  - Please provide a git message that explains what you've done.
  - Commit to the forked repository.
- Make a pull request
  - Make sure you send the PR to the `main` branch.
  - Use pull request template correctly.
  - Wait for the review.

If you follow these instructions, your PR will land pretty safely in the main repo!
