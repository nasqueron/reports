#   -------------------------------------------------------------
#   Nasqueron Reports :: Credentials :: Vault
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Read credentials from Vault or OpenBao
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import hvac


VAULT_CA_CERTIFICATE = "/usr/local/share/certs/nasqueron-vault-ca.crt"


def fetch_credentials(secret_path):
    vault_client = hvac.Client(
        verify=VAULT_CA_CERTIFICATE,
    )

    tokens = secret_path.split("/")
    secret_mount = tokens[0]
    secret_path = "/".join(tokens[1:])

    secret = vault_client.secrets.kv.read_secret_version(
        mount_point=secret_mount,
        path=secret_path,
        raise_on_deleted_version=True,
    )

    return secret["data"]["data"]
