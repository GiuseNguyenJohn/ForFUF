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
Resolution Unit                 : 
X Resolution                    : 100
Y Resolution                    : 100
Current IPTC Digest             : 0def9dc9a98ce8bc8abdd7b2c54c23f2
Copyright Notice                : picoCTF{1337} 
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 12.40
Rights                          : cvpbPGS{1337} 
Image Width                     : 2370
Image Height                    : 1927
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : cGljb0NURnsxMzM3fQ== 
Color Components                : .p.i.c.o.C.T.F.{.f.l.a.g.}.
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 2370x1927
Megapixels                      : 4.6
"""

class ForfufTestCase(unittest.TestCase):
    """Tests for 'forfuf.py'."""

    def test_check_file_exists(self):
        """Will filename 'exiftool_base64.jpg' (it exists) return True?"""
        file_exists = forfuf.check_file_exists('exiftool_base64.jpg')
        self.assertEqual(file_exists, True)

    def test_parse_for_possible_flags(self):
        """Will --flag-format and --start-flag return correct flags?"""
        plaintext_mo, rot_13_mo, base64_mo = forfuf.get_regex_flag_formats("p.{0,2}i.{0,2}c"
                ".{0,2}o.{0,2}C.{0,2}T.{0,2}F.{0,2}{.*}", "picoCTF{")
        # correct flags
        correct_plaintext_flag = "picoCTF{1337}"
        correct_range_flag = "p.i.c.o.C.T.F.{.f.l.a.g.}"
        correct_rot_13_flag = ["cvpbPGS{1337}"]
        correct_base64_flag = ["cGljb0NURnsxMzM3fQ== "] # space at the end because regex will match space too
        # found flags
        plaintext_flags = forfuf.parse_for_possible_flags(plaintext_mo, text_for_test_parsing)
        rot_13_flags = forfuf.parse_for_possible_flags(rot_13_mo, text_for_test_parsing)
        base64_flags = forfuf.parse_for_possible_flags(base64_mo, text_for_test_parsing)
        # compare found flags to correct ones
        self.assertEquals(correct_plaintext_flag, plaintext_flags[0])
        self.assertEquals(correct_range_flag, plaintext_flags[1])
        self.assertEquals(correct_rot_13_flag, rot_13_flags)
        self.assertEquals(correct_base64_flag, base64_flags)

if __name__ == '__main__':
    unittest.main()