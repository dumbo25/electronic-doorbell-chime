# run using 
#   $ sudo python chime.py
# or
#   open  browser and enter url: http://♣your-chime's-ipaddress♣/
#   requires a slash / after the IP address or it does not work

# This script depends on IFTTT, an Arlo or other smart doorbell, and port forwarding

# IFTTT using Arlo Doorbell Button press as a trigger works best
# only works on http, which shoouldn't be open to the internet
#
# Need to port forwarding so IFTTT can communicate with the Raspberry Pi
#   AT&T Gateway, Firewall, NAT Gaming
#      Custom Services
#         chime, 8081-8081, 8081, TCP/UDP, Add
#      return to NAT Gaming
#      Select Service 8081 and Needed by Device = ♣your-chime's-hostname♣
#         click Add

import time
import bottle
import subprocess

@bottle.get('/')
def home():
    cmd="sudo aplay -Dhw:0 /home/pi/dingDongChime.wav"
    subprocess.call(cmd, shell=True)
    return 'play chime'

bottle.run(host='0.0.0.0', port=8081)
