from gpiozero import Button
import time
import cv2

cam = cv2.VideoCapture(0)

bounce_time = 0.150

def take_picture_with_camera():
    print('Button pressed')
    ret, image = cam.read()
    print('cam.read')    
    if not ret:
        print('error taking picture')
    else:
        print('creating image path')
        image_path = '/home/ivy/scanner/scans/image_%s.jpg' % int(
            round(time.time() * 1000))
        print('writing image')
        cv2.imwrite(image_path, image)
    print('Image function over')

button = Button(2, bounce_time=bounce_time)
button.when_pressed = take_picture_with_camera

def run():
    print('Ready!')
    while True:
        pass
    cam.release()

run()
