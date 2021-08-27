#!/bin/bash
# On boot, this script is called in the /etc/rc.local script.
# Script that restarts the clock script when device reboots.

cd /home/pi/circadian-rhythm-pie
tmux new-session -d -s lights_on sudo python3 /home/pi/circadian-rhythm-pie/clock.py
exit 0
