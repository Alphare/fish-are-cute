#!/usr/bin/python3
import time
import datetime
from pathlib import Path

from pygame import camera, image

cam = None

def setup():
    print("Creating the fish_pictures folder")
    Path.mkdir(mode=0o777, parents=False, exist_ok=True)
    print("Initializing camera module")
    camera.init()

    print("Getting camera information")
    all_cams = camera.list_cameras()

    if not all_cams:
        raise Exception("No cameras found")

    global cam
    cam = camera.Camera(all_cams[0], (640, 480))
    print('Starting camera')
    cam.start()

def take_picture():
    global cam
    if not cam:
        raise NameError("No camera setup")
    for _ in range(5):  # Dirty hack to make sure that we get the last image
        img = cam.get_image()
    filename = str(datetime.datetime.now())[:-7].replace(' ', '_')
    image.save(img, 'fish_pictures/{}.jpg'.format(filename))

    print('File {}.jpg saved'.format(filename))

def start_timelapse(interval=5):
    while True:
        take_picture()
        time.sleep(interval)

if __name__ == '__main__':
    while cam is None:
        try:
            setup()
        except SystemError as e:
            print(e)
            print('Retrying')
            pass
    start_timelapse()
