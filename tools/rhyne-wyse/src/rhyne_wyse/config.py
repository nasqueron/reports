#   -------------------------------------------------------------
#   Rhyne-Wise :: Config
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Parse YAML configuration
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import yaml


DEFAULT_CONFIG_PATH = "conf/rhyne-wyse.yaml"
DEFAULT_HASHES_PATH = "/var/db/rhyne-wyse/hashes"


def get_config_path():
    return DEFAULT_CONFIG_PATH


def get_config():
    with open(get_config_path()) as config_file:
        return yaml.load(config_file, Loader=yaml.Loader)


def get_hashes_path():
    return DEFAULT_HASHES_PATH
