#!/usr/bin/env python3

# Attempt to import python 3.0, fall back if necessary
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

# Import os for bash call and time for sleep functionality
import os
import time

# Abstract away variables
repeat = True
wait_time = 45
pushbullet_auth = "<pushbullet auth here>"
message_title = "Raspi IP"

# Begin Program, attempt to grab system IP
time.sleep(wait_time)
while repeat:
    try:
        ip_address = str(urlopen('http://ip.42.pl/raw').read()).replace("'", '').replace('b','')
        repeat = False
    except ImportError:
        time.sleep(5)

# Declare Bash command 
bash_command = "curl --silent -u \"\"\"" + pushbullet_auth + "\"\":\" -d type=\"note\" -d body=" + ip_address + " -d title=\"" + message_title + "\" 'https://api.pushbullet.com/v2/pushes'"

# Call Bash Command
os.system(bash_command)
