from picamera import PiCamera
from PIL import Image
import os

camera = PiCamera()

camera.capture('gotcha_orig.jpg')

im = Image.open("gotcha_orig.jpg")
im.save("gotcha.jpg", dpi=(300,300))

os.system('scp gotcha.jpg jjohnson5253@skillpouch.com:/home/jjohnson5253/public_html/img/')





