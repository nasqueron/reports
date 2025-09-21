#   -------------------------------------------------------------
#   Secretsmith :: Vault :: Client
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import unittest
from unittest.mock import Mock, patch

from secretsmith.vault.client import from_config


class TestFromConfig(unittest.TestCase):
    @patch("secretsmith.vault.client.Client")
    @patch("secretsmith.vault.client.login_with_approle")
    def test_from_config_approle_method(self, mock_login_approle, mock_client):
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance

        config = {
            "server": {"url": "https://vault.domain.tld"},
            "auth": {
                "method": "approle",
                "role_id": "00000000-0000-0000-0000-000000000000",
                "secret_id": "00000000-0000-0000-0000-000000000000",
            },
        }
        from_config(config)

        mock_login_approle.assert_called_once_with(mock_client_instance, config["auth"])

    @patch("secretsmith.vault.client.Client")
    def test_from_config_token_method(self, mock_client):
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance

        config = {
            "server": {"url": "https://vault.domain.tld"},
            "auth": {"method": "token", "token": "s.test-token"},
        }
        from_config(config)

        mock_client.assert_called_once_with(
            url="https://vault.domain.tld",
            token="s.test-token",
            verify=None,
            namespace=None,
        )

    @patch("secretsmith.vault.client.Client")
    def test_from_config_unknown_method_raises_error(self, mock_client):
        """Test that an unknown authentication method raises ValueError"""
        mock_client_instance = Mock()
        mock_client.return_value = mock_client_instance

        config = {"auth": {"method": "notexisting"}}

        self.assertRaises(ValueError, from_config, config)


if __name__ == "__main__":
    unittest.main()
