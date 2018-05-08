# Author: Jake Johnson
# Created May 7, 2018
# This code takes and interrupt from GPIO and calls another script to take a
# photo and upload to server
# Derived from "parent detector project" from projects.raspberrypi.org

# Note: to find pinout type "pinout" in terminal
# Note: channel number refers to GPIO# not pin#

import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
    try:
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        GPIO.wait_for_edge(11, GPIO.RISING)

        os.system('python take_picture_and_upload_v2.py')
        
        print("got it")
        

    except KeyboardInterrupt:
        GPIO.cleanup()
    GPIO.cleanup()
