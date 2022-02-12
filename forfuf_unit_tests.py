#!/usr/bin/python3

import unittest
import forfuf
import re

class ForfufTestCase(unittest.TestCase):
    """Tests for 'forfuf.py'."""

    def test_check_file_exists(self):
        """Will filename 'test.png' (exists) return True?"""
        file_exists = forfuf.check_file_exists('test.png')
        self.assertEqual(file_exists, True)

    def test_get_regex_flag_format(self):
        """Will input 'picoctf\{.*\}' return correct match object?"""
        match_object = forfuf.get_regex_flag_format(r"picoctf\\{.*\\}")
        correct_match_object = re.compile(r"picoctf\{.*\}|cvpbpgs\{.*\}")
        self.assertEqual(match_object, correct_match_object)

if __name__ == '__main__':
    unittest.main()