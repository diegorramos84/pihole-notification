#!/usr/bin/env python3

import subprocess

pihole_status = subprocess.getoutput("pihole status")

if "enabled" not in pihole_status:
    subprocess.run(["python", "send_email.py"])
    print('Pi-hole is not running properly. Status:', pihole_status)