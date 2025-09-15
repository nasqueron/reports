#!/usr/bin/env python3

#   -------------------------------------------------------------
#   Rhyne-Wise :: Credentials :: Vault
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Fetch credentials from Vault
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from typing import Dict

import hvac


VAULT_CA_CERTIFICATE = "/usr/local/share/certs/nasqueron-vault-ca.crt"


def connect_to_vault():
    return hvac.Client(
        verify=VAULT_CA_CERTIFICATE,
    )


def read_secret(
    vault_client, mount_point: str, prefix: str, key: str
) -> Dict[str, str]:
    secret = vault_client.secrets.kv.read_secret_version(
        mount_point=mount_point,
        path=prefix + "/" + key,
    )
    return secret["data"]["data"]


def read_app_secret(vault_client, key: str) -> Dict[str, str]:
    return read_secret(vault_client, "apps", "rhyne-wyse", key)
