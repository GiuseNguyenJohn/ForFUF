# ForFUF - Forensics Faster U Fool

A command-line utility to automate the checking and solving of low hanging fruit for CTF forensic challenges.

<!-- TODO: add bash 1-liner to install dependencies -->
## Setup:
### Download required packages: 
```yes | sudo apt install binwalk exiftool steghide bsdmainutils && sudo gem install zsteg```

### Clone repository:
```git clone https://github.com/Magicks52/ForFUF.git```

## Usage:
```
 ________ ________  ________  ________ ___  ___  ________ 
|\  _____\\   __  \|\   __  \|\  _____\\  \|\  \|\  _____\
\ \  \__/\ \  \|\  \ \  \|\  \ \  \__/\ \  \\\  \ \  \__/ 
 \ \   __\\ \  \\\  \ \   _  _\ \   __\\ \  \\\  \ \   __\
  \ \  \_| \ \  \\\  \ \  \\  \\ \  \_| \ \  \\\  \ \  \_|
   \ \__\   \ \_______\ \__\\ _\\ \__\   \ \_______\ \__\ 
    \|__|    \|_______|\|__|\|__|\|__|    \|_______|\|__| 

usage: forfuf.py [-h] [--flag-format FLAG_FORMAT]

A command-line tool forto automate basic checksfor CTF forensics challenges

optional arguments:
  -h, --help            show this help message and exit
  --flag-format FLAG_FORMAT
                        regex flag pattern
```