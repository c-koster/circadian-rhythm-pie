from kelvin_to_rgb import convert_K_to_RGB
kvals = [1000,1500,2000,2500,4000,8000,16000,32000]
for k in kvals:
    print("{}K temperature has has rgb values: {}".format(k,convert_K_to_RGB(k)))



import datetime
import time
import board
import neopixel

pi_pin = board.D18
numpix = 144
brightness = 1.0
pixels = neopixel.NeoPixel(pi_pin, numpix, brightness=brightness)

# morning BLUE light hours
# BLUE light is stimulating
start_morning = "06:00:00"
end_morning = "10:00:00"

# evening RED light hours
# RED light is calming allows melatonin production to increase
start_night = "18:00:00"
end_night = "22:00:00"

color_change = False

for k in kvals:
    color = convert_k_to_rgb(k)

    pixels.fill(color)
    time.sleep(5)

pixels.fill((0,0,0))
exit(0)

"""
while True:
    date_string = datetime.datetime.now().strftime("%H:%M:%S" )

    if date_string == start_morning:
        color = (0, 0, 255)
        color_change = True

    elif date_string == end_morning:
        color = (0, 0, 0)
        color_change = True

    elif date_string == start_night:
        color = (255, 0, 0)
        color_change = True

    elif date_string == end_night:
        color = (0, 0, 0)
        color_change = True

    else:
        time.sleep(1)

    # update neopixel strip with new colors
    if color_change:
        pixels.fill(color)
        color_change = False
        time.sleep(1)
"""
