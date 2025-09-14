#   -------------------------------------------------------------
#   Nasqueron Reports :: Actions :: Reports
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Generate a report
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from nasqueron_reports import Report
from nasqueron_reports.connectors import db_mysql
from nasqueron_reports.formats import mediawiki
from nasqueron_reports.errors import *


#   -------------------------------------------------------------
#   Action
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def generate_report(report_config):
    connector_cb, format_cb = wire(report_config)

    # Fetch the data for the report
    report = Report()
    report.raw.headers, report.raw.rows = connector_cb(report_config)

    # Format
    format_options = report_config["format_options"]
    report.formatted = format_cb(report.raw, format_options)

    return report


#   -------------------------------------------------------------
#   Wiring
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


CONNECTORS_MAP = {
    "MariaDB": db_mysql.fetch_report,
    "MySQL": db_mysql.fetch_report,
}


FORMATS_MAP = {
    "mediawiki": mediawiki.to_table,
}


def wire(report_config):
    if "connector" not in report_config["service_options"]:
        service_name = report_config["service"]
        raise NasqueronReportConfigError(f"Service connector missing in configuration for service {service_name}")

    if "format" not in report_config:
        raise NasqueronReportConfigError(f"Format missing in report configuration")

    report_connector = report_config["service_options"]["connector"]
    if report_connector not in CONNECTORS_MAP:
        raise NasqueronReportConfigError(f"Unknown connector: {report_connector}")

    report_format = report_config["format"]
    if report_format not in FORMATS_MAP:
        raise NasqueronReportConfigError(f"Unknown format: {report_format}")

    return CONNECTORS_MAP[report_connector], FORMATS_MAP[report_format]
