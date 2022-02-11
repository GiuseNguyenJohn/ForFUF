#!/usr/bin/python3

"""
Name: John Nguyen
Contributors: Matt Sprengel
Description: Automates basic checks for CTF forensics challenges
Dependecies: binwalk, exiftool, hexdump, zsteg, strings, steghide
Tested: Python 3.9 on Kali Linux
"""

import codecs
import re
from argparse import ArgumentParser
from os.path import exists
from os import popen, getcwd, getuid


ascii_art = """
 ________ ________  ________  ________ ___  ___  ________ 
|\  _____\\\\   __  \|\   __  \|\  _____\\\\  \|\  \|\  _____\\
\ \  \__/\ \  \|\  \ \  \|\  \ \  \__/\ \  \\\\\  \ \  \__/ 
 \ \   __\\\\ \  \\\\\  \ \   _  _\ \   __\\\\ \  \\\\\  \ \   __\\
  \ \  \_| \ \  \\\\\  \ \  \\\\  \\\\ \  \_| \ \  \\\\\  \ \  \_|
   \ \__\   \ \_______\ \__\\\\ _\\\\ \__\   \ \_______\ \__\ 
    \|__|    \|_______|\|__|\|__|\|__|    \|_______|\|__| 
"""


class NotSudo(Exception):
    pass

def check_sudo():
    """Check if program is being run as root."""
    # Raise error if not run with uid 0 (root)
    if getuid() != 0:
        raise NotSudo("This program is not being run with sudo permissions.")

def check_file_exists(filepath):
    """Check that the given file exists."""
    # We know the program is being run as root, so if an error is returned,
    # we know the filepath doesn't exist.
    if exists(filepath):
        return True
    else:
        return False

def get_regex_flag_format(regex_string):
    """Takes a string and returns a match object"""
    # Pattern of plaintext AND rot13 flag format
    pattern = f"{regex_string}|{codecs.encode(regex_string, 'rot13')"
    match_object = re.compile(pattern)
    return match_object

def parse_for_possible_flags(match_object, text):
    """
    Uses regex object from 'get_regex_flag_format' to search
    text for flag pattern
    """
    # Get list of possible flags and return the list
    possible_flags = match_object.findall(text)
    return possible_flags

class FileClass:
    """
    A class to describe a given file. Includes steghide check with blank password.
    """

    def __init__(self, filename):
        self.filename = filename
        self.file_description = ''


def main():
    print(ascii_art)
    parser = ArgumentParser(description="A command-line tool for"
                                        "to automate basic checks"
                                        "for CTF forensics challenges")
    parser.add_argument('--flag-format', type=str, help='regex pattern for flag')
    args = parser.parse_args()

if __name__ == '__main__':
    main()