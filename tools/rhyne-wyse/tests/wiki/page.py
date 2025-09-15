#   -------------------------------------------------------------
#   Rhyne-Wise :: Tests :: Wiki :: Page
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import unittest

from rhyne_wyse.wiki.page import replace_between_markers


class PageTest(unittest.TestCase):
    def test_replace_between_markers(self):
        current = """The tree is:
[TREE]
Fir
[/TREE]
"""

        expected = """The tree is:
[TREE]
Abies Electronicus
[/TREE]
"""

        actual = replace_between_markers(
            current,
            "[TREE]",
            "[/TREE]",
            "Abies Electronicus",
        )

        self.assertEqual(expected, actual)

    def test_replace_between_markers_when_missing(self):
        self.assertRaises(
            ValueError,
            replace_between_markers,
            "The tree is: Fir",
            "[TREE]",
            "[/TREE]",
            "Abies Electronicus",
        )


if __name__ == "__main__":
    unittest.main()
