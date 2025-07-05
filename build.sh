#!/usr/bin/env bash
# Force pip install and bypass Poetry completely
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
