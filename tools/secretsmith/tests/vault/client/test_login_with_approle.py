#   -------------------------------------------------------------
#   Secretsmith :: Vault :: Client
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import unittest
from unittest.mock import Mock

from secretsmith.vault.client import login_with_approle


class TestLoginWithApprole(unittest.TestCase):

    def test_login_with_approle_success(self):
        mock_client = Mock()
        config_auth = {"role_id": "test-role-id", "secret_id": "test-secret-id"}

        login_with_approle(mock_client, config_auth)
        mock_client.auth.approle.login.assert_called_once_with(
            role_id="test-role-id", secret_id="test-secret-id"
        )

    def test_login_with_approle_no_secret_id(self):
        mock_client = Mock()
        config_auth = {"role_id": "test-role-id"}

        login_with_approle(mock_client, config_auth)
        mock_client.auth.approle.login.assert_called_once_with(
            role_id="test-role-id", secret_id=None
        )

    def test_login_with_approle_missing_role_id_raises_error(self):
        mock_client = Mock()
        config_auth = {"secret_id": "test-secret-id"}

        self.assertRaises(ValueError, login_with_approle, mock_client, config_auth)


if __name__ == "__main__":
    unittest.main()
