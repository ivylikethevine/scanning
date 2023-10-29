from gpiozero import Button
import time
import cv2
import fnmatch
import os

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
cam.set(cv2.CAP_PROP_FPS, 10)

num_pics = 50
bounce_time = 0.150

def take_picture_with_camera():
    ret, image = cam.read()
    if ret:
        image_path = './scans/image_%s.jpg' % int(
            round(time.time() * 1000))
        print(cv2.imwrite(image_path, image))

button = Button(2, bounce_time=bounce_time)
button.when_released = take_picture_with_camera

def run():
    count = 0
    print('Ready!')
    while count < num_pics:
        dir_path = './scans/'
        count = len(fnmatch.filter(os.listdir(dir_path), '*.*'))
        print('Count:', count)
        pass
    cam.release()

run()
