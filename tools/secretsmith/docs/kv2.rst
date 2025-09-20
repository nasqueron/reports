========================================
Interact with key/value v2 secret engine
========================================

Querying secrets
================

Secrets are usually stored in a kv2 secret engine.

As hvac syntax can be particularly verbose for those operations,
secretsmith also provides helper methods for more common use cases.

All examples assume you have already obtained a logged-in client with
``secretsmith.login()`` and then import the helpers::

    from secretsmith.vault import secrets

The examples assume you want to query in the ``secret`` mounting point the  ``app/db`` secret path.
Replace ``secret`` by your own kv2 mounting point when different.

read_secret
-----------

**Goal**:
Read a secret from kv2 and return only the secret data as a dictionary.
This is the simplest helper to fetch all key/value pairs stored at a path.

**Example**::

    secret = secrets.read_secret(vault_client, "secret", "app/db")
    print(secret["username"])

read_secret_with_metadata
-------------------------

**Goal**:
Read a secret from kv2 and return **both the data and the metadata**.
Metadata includes information such as version number, timestamps, etc.

**Example**::

    data, metadata = secrets.read_secret_with_metadata(vault_client, "secret", "app/db")
    print("User:", data["username"])
    print("Secret created at:", metadata["created_time"])
    print("Secret version:", metadata["version"])

If you've custom metadata, those are available in ``metadata["custom_metadata"]``.

read_secret_with_custom_metadata
--------------------------------

**Goal**:
Like ``read_secret_with_metadata``, but also merges **custom metadata**
fields directly into the returned metadata dictionary. This is useful if
you add annotations to your secrets.

**Example**::

    data, metadata = secrets.read_secret_with_custom_metadata(vault_client, "secret", "app/db")
    print("User:", data["username"])
    if "owner" in metadata:
        print("Secret owner:", metadata["owner"])

get_username
------------

**Goal**:
Return the ``username`` field from a secret, raising an error if it is
missing. This is a straightforward design choice for cases where you
don't want to deal with a full dictionary of values.

**Example**::

    user = secrets.get_username(vault_client, "secret", "app/db")
    print("Username:", user)

get_password
------------

**Goal**:
Return the ``password`` field from a secret, raising an error if it is
missing.

**Example**::

    password = secrets.get_password(vault_client, "secret", "app/db")

get_field
---------

**Goal**:
Return a specific field from a secret. This is the generic helper that
``get_username`` and ``get_password`` build upon. Raises a ``ValueError``
if the requested field does not exist.

**Use case**:
When you use a secret to store API keys and tokens, chances are you only
have one field, to query only this field as a string is straightforward.

**Example**::

    api_key = secrets.get_field(vault_client, "secret", "app/service", "api-key")

hvac
====

You can still directly use hvac. The helper methods are only provided as sugar syntax.
