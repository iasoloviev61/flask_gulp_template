#!/usr/bin/env bash
export FLASK_APP=run.py
export FLASK_DEBUG=1
export FLASK_ENV=development
python3.5 -m flask run --host=0.0.0.0