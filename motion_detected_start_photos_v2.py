# Author: Jake Johnson
# Created May 7, 2018
# This code takes and interrupt from GPIO and then begins taking photos
# Derived from "parent detector project" from projects.raspberrypi.org

# Note: to find pinout type "pinout" in terminal
# Note: channel number refers to GPIO# not pin#

from picamera import PiCamera
import RPi.GPIO as GPIO

camera = PiCamera()

GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    GPIO.wait_for_edge(11, GPIO.RISING)
    camera.start_preview()
    print("got it")

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
