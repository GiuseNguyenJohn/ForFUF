# ForFUF - Forensics Faster U Fool

A command-line utility to automate the checking and solving of low hanging fruit for CTF forensic challenges.

_Note: Project still in development stage_

DEMO: 

## Setup:
### Clone Repository:
```
git clone https://github.com/Magicks52/ForFUF.git && cd ./ForFUF
```
### Run 'install.sh': 
```
chmod +x ./install.sh && sudo ./install.sh
```
### Mark 'forfuf.py' as executable:
```
chmod +x forfuf.py
```
### Example:
```
sudo ./forfuf.py -f "p.{0,2}i.{0,2}c.{0,2}o.{0,2}C.{0,2}T.{0,2}F.{0,2}\{.{1,40}\}" -s "picoCTF{" exiftool_base64.jpg
```
## Usage:
```
 ________ ________  ________  ________ ___  ___  ________ 
|\  _____\\   __  \|\   __  \|\  _____\\  \|\  \|\  _____\
\ \  \__/\ \  \|\  \ \  \|\  \ \  \__/\ \  \\\  \ \  \__/ 
 \ \   __\\ \  \\\  \ \   _  _\ \   __\\ \  \\\  \ \   __\
  \ \  \_| \ \  \\\  \ \  \\  \\ \  \_| \ \  \\\  \ \  \_|
   \ \__\   \ \_______\ \__\\ _\\ \__\   \ \_______\ \__\ 
    \|__|    \|_______|\|__|\|__|\|__|    \|_______|\|__| 

usage: forfuf.py [-h] [-f FLAG_FORMAT] [-p PASSWORD] [-s START_FLAG] filename

A command-line tool to automate basic checksfor CTF forensics challenges

positional arguments:
  filename              file to analyze

optional arguments:
  -h, --help            show this help message and exit
  -f FLAG_FORMAT, --flag-format FLAG_FORMAT
                        regex flag pattern (ex. "p.{0,2}i.{0,2}c.{0,2}o.{0,2}C.{0,2}T.{0,2}F.{0,2}\{.*\}")
  -p PASSWORD, --password PASSWORD
                        password for steghide
  -s START_FLAG, --start-flag START_FLAG
                        prefix of flag (ex. "picoctf{")
```