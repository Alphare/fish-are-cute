#!/usr/bin/env python3
import time
import datetime
from pathlib import Path

from pygame import camera, image

cam = None

OUT_FOLDER = Path("pictures")
FILE_EXTENSION = "jpg"

def setup():
    print("Creating the fish_pictures folder")
    OUT_FOLDER.mkdir(mode=0o777, parents=False, exist_ok=True)
    print("Initializing camera module")
    camera.init()

    print("Getting camera information")
    all_cams = camera.list_cameras()

    if not all_cams:
        raise SystemError("No cameras found")

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
    full_filename = '{}.{}'.format(filename, FILE_EXTENSION)
    image.save(img, str(OUT_FOLDER / full_filename))

    print('File {} saved'.format(full_filename))

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
            print('Retrying in a second')
            time.sleep(1)

    start_timelapse()
