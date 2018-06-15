#!/usr/bin/env bash
export FLASK_APP=run.py
export FLASK_DEBUG=1
export FLASK_ENV=development
#flask db migrate -m "users table"
#flask db upgrade
python3.5 -m flask run --host=0.0.0.0