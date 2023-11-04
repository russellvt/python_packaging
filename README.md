# Python Packaging and Workflows

![PyLint](https://github.com/russellvt/python_packaging/actions/workflows/pylint.yml/badge.svg)
![Python](https://github.com/russellvt/python_packaging/actions/workflows/python-app.yml/badge.svg)

Tests and Examples of Python Packaging and Automation


## Environmental Setup
Initial environmental setup. This only needs to be done once.

    python3 -m venv venv-packaging
    . ./venv-packaging/bin/activate
    pip install build pip setuptools wheel --upgrade


## Github Workflows
Getting GitHub Actions / Workflows to work.

### Pylint
You should be using `pylint` within your IDE even prior to commit.
GitHub also delivers this workflow in an automated fashion.


## References
References used during the creation and development of this module.

* [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [GitHub Status Badges](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)
