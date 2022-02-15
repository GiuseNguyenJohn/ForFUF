# ForFUF - Forensics Faster U Fool

A command-line utility to automate the checking and solving of low hanging fruit for CTF forensic challenges.

## Setup:
### Download required packages: 
```
yes | sudo apt install binwalk exiftool steghide bsdmainutils && sudo gem install zsteg
```
### Download Stegsolve:
```
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
chmod +x stegsolve.jar
sudo mv ./stegsolve.jar /bin/stegsolve
```
### Clone repository:
```
git clone https://github.com/Magicks52/ForFUF.git
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

usage: ForFUF.py [-h] [-f FLAG_FORMAT] [-p PASSWORD] filename

A command-line tool forto automate basic checksfor CTF forensics challenges

positional arguments:
  filename              file to analyze

optional arguments:
  -h, --help            show this help message and exit
  -f FLAG_FORMAT, --flag-format FLAG_FORMAT
                        regex flag pattern
  -p PASSWORD, --password PASSWORD
                        password for steghide
```