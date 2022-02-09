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

def check_file_permission(filename):
    """Check that the user has correct permissions to supplied file."""
    if exists(os.join(getcwd(),))

class FileClass:
    """
    A class to describe a given file. Includes binwalk check for
    embedded files.
    """

    def __init__(self, filename):
        self.filename = filename
        
        self.file_description = 