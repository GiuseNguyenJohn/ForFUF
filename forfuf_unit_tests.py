import unittest
import forfuf

class ForfufTestCase(unittest.TestCase):
    """Tests for 'forfuf.py'."""

    def test_check_file_exists(self):
        """Will filename 'test.png' (exists) return True?"""
        file_exists = forfuf.check_file_exists('test.png')
        self.assertEqual(file_exists, True)

if __name__ = '__main__':
    unittest.main()