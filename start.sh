#!/bin/bash

git clone https://github.com/ТВОЙ_ЮЗЕРНЕЙМ/ИМЯ_РЕПОЗИТОРИЯ.git
cd ИМЯ_РЕПОЗИТОРИЯ

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python3 main.py
