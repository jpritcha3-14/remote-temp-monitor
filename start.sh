#!/bin/bash
# stop script on error
set -e

loc=/home/bismarck/bismarck/

# run pub/sub sample app using certificates downloaded in package
printf "\nStarting up bismarck temperature monitor...\n"
/usr/bin/python3 "$loc"publish_temp.py -e a2eoodttfyy85k-ats.iot.us-west-2.amazonaws.com -r "$loc"root-CA.crt -c "$loc"Bismarck.cert.pem -k "$loc"Bismarck.private.key -id bismarck -t bismarck/temp
