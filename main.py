from gpiozero import Button
import time
import cv2

cam = cv2.VideoCapture(0)

bounce_time = 1.0
num_pics = 50
count = 0

def take_picture_with_camera():
    ret, image = cam.read()
    image_path = '/home/ivy/scanner/scans/image_%s.jpg' % int(
        round(time.time() * 1000))
    cv2.imwrite(image_path, image)
    count += 1
    print('Pic #' + count)

button = Button(2, bounce_time=bounce_time)
button.when_pressed = take_picture_with_camera

def run():
    print('Ready!')
    while count < num_pics:
        pass
    cam.release()

run()
