# Introduction

This is a Cookiecutter template to create a python library.
 
# Usage

After cloning the project:

~~~bash
cookiecutter pylibtemplate
~~~

Directly from Github:

~~~
cookiecutter https://github.com/hectorcanto/pylibtemplate
~~~

Replace all the options with your own choices. To understand and help the choices check
config.yml.j2 for instructions and help.

Alternatively, produce a custom config based on config.yml.j2.

~~~bash
jinja2 config.yml.template > config.yml
cookiecutter --config-file config.yml template_deploy
~~~

If there is an existing folder you can overwrite/extend it using _replay_option_:

~~~bash
cookiecutter --replay pylibtemplate
~~~
