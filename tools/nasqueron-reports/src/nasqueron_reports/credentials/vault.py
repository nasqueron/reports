#   -------------------------------------------------------------
#   Nasqueron Reports :: Credentials :: Vault
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Read credentials from Vault or OpenBao
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


from secretsmith.vault.client import from_config as client_from_config
from secretsmith.vault.secrets import read_secret
from secretsmith.vault.utils import split_path


def fetch_credentials(vault_config, full_secret_path):
    vault_client = client_from_config(vault_config)

    mount_point, secret_path = split_path(full_secret_path)
    return read_secret(vault_client, mount_point, secret_path)
