#!/usr/bin/env bash

export APP_ENV=prod

venv/bin/python main.py ./config/prod-limited.json
