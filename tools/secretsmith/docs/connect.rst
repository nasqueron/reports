===========================
Connect to Vault or OpenBao
===========================

Code is minimalist
==================

As everything happen in the application configuration file,
your code needs two things:

- get the path of your configuration file
- invoke secretsmith.login()

.. code-block:: python

  import secretsmith

  VAULT_CONFIG_PATH = "/path/to/config.yaml"

  vault_client = secretsmith.login(config_path=VAULT_CONFIG_PATH)

You'll then get a hvac.Client object and can call any hvac method on it.

Configuration file
==================

Introduction
------------

Secretsmith uses a YAML configuration file to determine the login parameters:

.. code-block:: yaml

  vault:
    server:
      url: https://127.0.0.1:8200
    auth:
      token: hvs.000000000000000000000000

When using AppRole, the configuration file will look like:

.. code-block:: yaml

    vault:
      server:
        url: https://127.0.0.1:8200
        verify: /path/to/ca.pem
      auth:
        method: approle
        role_id: e5a7b66e-5d08-da9c-7075-71984634b882
        secret_id: 841771dc-11c9-bbc7-bcac-6a3945a69cd9

The format is based on the Vault execution module for SaltStack.

Global parameters
-----------------

The following parameters are supported:

- ``server`` — a block to specify the Vault or OpenBao server parameters

  - ``url`` — the URL
  - ``verify`` — the path to a CA certificate to verify the server's certificate
  - ``namespace`` — the namespace to use (by default, will follow environment)

- ``auth`` — a block to specify the authentication method and parameters

  - ``method`` — what authentication backend to use, by default ``token``

Additional parameters are supported in the ``auth`` block depending
on the authentication method.

Token authentication method
----------------------------

When the method is ``token``, the following additional parameters are supported:

- ``token`` — the token to use
- ``token_file`` — alternatively, the path to a file containing the token

AppRole authentication method
-----------------------------

When the method is ``approle``, the following additional parameters are supported:

- ``role_id`` — the AppRole role ID (required)
- ``secret_id`` — the AppRole secret ID (optional)
