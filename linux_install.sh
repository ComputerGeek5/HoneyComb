#!/bin/bash
#TODO: Make this environment-agnostic as well in the future

apt update -y
apt upgrade -y
apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa
apt -y install python3.10

chmod +x configure.sh
./configure.sh

chmod +x main.py

curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.10 get-pip.py
pip install --no-cache-dir -r requirements.txt