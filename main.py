from gpiozero import Button
import time
import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
cam.set(cv2.CAP_PROP_FPS, 10)

bounce_time = 0.100

def take_picture_with_camera():
    ret, image = cam.read()
    if ret:
        image_path = '/home/ivy/scanner/scans/image_%s.jpg' % int(
            round(time.time() * 1000))
        cv2.imwrite(image_path, image)
        print('Pic taken')

button = Button(2, bounce_time=bounce_time)
button.when_released = take_picture_with_camera

def run():
    print('Ready!')
    while True:
        pass
    cam.release()

run()
