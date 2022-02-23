#!/usr/bin/python3

"""
Author: John Nguyen (@Magicks52)
Contributors: Matt Sprengel (@ItWasDNS), David Nam (@DavidTimothyNam)
Description: Automates basic checks for CTF forensics challenges
Dependecies: binwalk, digital invisible ink toolkit, exiftool, strings,
            steghide, stegsolve, unzip, xxd, zsteg
Tested: Python 3.9 on Kali Linux
"""

import base64
import binascii
import codecs
import magic
import re
from argparse import ArgumentParser
from os.path import exists
from os import popen, getuid, remove

ascii_art = """
 ________ ________  ________  ________ ___  ___  ________ 
|\  _____\\\\   __  \|\   __  \|\  _____\\\\  \|\  \|\  _____\\
\ \  \__/\ \  \|\  \ \  \|\  \ \  \__/\ \  \\\\\  \ \  \__/ 
 \ \   __\\\\ \  \\\\\  \ \   _  _\ \   __\\\\ \  \\\\\  \ \   __\\
  \ \  \_| \ \  \\\\\  \ \  \\\\  \\\\ \  \_| \ \  \\\\\  \ \  \_|
   \ \__\   \ \_______\ \__\\\\ _\\\\ \__\   \ \_______\ \__\\ 
    \|__|    \|_______|\|__|\|__|\|__|    \|_______|\|__| 
"""

def append_to_log(section_title, text):
    """Append given heading and text to 'forfuf_log.txt'."""
    with open('forfuf_log.txt', 'a') as f:
        # Format of heading should be like '===== [ Title Case ] ====='
        heading = section_title.center(70, '=')
        f.write(heading.replace(section_title, f' [ {section_title.title()} ] '))
        # Write text followed by one blank line
        f.write(f'\n{text}\n\n')

def auto_create_regex_string(crib):
    """Use the crib to create the regex string"""
    crib = crib.strip("{")
    regex_string = ""
    for character in crib:
        regex_string += character
        regex_string += ".{0,2}"
    regex_string += "\\{.*?\\}"
    return regex_string

def check_sudo():
    """Check if program is being run as root."""
    # Raise error if not run with uid 0 (root)
    if getuid() != 0:
        print("This program is not being run with sudo permissions.")
        exit(1)

def clear_log():
    """Deletes log file if it exists."""
    try:
        remove('forfuf_log.txt')
    except:
        pass

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
    base64_pattern = re.compile(f"{base64_first_three[0:3]}[+\\\\A-Za-z0-9]+[=]{{0,2}}\s")
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

def run_diit():
    """Run Digital Invisible Ink Toolkit from /bin/diit."""
    popen('/bin/diit')

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

    def handle_jpg_and_jpeg(self):
        """Runs all applicable checks on jpg/jpeg file."""
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
        if ask_stegsolve.lower() == 'y' or ask_stegsolve.lower() == 'yes':
            run_stegsolve()
        # If input is 'y' or 'yes', run diit
        ask_diit = input('Run Digital Ink Invisible Tookit? (y/n)')
        if ask_diit.lower() == 'y' or ask_diit.lower() == 'yes':
            run_diit()
            
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
        exit(0)

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
    # check if uid is 0
    check_sudo()
    # clear logfile
    print("Clearing log...")
    clear_log()
    # create argument parser
    parser = ArgumentParser(description="A command-line tool for"
                                        "to automate basic checks"
                                        "for CTF forensics challenges")
    parser.add_argument('filename', type=str, help='file to analyze')
    parser.add_argument('-f', '--flag-format', type=str, help='regex flag pattern')
    parser.add_argument('-p', '--password', type=str, help='password for steghide')
    parser.add_argument('-c', '--crib', type=str, help='crib of flag (ex. "picoctf")')
    args = parser.parse_args()
    # try to create instance of FileClass
    try:
        file = FileClass(args.filename, args.password if args.password else None)
    except FileNotFoundError:
        print(f"No such file: '{args.filename}'")
    # check if file is a zip
    if 'zip archive' in file.file_description.lower():
        print("ZIP archive detected.")
        file.handle_zip()
    # check if file is a jpg/jpeg
    elif 'jpg' in file.file_description.lower() or 'jpeg' in file.file_description.lower():
        print("JPG/JPEG file detected.")
        file.handle_jpg_and_jpeg()
    # check if file is png/bmp
    elif 'png' in file.file_description.lower() or 'bmp' in file.file_description.lower():
        print("PNG/BMP file detected.")
        file.handle_png_and_bmp()
    # check for corrupt header
    elif file.file_description.lower() == 'data':
        file.handle_corrupt_header()
    # check if file is a valid file format, but unsupported
    else:
        print(f"File description: {file.file_description}")
        print("File format not supported.")
        exit(1)
    # Find flag in log if at least --crib is specified
    if args.crib:
        # Create regex string
        regex_string = auto_create_regex_string(args.crib)
        if args.flag_format:
            regex_string = args.flag_format
        # Create flag match objects
        plain_mo, rot13_mo, base64_mo = get_regex_flag_formats(regex_string, args.crib)
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
                print(f'Possible base64 flag: {flag}')
                print(f"\tDECODED: {base64.b64decode(bytes(flag, 'utf-8')).decode()}")
        if not (plaintext_flags or rot13_flags or base64_flags):
            print("No flags found.")
    else:
        print("--flag-format (-f) or --crib (-c) not specified.")
        exit(0)

if __name__ == '__main__':
    main()