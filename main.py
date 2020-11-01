import serial
import time
import io
import picamera
import os
import requests


def capture():
    if(os.path.exists('/home/pi/Desktop/images/snapshot.jpg')):
        os.remove('/home/pi/Desktop/images/snapshot.jpg')
    camera = picamera.PiCamera()
    camera.hflip = True
    camera.capture("/home/pi/Desktop/images/snapshot.jpg", resize=(500, 500))


def upload():
    fileToSend = "/home/pi/Desktop/images/snapshot.jpg"
    url = "http://104.198.69.57:5000/upload"
    files = [('DoorImage', (fileToSend, open(
        fileToSend, 'rb'), 'application/octet'))]
    r = requests.post(url, files=files)

def lock():
    arduino = serial.Serial('COM5', 9600, timeout=1) # Gotta change the com port when we connect the arduin to the pi
    time.sleep(10)
    sio = io.TextIOWrapper(io.BufferedRWPair(arduino, arduino))
    arduino.write(b'L')
    time.sleep(10)

def unlock():
    arduino = serial.Serial('COM5', 9600, timeout=1) # Gotta change the com port when we connect the arduin to the pi
    time.sleep(10)
    sio = io.TextIOWrapper(io.BufferedRWPair(arduino, arduino))
    arduino.write(b'U')
    time.sleep(10)


