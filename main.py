from gpiozero import Button
import time
import cv2

cam = cv2.VideoCapture(0)

pics = 0
bounce_time = 0.100

def take_picture_with_camera(pics):
    ret, image = cam.read()
    if ret:
        image_path = '/home/ivy/scanner/scans/image_%s.jpg' % int(
            round(time.time() * 1000))
        cv2.imwrite(image_path, image)
        pics += 1
        print(pics)

button = Button(2, bounce_time=bounce_time)
button.when_pressed = lambda pics : take_picture_with_camera(pics)

def run():
    print('Ready!')
    while True:
        pass
    cam.release()

run()
