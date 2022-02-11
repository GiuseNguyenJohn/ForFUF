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
    a certain range (ex. C.T.F.{.F.L.A.G.} )  // attempt for 'picoctf{}':  p.{0,2}i.{0,2}c.{0,2}o.{0,2}c.{0,2}t.{0,2}f.{0,2}\\{.*\\}


### TODO:
- [] Add one-liner in README to install all dependencies in bash
- [x] check if program ran with sudo
- [x] check if given file exists
- [x] store flag format, return match object (plaintext, rot13, base64)
- [] get a file's magic bytes
- [x] search for flag in text, return possible flags
- [] store fake flag
- [] compare magic bytes to header dictionary to return filetype
- [] take png/bmp filename and return zsteg output
- [] create log in current directory
- [] take text and append to log
- [] take zip filename and unzip
- [] take filename and extract with `binwalk -Me`, return output
- [] take filename and return strings output
- 