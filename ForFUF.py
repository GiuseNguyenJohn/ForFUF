"""
Name: John Nguyen
Contributor: Matt Sprengel
Description: Automates basic checks for CTF forensics challenges
Dependecies: binwalk, exiftool, hexdump, zsteg, strings, steghide
Tested: Python 3.9.6 on GNU/Linux
"""

"""
Ideas:
- write unit tests for each function/class
- Questions:
    - grep for flag, or parse with python?
    - how to format output? files? stdout?
    - how to check for run with sudo? uid? $USER env var?
- automatic flag detection?
- run 'file' linux tool to determine type of file
- check and fix corrupt file headers
- check LSB steg with zsteg
- extract strings and search for flag
- use regex to identify when flag characters are all grouped together within
    a certain range (ex. C.T.F.{.F.L.A.G.} )
"""

"""
TODO:
- Add one-liner in README to install all dependencies in bash
- Add function to check if given file exists
- use try/except to figure out if file exists
- Make argparser to parse:
    - infile
    - outfile
    - flag format
    - fake flag format?
    - 'all' option
    - individual checks only:
        - embedded files
        - metadata
        - LSB encoding
        - 
"""

from argparse import ArgumentParser
import os
from os.path import exists
from os import popen
from os import getcwd
from os import getuid

class NotSudo(Exception):
    pass

class FileClass:
    """
    A class to describe a given file. Includes binwalk check for
    embedded files.
    """

    def __init__(self, filename):
        self.filename = filename
        self.file_description = ''

def check_sudo():
    """Check if program is being run as root."""

    if os.getuid() != 0:
        raise NotSudo("This program is not being run with sudo permissions.")

def check_file_exists(filename):
    """Check that the given file exists."""

    if exists(filename):
        return True
    if exists(os.join(getcwd(),filename)):
        return True
    return False

def check_setup(filename):
    """Make sure program is run as root and given file exists."""

    check_sudo()
    if not check_file_exists(filename):
        print(f"File {filename} not found!")
        exit(1)

parser = ArgumentParser(description="A command-line tool for"
                                    "to automate basic checks"
                                    "for CTF forensics challenges")
