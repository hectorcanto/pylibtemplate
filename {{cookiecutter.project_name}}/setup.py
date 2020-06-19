from setuptools import setup, find_packages
from install_requires import convert
from codecs import open
from os import path
from {{cookiecutter.libname}} import __version__


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='{{cookiecutter.libname}}',
    version=__version__,
    description='',  # TODO
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',  # TODO
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='',  # TODO
    install_requires=convert('requirements.txt', 'setup.py')[0],
    dependency_links=[],
    author_email=''  # TODO
)
