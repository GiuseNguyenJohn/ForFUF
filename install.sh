#!/bin/bash
yes | sudo apt install binwalk exiftool steghide bsdmainutils libmagic1 && sudo gem install zsteg
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
chmod +x stegsolve.jar
sudo mv ./stegsolve.jar /bin/stegsolve
sudo pip install -r requirements.txt