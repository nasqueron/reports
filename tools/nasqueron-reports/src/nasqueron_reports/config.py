#   -------------------------------------------------------------
#   Nasqueron Reports :: Config
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Reports configuration
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import os

import yaml

from nasqueron_reports.credentials import vault
from nasqueron_reports.errors import NasqueronReportConfigError


#   -------------------------------------------------------------
#   Configuration paths
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


DEFAULT_CONFIG_PATHS = [
    "conf/reports.yaml",
    ".reports.yaml",
    "/usr/local/etc/reports.yaml",
    "/etc/reports.yaml",
]


DEFAULT_SQL_PATHS = [
    ".",
    "/usr/local/share/nasqueron-reports",
    "/usr/share/nasqueron-reports"
]


def get_config_path():
    for config_path in DEFAULT_CONFIG_PATHS:
        if os.path.exists(config_path):
            return config_path

    return None


def resolve_sql_path(sql_path):
    for sql_directory in DEFAULT_SQL_PATHS:
        full_path = os.path.join(sql_directory, sql_path)
        if os.path.exists(full_path):
            return full_path

    return sql_path


#   -------------------------------------------------------------
#   Main configuration
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def get_config():
    config_path = get_config_path()

    if not config_path:
        raise NasqueronReportConfigError("You need to create a reports.yaml config file")

    with open(config_path) as fd:
        config = yaml.safe_load(fd)

    return config


#   -------------------------------------------------------------
#   Report configuration
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def inject_service_config(config, report_config):
    try:
        service_name = report_config["service"]
    except KeyError:
        raise NasqueronReportConfigError(
            f"Service parameter missing in report configuration"
        )

    try:
        report_config["service_options"] = config["services"][service_name]
    except KeyError:
        raise NasqueronReportConfigError(
            f"Service not declared in configuration: {service_name}"
        )

    if "credentials" in report_config["service_options"]:
        secret_path = report_config["service_options"]["credentials"]
        credentials = vault.fetch_credentials(secret_path)
    else:
        credentials = {}

    report_config["service_options"]["credentials"] = credentials


def parse_report_config(report_name):
    config = get_config()

    try:
        report_config = config["reports"][report_name]
    except KeyError:
        raise NasqueronReportConfigError(f"Report not found: {report_name}")

    inject_service_config(config, report_config)

    return report_config
