FROM python:{{cookiecutter.python_docker}}

WORKDIR /opt/{{cookiecutter.libname}}
RUN apk add make build-base git
RUN apk del sqlite
COPY requirements/ requirements/
RUN pip install -r requirements/dev.txt

COPY . /opt/{{cookiecutter.libname}}
