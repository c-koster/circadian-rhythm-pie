"""
clock.py

Determines time of day and writes pixel data to the light strip
This should run on boot.
"""

import datetime
import time
import board
import neopixel

from kelvin_to_rgb import convert_K_to_RGB
#kvals = list(range(1000,6100,100))
#[print("{}K temperature has has rgb values: {}".format(k,convert_K_to_RGB(k))) for k in kvals]

OFF_ZERO = (0,0,0)

pi_pin = board.D18
numpix = 150
brightness = .08

# morning BLUE light hours
# BLUE light is stimulating
start_morning = "07:30:00"
end_morning = "09:00:00"

# evening hours means dim-ish red lights
start_evening = "19:00:00"
#end_evening = "22:00:00" # no end_evening needed as the lights switch at 10pm

# third option: night hours means barely visible (or just off). End at 6am
start_night = "22:00:00"
end_night = "06:00:00"

print("starting infintie clock")

with neopixel.NeoPixel(pi_pin, numpix, brightness=brightness) as pixels:

    color_change = False
    while True:
        date_string = datetime.datetime.now().strftime("%H:%M:%S")

        if date_string == start_morning:
            color = convert_K_to_RGB(8000)
            color_change = True

        elif date_string == end_morning:
            color = OFF_ZERO
            color_change = True

        elif date_string == start_evening:
            color = convert_K_to_RGB(1250)
            color_change = True

        elif date_string == start_night:
            color = convert_K_to_RGB(1000)
            color_change = True

        elif date_string == end_night:
            color = OFF_ZERO
            color_change = True

        else:
            time.sleep(1)

        # update neopixel strip with new colors
        if color_change:
            pixels.fill(color)
            color_change = False
            time.sleep(1)
