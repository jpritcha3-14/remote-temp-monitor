#!/bin/bash
# stop script on error
set -e

loc=/home/bismarck/bismarck/

printf "\nStarting HTTP server on port 12000...\n"
/usr/bin/python3 "$loc"HTTPServer.py
