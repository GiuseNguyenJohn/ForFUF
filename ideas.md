### Ideas:
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
    a certain range (ex. C.T.F.{.F.L.A.G.} ) // Attempt for 'picoctf{}': p.{0,2}i.{0,2}c.{0,2}o.{0,2}c.{0,2}t.{0,2}f.{0,2}\{.*\}


### TODO:
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
- [] iterencode to test all 26 ROT's instead of just rot13
- [] make some functions work in python instead of using dependencies