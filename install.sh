#!/bin/bash
yes | sudo apt install binwalk exiftool steghide bsdmainutils libmagic1 && sudo gem install zsteg
wget "http://www.caesum.com/handbook/Stegsolve.jar" -O stegsolve.jar
chmod +x stegsolve.jar
sudo mv ./stegsolve.jar /bin/stegsolve
wget "https://downloads.sourceforge.net/project/diit/diit/1.5/diit-1.5.jar?ts=gAAAAABiECz6OPbRF-XuW33BOJQGabDTxbQrbUrUxebsDyldES0Q1nizVKWjX8bTE76HkMphqwKBdXEYgzRobxYcRaPzVp_yLQ%3D%3D&r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fdiit%2Ffiles%2Fdiit%2F1.5%2Fdiit-1.5.jar%2Fdownload" -O diit
chmod +x diit
sudo mv ./diit /bin/diit
sudo pip install -r requirements.txt