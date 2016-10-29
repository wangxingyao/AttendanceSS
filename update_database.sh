#!/usr/bin/env bash

rm app.db db_repository/ -rf
./db_create.py
./db_add_data.py
