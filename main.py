 
import serial
import time
import io
import picamera
import os
import requests

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) # Gotta change the com port when we connect the arduin to the pi
time.sleep(7)

def capture():
    if(os.path.exists('/home/pi/Desktop/images/snapshot.jpg')):
        os.remove('/home/pi/Desktop/images/snapshot.jpg')
    camera = picamera.PiCamera()
    camera.hflip = True
    camera.capture("/home/pi/Desktop/images/snapshot.jpg", resize=(500, 500))


def upload():
    fileToSend = "/home/pi/Desktop/images/snapshot.jpg"
    url = "http://104.198.69.57/upload"
    files = [('DoorImage', (fileToSend, open(
        fileToSend, 'rb'), 'application/octet'))]
    r = requests.post(url, files=files)
    result = str(r.content, "utf-8")
    return result

def lock():
    arduino.write(b'L')

def unlock():
    arduino.write(b'U')

while(True):
    time.sleep(2) #should be changed on how often we want to run the entire process.
    capture()
    result = upload()
    print(result)
    if(result == "False"):
        unlock()
        time.sleep(3)    #Time after which the door should automatically be locked.
        lock()
    break
