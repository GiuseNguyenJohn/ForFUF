#!/usr/bin/python3

import unittest
import forfuf
import re
text_for_test_parsing = """
ExifTool Version Number         : 12.40
File Name                       : cat.jpg
Directory                       : .
File Size                       : 1017 KiB
File Modification Date/Time     : 2022:02:11 13:14:59-08:00
File Access Date/Time           : 2022:02:11 13:14:59-08:00
File Inode Change Date/Time     : 2022:02:11 13:14:59-08:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 100
Y Resolution                    : 100
Current IPTC Digest             : 0def9dc9a98ce8bc8abdd7b2c54c23f2
Copyright Notice                : picoctf{1337}
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 12.40
Rights                          : copyright
Image Width                     : 2370
Image Height                    : 1927
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 2370x1927
Megapixels                      : 4.6
"""

class ForfufTestCase(unittest.TestCase):
    """Tests for 'forfuf.py'."""

    def test_check_file_exists(self):
        """Will filename 'test.png' (exists) return True?"""
        file_exists = forfuf.check_file_exists('cat.jpg')
        self.assertEqual(file_exists, True)

    def test_get_regex_flag_format(self):
        """Will input 'picoctf\{.*\}' return correct match object?"""
        match_object = forfuf.get_regex_flag_format(r"picoctf\{.*\}")
        correct_match_object = re.compile(r"picoctf\{.*\}|cvpbpgs\{.*\}")
        self.assertEqual(match_object, correct_match_object)

    def test_parse_for_possible_flags(self):
        """Will match object and exif data input return flag?"""
        match_object = forfuf.get_regex_flag_format(r"picoctf\{.*\}")
        correct_flag = "picoctf{1337}"
        found_flag = forfuf.parse_for_possible_flags(match_object, text_for_test_parsing)
        self.assertIn(correct_flag, found_flag)

if __name__ == '__main__':
    unittest.main()