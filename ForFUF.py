"""
Name: John Nguyen
Contributor: Matt Sprengel
Description: Automates basic checks for CTF forensics challenges
Dependecies: binwalk, exiftool, hexdump, zsteg, strings
Tested: Python 3.9.6 on GNU/Linux
"""

"""
Ideas:
- Questions:
    - grep for flag, or parse with python?
    - how to format output? files? stdout?
- automatic flag detection?
- check and fix corrupt file headers
- check LSB steg with zsteg
- extract strings and search for flag
- use regex to identify when flag characters are all grouped together within
    a certain range
"""

"""
TODO:
- Add one-liner in README to install all dependencies in bash
-  
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