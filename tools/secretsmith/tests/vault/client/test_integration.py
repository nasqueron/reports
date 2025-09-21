#   -------------------------------------------------------------
#   Secretsmith :: Vault :: Client
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import os
import unittest
from unittest.mock import patch, Mock

from secretsmith.vault.client import from_config


class TestIntegration(unittest.TestCase):
    @patch("secretsmith.vault.client.Client")
    def test_full_config_with_all_options(self, mock_client):
        config = {
            "server": {
                "url": "https://vault.domain.tld",
                "verify": "/path/to/ca.crt",
                "namespace": "test-namespace",
            },
            "auth": {
                "method": "token",
                "token": "s.full-test-token",
            },
        }
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance

        from_config(config)
        mock_client.assert_called_once_with(
            url="https://vault.domain.tld",
            token="s.full-test-token",
            verify="/path/to/ca.crt",
            namespace="test-namespace",
        )

    @patch("secretsmith.vault.client.Client")
    def test_empty_config(self, mock_client):
        from_config({})

        with patch.dict(os.environ, {}, clear=True):
            mock_client.assert_called_once_with(
                url=None,
                token=None,
                verify=None,
                namespace=None,
            )


if __name__ == "__main__":
    unittest.main()
