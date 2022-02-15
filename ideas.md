### Ideas:
- write unit tests for each function/class
- Questions:
    - grep for flag, or parse with python?
    - how to format output? files? stdout?
    - how to check for run with sudo? uid? $USER env var?
- automatic flag detection?
- run 'file' linux tool to determine type of file
- check and fix corrupt file headers (autofix somehow? like if first 2 bytes
    are like a PNG, say 'png detected, fix header? (Y/N) )
- check LSB steg with zsteg
- extract strings and search for flag
- use regex to identify when flag characters are all grouped together within
    a certain range (ex. C.T.F.{.F.L.A.G.} )  // attempt for 'picoctf{}':  p.{0,2}i.{0,2}c.{0,2}o.{0,2}c.{0,2}t.{0,2}f.{0,2}\{.*\}


### TODO:   
- [x] add one-liner in README to install all dependencies in bash
- [x] check if program ran with sudo
- [x] check if given file exists
- [x] store flag format, return match object (plaintext, rot13, base64)
- [x] search for flag in text, return possible flags
- [x] determine filetype with magic module
- [x] take png/bmp filename and return zsteg output
- [x] take text and append to log
- [] take zip filename and unzip
- [x] take filename and extract with `binwalk -Me`, return output
- [x] take filename and return strings output
- [x] take filename and return exiftool output
- [x] take filename and default password of '', extract with password using steghide, return output
- [x] output magic bytes neatly
- [x] take hex and overwrite the file header
- [] in class 'FileClass':
    - [] make method 'handle_png_and_bmp'
    - [] make method 'handle_jpg_and_jpeg'
    - [] make method 'handle_zip