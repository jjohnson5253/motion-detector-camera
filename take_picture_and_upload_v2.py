from picamera import PiCamera
import os

camera = PiCamera()

camera.capture('gotcha.jpg')

os.system('scp gotcha.jpg jjohnson5253@skillpouch.com:/home/jjohnson5253/public_html/img/')





