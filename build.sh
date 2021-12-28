#/bin/sh
pip3 install -r requirements.txt &&
cd dev &&
pelican -s publishconf.py
