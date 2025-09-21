#   -------------------------------------------------------------
#   Secretsmith :: Vault :: Client
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import os
import unittest
from unittest.mock import patch

from secretsmith.vault.client import resolve_namespace


class TestResolveNamespace(unittest.TestCase):
    """Test the resolve_namespace function"""

    def test_resolve_namespace_from_config(self):
        config = {"namespace": "quux"}
        result = resolve_namespace(config)

        self.assertEqual("quux", result)

    def test_resolve_namespace_from_environment(self):
        config = {}
        os.environ["VAULT_NAMESPACE"] = "quux"

        result = resolve_namespace(config)
        self.assertEqual("quux", result)

    def test_resolve_namespace_config_overrides_environment(self):
        config = {"namespace": "config-namespace"}
        os.environ["VAULT_NAMESPACE"] = "env-namespace"

        result = resolve_namespace(config)
        self.assertEqual("config-namespace", result)

    def test_resolve_namespace_no_config_no_env_returns_none(self):
        config = {}

        with patch.dict(os.environ, {}, clear=True):
            result = resolve_namespace(config)
            self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
