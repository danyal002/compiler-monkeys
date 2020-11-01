import serial                                          
import time
import io

# SPACE BELOW FOR HARWARE STUFF - DO NOT TYPE ABOVE THIS LINE LOLOLOL
arduino = serial.Serial('COM5', 9600, timeout=1)
time.sleep(10)
sio = io.TextIOWrapper(io.BufferedRWPair(arduino, arduino))
arduino.write(b'L')
print("sentL")
time.sleep(10)
arduino.write(b'U')

