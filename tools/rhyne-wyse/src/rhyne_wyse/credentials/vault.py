#!/usr/bin/env python3

#   -------------------------------------------------------------
#   Rhyne-Wyse :: Credentials :: Vault
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Fetch credentials from Vault
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from typing import Dict

import secretsmith
from secretsmith.vault.secrets import read_secret


def read_app_secret(config: Dict[str, str]) -> Dict[str, str]:
    config_path = config.get("vault_credentials", None)

    try:
        vault_client = secretsmith.login(config_path)
    except PermissionError:
        # Allow running the bot under a user account too
        vault_client = secretsmith.login()

    return read_secret(vault_client, config["mount_point"], config["secret_path"])
