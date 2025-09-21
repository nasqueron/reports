#   -------------------------------------------------------------
#   Secretsmith :: Vault :: Client
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import os
import unittest
import tempfile

from secretsmith.vault.client import resolve_token


class TestResolveToken(unittest.TestCase):
    def test_empty_config_returns_none(self):
        result = resolve_token({})

        self.assertIsNone(result)

    def test_resolve_token_from_file(self):
        token_content = "s.test-file-token"

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            # Extra whitespaces ensure the token is correctly stripped
            temp_file.write(token_content + "\n  ")

        try:
            config_auth = {"tokenfile": temp_file.name}
            result = resolve_token(config_auth)

            self.assertEqual(token_content, result)
        finally:
            os.unlink(temp_file.name)

    def test_resolve_token_from_config(self):
        config_auth = {"token": "s.0000"}
        result = resolve_token(config_auth)

        self.assertEqual("s.0000", result)


if __name__ == "__main__":
    unittest.main()
