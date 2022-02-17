#!/usr/bin/python3

"""
Name: John Nguyen
Contributors: Matt Sprengel
Description: Automates basic checks for CTF forensics challenges
Dependecies: cat, binwalk, exiftool, strings, steghide, stegsolve, unzip, xxd, zsteg
Tested: Python 3.9 on Kali Linux
"""

import base64
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
   \ \__\   \ \_______\ \__\\\\ _\\\\ \__\   \ \_______\ \__\\ 
    \|__|    \|_______|\|__|\|__|\|__|    \|_______|\|__| 
"""


class NotSudo(Exception):
    pass

def check_sudo():
    """Check if program is being run as root."""
    # Raise error if not run with uid 0 (root)
    if getuid() != 0:
        raise NotSudo("This program is not being run with sudo permissions.")

def append_to_log(section_title, text):
    """Append given heading and text to 'forfuf_log.txt'."""
    with open('forfuf_log.txt', 'a') as f:
        # Format of heading should be like '===== [ Title Case ] ====='
        heading = section_title.center(70, '=')
        f.write(heading.replace(section_title, f' [ {section_title.title()} ] '))
        # Write text followed by one blank line
        f.write(f'\n{text}\n\n')

def check_file_exists(filepath):
    """Check that the given file exists."""
    # We know the program is being run as root, so if an error is returned,
    # we know the filepath doesn't exist.
    if not exists(filepath):
        print(f'"{filepath}" not found!')
        exit(1)
    else:
        return True

def get_formatted_log():
    """Return log stripped of all newline characters."""
    with open('forfuf_log.txt', 'r') as f:
        return f.read().replace('\n', ' ')

def get_regex_flag_formats(regex_string, start_flag):
    """Takes a string and returns plaintext, rot13, and base64 match objects."""
    # Pattern of plaintext, rot13, and base64
    plaintext_pattern = re.compile(regex_string)
    rot13_pattern = re.compile(codecs.encode(regex_string, 'rot-13'))
    base64_first_three = base64.b64encode(bytes(start_flag, 'utf-8')).decode()
    base64_pattern = re.compile(f"{base64_first_three[0:3]}[+\A-Za-z0-9]+[=]{{0,2}}\s")
    return plaintext_pattern, rot13_pattern, base64_pattern

def parse_for_possible_flags(match_object, text):
    """
    Uses regex object from 'get_regex_flag_formats' to search
    text for flag pattern
    """
    # Get list of possible flags and return the list
    possible_flags = match_object.findall(text)
    return possible_flags

def read_file_header(filename):
	"""Print neatly formatted first few bytes of file."""
	output = popen(f'xxd -p {filename}').read(50)
	formatted_bytes = ' '.join(output[x:x+2] for x in range(0, len(output), 2))
	print("Header is probably corrupt - the first few bytes"
            f"of '{filename}' are: {formatted_bytes}")

def run_binwalk(filename):
    """Attempts to extract hidden files with 'binwalk -Me FILENAME'."""
    cmd = f"binwalk -Me --run-as=root {filename}" # '-M' for 'matryoshka'
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

def run_stegsolve():
    """Run stegsolve from /bin/stegsolve."""
    popen('/bin/stegsolve')

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

def run_unzip(filename):
    """Tries to unzip file, either password protected or not."""
    output = popen(f'unzip {filename}')
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

    def __init__(self, filename, password=None):
        self.filename = filename
        self.file_description = magic.from_file(filename)
        self.password = password

    def check_setup(self):
        """
        Exits with error code 1 if not ran with sudo or
        if given file doesn't exist.
        """
        check_sudo()
        check_file_exists(self.filename)

    def handle_jpg_and_jpeg(self):
        """Runs all applicable checks on jpg/jpeg file."""
        # cat (broken for now)
        # print('Running cat...')
        # append_to_log('cat', run_cat(self.filename))
        # strings
        print('Running strings...')
        append_to_log('strings', run_strings(self.filename))
        # exiftool
        print('Running exiftool...')
        append_to_log('exiftool', run_exiftool(self.filename))
        # binwalk
        print('Running binwalk...')
        append_to_log('binwalk', run_binwalk(self.filename))
        # steghide
        print('Running steghide...')
        if self.password:
            append_to_log('steghide', run_steghide_extract(self.filename, self.password))
        else:
            append_to_log('steghide', run_steghide_extract(self.filename))
        # If input is 'y' or 'yes', run stegsolve
        ask_stegsolve = input('Run stegsolve? (y/n)')
        if ask_stegsolve.lower() == 'y' or 'yes':
            run_stegsolve()
        else:
            exit(0)             
    
    def handle_png_and_bmp(self):
        """Runs all applicable checks on png/bmp file."""
        # zsteg
        print('Running zsteg...')
        append_to_log('zsteg', run_zsteg(self.filename))
        # run same checks for jpg/jpeg
        self.handle_jpg_and_jpeg()
    
    def handle_zip(self):
        """Tries to unzip file, alerts user if zip is password protected."""
        # unzip
        print(f'Unzipping {self.filename}...')
        unzip_output = run_unzip(self.filename)
        append_to_log('unzip', unzip_output)
        if 'password' in unzip_output:
            print(f'{self.filename} is password protected!')
        exit(1)

    def handle_corrupt_header(self):
        """
        Asks for file header as user input, then either creates
        a copy with new header or does nothing.
        """
        read_file_header(self.filename)
        ask_fix_header = input('Input new file header as hex string'
                                'here, or "n" to do nothing: ')
        if ask_fix_header.lower() != 'n':
            print(f'Fixing file header of {self.filename}...')
            write_file_header(self.filename, ask_fix_header)
        exit(0)

def main():
    print(ascii_art)
    parser = ArgumentParser(description="A command-line tool for"
                                        "to automate basic checks"
                                        "for CTF forensics challenges")
    parser.add_argument('filename', type=str, help='file to analyze')
    parser.add_argument('-f', '--flag-format', type=str, help='regex flag pattern')
    parser.add_argument('-p', '--password', type=str, help='password for steghide')
    parser.add_argument('-s', '--start-flag', type=str, help='prefix of flag (ex. "picoctf{")')
    args = parser.parse_args()
    # Create instance of FileClass
    file = FileClass(args.filename, args.password if args.password else None)
    # Check if setup is good to go
    file.check_setup()
    # Determine which checks to run
    if 'zip archive' in file.file_description.lower(): # check if file is a zip
        file.handle_zip()
    elif 'jpg' or 'jpeg' in file.file_description.lower(): # check if file is jpg/jpeg
        file.handle_jpg_and_jpeg()
    elif 'png' or 'bmp' in file.file_description.lower(): # check if file is png/bmp
        file.handle_png_and_bmp()
    elif 'data' in file.file_description.lower(): # check for corrupt header
        file.handle_corrupt_header()
    else:
        print(f"File description: {file.file_description}")
        print("File format not supported.")
        exit(1)
    # Find flag in log if --flag-format is specified
    if args.flag_format and args.start_flag:
        # Create flag match objects
        plain_mo, rot13_mo, base64_mo = get_regex_flag_formats(args.flag_format, args.start_flag)
        # Parse log file 'forfuf_log.txt' for matching flags
        log_text = get_formatted_log()
        plaintext_flags = parse_for_possible_flags(plain_mo, log_text)
        rot13_flags = parse_for_possible_flags(rot13_mo, log_text)
        base64_flags = parse_for_possible_flags(base64_mo, log_text)
        # print flags
        if plaintext_flags:
            for flag in plaintext_flags:
                print(f'Possible plaintext flag: {flag}')
        if rot13_flags:
            for flag in rot13_flags:
                print(f'Possible rot13 flag: {flag}')
                print(f"\tDECODED: {codecs.decode(flag, 'rot-13')}")
        if base64_flags:
            for flag in base64_flags:
                # make base64 flag a multiple of 4
                
                # print base64 flag
                breakpoint()
                print(f'Possible base64 flag: {flag}')
                print(f"\tDECODED: {base64.b64decode(bytes(flag, 'utf-8'))}")
        if not (plaintext_flags or rot13_flags or base64_flags):
            print("No flags found.")
    else:
        print("No flag format specified.")
        exit(0)

if __name__ == '__main__':
    main()