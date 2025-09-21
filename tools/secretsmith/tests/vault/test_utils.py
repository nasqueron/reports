#   -------------------------------------------------------------
#   Secretsmith :: Vault :: Utilities
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import unittest

from secretsmith.vault.utils import split_path


class TestUtils(unittest.TestCase):

    def test_split_path_basic(self):
        full_path = "mount/secret/path/to/data"
        expected = ("mount", "secret/path/to/data")

        self.assertEqual(expected, split_path(full_path))

    def test_split_path_no_secret_path(self):
        full_path = "mount"
        expected = ("mount", "")

        self.assertEqual(expected, split_path(full_path))

    def test_split_path_leading_slash(self):
        full_path = "/mount/secret/path"
        expected = ("", "mount/secret/path")

        self.assertEqual(expected, split_path(full_path))

    def test_split_path_trailing_slash(self):
        full_path = "mount/secret/"
        expected = ("mount", "secret/")

        self.assertEqual(expected, split_path(full_path))

    def test_split_path_empty_string(self):
        full_path = ""
        expected = ("", "")

        self.assertEqual(expected, split_path(full_path))


if __name__ == "__main__":
    unittest.main()
