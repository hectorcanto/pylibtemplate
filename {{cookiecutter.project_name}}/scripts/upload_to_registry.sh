#!/usr/bin/env bash
echo "Pushing '{{cookiecutter.display_name}}' to Pypi registry"
pip install twine install_requires
python setup.py sdist bdist_wheel
twine upload --verbose -u "$PYPI_USERNAME" -p "$PYPI_PASSWORD" --repository-url "$REPO_URL" dist/*
