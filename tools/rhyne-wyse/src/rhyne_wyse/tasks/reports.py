#   -------------------------------------------------------------
#   Rhyne-Wyse :: Tasks :: Reports
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from typing import Dict

import requests
import yaml

from nasqueron_reports.actions.reports import generate_report
from nasqueron_reports.config import parse_report_config

from rhyne_wyse.wiki.page import get_page_age
from rhyne_wyse.utils.hashes import *


#   -------------------------------------------------------------
#   Main tasks
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def prepare_report(report_options: Dict) -> Report:
    if report_options["tool"] == "nasqueron-reports":
        return generate_nasqueron_report(report_options)
    elif report_options["tool"] == "fetch":
        return fetch_report(report_options)

    raise ValueError("Unknown report tool: " + report_options["tool"])


def needs_report_update(site, page_title, report: Report, tweaks: List) -> bool:
    to_update = False
    report_hash = ""

    # Do not eagerly return True, as we need to update the hash either

    if "update-at-least-monthly" in tweaks:
        age = get_page_age(site, page_title)
        if age > 30:
            to_update = True

    if "compute-hash-ignoring-date" in tweaks:
        report_hash = compute_hash_ignoring_date(report)
    elif "compute-hash-first-column" in tweaks:
        report_hash = compute_hash_from_first_column(report)

    if report_hash is not None:
        current_hash = read_hash_from_datastore(page_title)
        if current_hash != report_hash:
            to_update = True
            write_hash_to_datastore(page_title, report_hash)

    return to_update


#   -------------------------------------------------------------
#   Call Nasqueron Reports to generate a report
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def parse_nasqueron_report_config(report_options):
    tool_options = report_options.get("tool_options", {})
    vault_credentials = tool_options.get("vault_credentials", None)

    if vault_credentials is not None:
        try:
            with open(vault_credentials) as fd:
                return {
                    "vault": yaml.safe_load(fd),
                }
        except PermissionError:
            # Allow running the bot under a user account too
            pass

    return {}


def generate_nasqueron_report(report_options):
    extra_config = parse_nasqueron_report_config(report_options)
    report_config = parse_report_config(report_options["report"], extra_config)

    return generate_report(report_config)


#   -------------------------------------------------------------
#   Fetch an already generated report from a specific URL
#
#   For reports configured with `tool: fetch`
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def fetch_report(report_options) -> Report:
    url = report_options["tool_options"]["url"]

    response = requests.get(url)
    response.raise_for_status()

    return Report(None, response.text)
