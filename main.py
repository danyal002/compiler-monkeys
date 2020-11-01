import serial
import time
import io
import picamera
import os
import requests


def capture():
    if(os.path.exists('/deskop/images/snapshot.jpg')):
        os.remove('/deskop/images/snapshot.jpg')
    camera = picamera.PiCamera()
    camera.capture("snapshot.jpg", resize=(500, 500))


def upload():
    fileToSend = "/desktop/images/snapshot.jpg"
    url = "http://104.198.69.57:5000/upload"
    files = [('DoorImage', (fileToSend, open(
        fileToSend, 'rb'), 'application/octet'))]
    r = requests.post(url, files=files)


# SPACE BELOW FOR HARWARE STUFF - DO NOT TYPE ABOVE THIS LINE LOLOLOL
arduino = serial.Serial('COM5', 9600, timeout=1)
time.sleep(10)
sio = io.TextIOWrapper(io.BufferedRWPair(arduino, arduino))
arduino.write(b'L')
print("sentL")
time.sleep(10)
arduino.write(b'U')
