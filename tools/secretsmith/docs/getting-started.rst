================================
Getting started with secretsmith
================================

Installation
============
The secretsmith package is available on PyPI:

.. code-block:: shell

   $ pip install secretsmith

We suggest you add the package in a requirements.txt file:

.. code-block:: text

   secretsmith~=0.1.0

How to use in code?
===================

Call ``secretsmith.login()`` with the path to the configuration file:

.. code-block:: python

  import secretsmith

  VAULT_CONFIG_PATH = "/path/to/config.yaml"

  vault_client = secretsmith.login(config_path=VAULT_CONFIG_PATH)

Then, you can use the client as a hvac library Vault client.

We provide helper methods for common tasks, but you can also directly use hvac.

See :doc:`connect` for the configuration file format.
