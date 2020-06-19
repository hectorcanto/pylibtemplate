import json
import logging
import sys
from os.path import join, abspath, dirname


def set_logger(disable=('parso', 'urllib3')):
    """
    Set the logger to Debug and standard out, specially useful for scripts and prototyping.
    """
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    for logger_namespace in disable:
        # Remove debugging from too verbose log namespaces
        other = logging.getLogger(logger_namespace)
        other.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)


def load_json_fixture(current_file, filename):
    """
    :param current_file:  usually __file__, to compute the relative route of the fixture folder
    :param filename: the full name of a JSON file with extension
    :returns: a Python object, usually a dict or list
    """
    route = join(abspath(dirname(current_file), "fixtures", filename))
    with open(route) as buf:
        fixture = json.load(buf)
    return fixture
