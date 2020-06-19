GREEN="\\e[32m"
REGULAR="\\e[39m"
RED="\\e[91m"

VERSION=$(shell cat {{cookiecutter.libname}}/__init__.py | grep __version | head -n 1 | cut -d" " -f 3| tr -d "'")

clean-py:
	find . -name '__pycache__' -exec rm -fr {}

clean-build:
	@rm -rf *.egg-info .sonar .scannerwork build dist .pytest_cache

build:
	docker build -t {{cookiecutter.libname}}:dev .

silent-build:
	@docker build -q -t {{cookiecutter.libname}}:dev .

flake:
	@ flake8 \
	&& echo -e "${GREEN}Passed Flake8 style review.${REGULAR}" \
	|| (echo -e "${RED}Flake8 style review failed.${REGULAR}" ; exit 1)

flake-docker: silent-build
	@docker run {{cookiecutter.libname}}:dev flake8 \
	&& echo "${GREEN}Passed Flake8 style review.${REGULAR}" \
	|| (echo "${RED}Flake8 style review failed.${REGULAR}" ; exit 1)

linting:
	@pylint --rcfile=setup.cfg {{cookiecutter.libname}}/ tests/ | tee .coverage-reports/pylint.txt

version-bump:
	@python -c 'from {{cookiecutter.libname}} import __version__; print("Previous version:", __version__)'
	@bumpversion --allow-dirty minor
	@python -c 'from {{cookiecutter.libname}} import __version__; print("New version:", __version__)'

show-version:
	@echo ${VERSION}

new-version-check:
	@git ls-remote --exit-code --tags origin $VERSION && echo "Version ${VERSION} already exists!" || echo "Version ${VERSION} is new. OK.";

vulnerabilities-check:
	@safety check --full-report

sonar-scan:
	@sed -i -e "s,<source>.*,<source>/usr/src/{{cookiecutter.libname}}/</source>,g" .coverage-reports/coverage.xml
	docker run -v "${PWD}:/usr/src" --user="$(shell id -u):$(shell id -g)" sonarsource/sonar-scanner-cli

docker-scan:
	docker run -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy {{cookiecutter.libname}}:dev

.PHONY: clean-py clean-build build silent-build flake flake-docker linting version-bump \
        show-version new-version-check vulnerabilities-check sonar-scan docker-scan

