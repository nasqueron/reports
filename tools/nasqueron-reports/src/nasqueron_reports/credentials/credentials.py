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


def resolve_credentials(full_config, credentials_config):
    if credentials_config["driver"] == "vault":
        vault_config = full_config.get("vault", {})
        return vault.fetch_credentials(vault_config, credentials_config["secret"])

    if credentials_config["driver"] == "env":
        variables = credentials_config.get("variables", {})
        return read_environment(variables)

    raise NasqueronReportConfigError("Credentials driver parameter is missing")


#   -------------------------------------------------------------
#   Environment
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def read_environment(variables):
    return {k: os.environ.get(v, "") for k, v in variables.items()}
