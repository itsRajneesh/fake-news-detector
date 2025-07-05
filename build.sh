#!/usr/bin/env bash
# Force use of correct Python version & pip instead of Poetry
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
