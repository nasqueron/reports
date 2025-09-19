#   -------------------------------------------------------------
#   Secretsmith :: Vault :: KV secrets engine - version 2
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------

import unittest
from unittest.mock import MagicMock

from secretsmith.vault.secrets import *


class TestReadSecret(unittest.TestCase):
    def setUp(self):
        self.mock_client = MagicMock()

        secret_mock = MagicMock(return_value=self.mock_kv2_secret())
        self.mock_client.secrets.kv.read_secret_version = secret_mock

    @staticmethod
    def mock_kv2_secret():
        return {
            "data": {
                "data": {
                    "username": "someuser",
                    "password": "somepass",
                },
                "metadata": {
                    "created_time": "2021-01-01T00:00:00.000000Z",
                    "deletion_time": "",
                    "destroyed": False,
                    "version": 1,
                    "custom_metadata": {"owner": "someone"},
                },
            }
        }

    def test_read_secret(self):
        result = read_secret(self.mock_client, "test_mount", "test_path")

        expected = {"username": "someuser", "password": "somepass"}
        self.assertEqual(expected, result)

    def test_read_secret_empty_data(self):
        self.mock_client.secrets.kv.read_secret_version.return_value = {
            "data": {"data": {}}
        }

        result = read_secret(self.mock_client, "test_mount", "empty_data_path")

        self.assertEqual({}, result)

    def test_read_secret_with_metadata_(self):
        result_data, result_metadata = read_secret_with_metadata(
            self.mock_client, "test_mount", "test_path"
        )
        expected_data = {"username": "someuser", "password": "somepass"}
        expected_metadata = {
            "created_time": "2021-01-01T00:00:00.000000Z",
            "deletion_time": "",
            "destroyed": False,
            "version": 1,
            "custom_metadata": {"owner": "someone"},
        }
        self.assertEqual(expected_data, result_data)
        self.assertEqual(expected_metadata, result_metadata)

    def test_read_secret_with_custom_metadata(self):
        result_data, result_metadata = read_secret_with_custom_metadata(
            self.mock_client, "test_mount", "test_path"
        )
        expected_data = {"username": "someuser", "password": "somepass"}
        expected_metadata = {
            "created_time": "2021-01-01T00:00:00.000000Z",
            "deletion_time": "",
            "destroyed": False,
            "version": 1,
            "owner": "someone",
        }
        self.assertEqual(expected_data, result_data)
        self.assertEqual(expected_metadata, result_metadata)

    def test_get_username(self):
        result = get_username(self.mock_client, "test_mount", "test_path")
        self.assertEqual("someuser", result)

    def test_get_password(self):
        result = get_password(self.mock_client, "test_mount", "test_path")
        self.assertEqual("somepass", result)

    def test_get_field(self):
        result = get_field(self.mock_client, "test_mount", "test_path", "username")
        self.assertEqual("someuser", result)


if __name__ == "__main__":
    unittest.main()
