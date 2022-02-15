#!/usr/bin/python3

"""
Name: John Nguyen
Contributors: Matt Sprengel
Description: Automates basic checks for CTF forensics challenges
Dependecies: binwalk, exiftool, zsteg, strings, steghide, xxd
Tested: Python 3.9 on Kali Linux
"""

import binascii
import codecs
import magic
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

def append_to_log(text):
    """Take text and append it to log, then append newline and many “=”s."""
    with open('forfuf_log.txt', 'a') as f:
        f.write(text + "\n==========================")

def check_file_exists(filepath):
    """Check that the given file exists."""
    # We know the program is being run as root, so if an error is returned,
    # we know the filepath doesn't exist.
    if not exists(filepath):
        print(f'"{filepath}" not found!')
        exit(1)
    else:
        return True

def get_regex_flag_format(regex_string):
    """Takes a string and returns a match object"""
    # Pattern of plaintext AND rot13 flag format
    pattern = f"{regex_string}|{codecs.encode(regex_string, 'rot13')}"
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

def read_file_header(filename):
	"""Print neatly formatted first few bytes of file."""
	output = popen(f'xxd -p {filename}').read(50)
	formatted_bytes = ' '.join(output[x:x+2] for x in range(0, len(output), 2))
	print(f"The first few bytes of '{filename}' are: {formatted_bytes}")

def run_binwalk(filename):
    """Attempts to extract hidden files with 'binwalk -Me FILENAME'."""
    cmd = f"binwalk -Me {filename}" # '-M' for 'matryoshka'
    output = popen(cmd)
    return output.read() # Return output

def run_cat(filename):
    """Dumps ascii representation of data with 'cat FILENAME'."""
    cmd = f"cat {filename}"
    output = popen(cmd)
    return output.read() # Return output

def run_exiftool(filename):
    """Gets metadata with 'exiftool FILENAME'."""
    cmd = f"exiftool {filename}"
    output = popen(cmd)
    return output.read() # Return output

def run_steghide_extract(filename, password="''"):
    """Extracts using 'steghide extract -sf FILENAME -p PASSPHRASE'."""
    # Steghide command
    cmd = f"steghide extract -sf {filename} -p {password}"
    output = popen(cmd)
    return output.read() # Return output

def run_strings(filename):
    """Dump strings found in file with 'strings FILENAME'."""
    cmd = f"strings {filename}"
    output = popen(cmd)
    return output.read() # Return output

def run_zsteg(filename):
    """Checks for LSB encoding with 'zsteg -a FILENAME'."""
    cmd = f"zsteg -a {filename}"
    output = popen(cmd)
    return output.read() # Return output

def write_file_header(filename, file_header):
	"""
	Takes string of hex and substitutes it in the hex data of
	the given file, then writes hex data to new file called
	'fixed_FILENAME'.
	"""
	# store plain hex of file, excluding the first few bytes
	rest_of_file = popen(f"xxd -p -s {len(file_header) // 2} {filename}").read().replace('\n','')
	with open(f'fixed_{filename}', 'wb') as f:
		fixed_file = binascii.unhexlify(file_header + rest_of_file)
		f.write(fixed_file) # write to new file

class FileClass:
    """
    A class to describe a given file.
    """

    def __init__(self, filename):
        self.filename = filename
        self.file_description = magic.from_file(filename)

    def check_setup(self):
        check_sudo()
        check_file_exists(self.filename)

    def handle_png_and_bmp(self):
        """Runs all applicable checks on png/bmp file."""

def main():
    print(ascii_art)
    parser = ArgumentParser(description="A command-line tool for"
                                        "to automate basic checks"
                                        "for CTF forensics challenges")
    parser.add_argument('--flag-format', type=str, help='regex flag pattern')
    parser.add_argument
    args = parser.parse_args()

if __name__ == '__main__':
    main()