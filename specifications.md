## SPECIFICATIONS:
Forfuf will be a Linux command-line tool to automate the running of 
most standard tools used in CTF steganograpy and forensics. The general
flow of the program involves:

1. checking if forfuf is ran with sudo
2. checking that the file specified exists
3. deleting the log file if it exists
4. determining the filetype
5. running all applicable checks for the filetype and appending all data
    from checks to logfile ('forfuf_log.txt')
6. parsing the logfile for flags (automatic detection for flag in plaintext,
    rot13, and base64) if --flag-format and --start-flag is specified
7. outputting flags to stdout

The only required argument is the FILENAME; optional arguments include:

- flag format in regex
- flag prefix for the purpose of detecting base64
- password for steghide; if not specified, defaults to blank password

### Checks for filetypes:

If the file is a ZIP archive, Forfuf should:
- attempt to unzip the archive
- tell if the zipfile is password protected

If the file is a JPG/JPEG, Forfuf should:
- check strings output
- check cat output (see TODO)
- check exiftool output
- attempt to extract with binwalk
- attempt to extract with steghide
- ask to run stegsolve

If the file is a PNG/BMP, Forfuf should:
- run all the checks for JPG/JPEG's
- check zsteg output

If the header is corrupt (detected by the word 'data' at the beginning), forfuf should:
- output neatly formatted first few bytes of file
- take optional new file header as a string of hex and 
    make new file with patched file header

### Style Guide:
This style guide that should be referenced for this project is PEP 8,
so important guidelines to keep in mind are:

- put imports at the beginning of file
- lines less than 80 characters long
- use four spaces, no tabs
- use docstrings at the beginning of functions and classes

## TODO:
- [x] Add one-liner in README to install all dependencies in bash
- [x] check if program ran with sudo
- [x] check if given file exists
- [x] store flag format, return match object (plaintext, rot13, base64)
- [x] get a file's magic bytes
- [x] search for flag in text, return possible flags
- [x] store fake flag
- [x] compare magic bytes to header dictionary to return filetype
- [x] take png/bmp filename and return zsteg output
- [x] create log in current directory
- [x] take text and append to log
- [x] take zip filename and unzip
- [x] take filename and extract with `binwalk -Me`, return output
- [x] take filename and return strings output
- [] fix run_cat (the `read()` method for the object created by `popen()`
    outputs 'invalid start byte' for photos)
- [] iterencode to test all 26 ROT's instead of just rot13
- [] make some functions work in python instead of using dependencies
- [] fix and update unit tests
- [x] tell user if zip file is password protected