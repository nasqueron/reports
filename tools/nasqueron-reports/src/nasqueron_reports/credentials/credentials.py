#   -------------------------------------------------------------
#   Nasqueron Reports :: Credentials :: Vault
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Read credentials from Vault or OpenBao
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import os

from nasqueron_reports.credentials import vault
from nasqueron_reports.errors import NasqueronReportConfigError


#   -------------------------------------------------------------
#   Credentials wiring
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def resolve_credentials(config):
    if config["driver"] == "vault":
        return vault.fetch_credentials(config["secret"])

    if config["driver"] == "env":
        variables = config.get("variables", {})
        return read_environment(variables)

    raise NasqueronReportConfigError("Credentials driver parameter is missing")


#   -------------------------------------------------------------
#   Environment
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def read_environment(variables):
    return {k:os.environ.get(v, "") for k, v in variables.items()}
