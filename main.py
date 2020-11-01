import serial                                           # import serial library
import time
import io












# SPACE BELOW FOR HARWARE STUFF - DO NOT TYPE ABOVE THIS LINE LOLOLOL
arduino = serial.Serial('COM5', 9600, timeout=1)
time.sleep(10)
sio = io.TextIOWrapper(io.BufferedRWPair(arduino, arduino))
arduino.write(b'L')
print("sentL")
# sio.write("L\n")
# sio.flush()
time.sleep(10)
arduino.write(b'U')
# sio.write("U\n")
# sio.flush()

# import serial
# import io
# ser = serial.serial_for_url('loop://', timeout=1)
# sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

# sio.write(unicode("hello\n"))
# sio.flush() # it is buffering. required to get the data out *now*
# hello = sio.readline()
# print(hello == unicode("hello\n"))
# reachedPos = str(arduino.readline())
                                            # create loop

	                          # write position to serial port
   # reachedPos = str(arduino.readline())            # read serial port for arduino echo
   # print(reachedPos)                               # print arduino echo to console



# def lock():                    
#     if(arduino.)
#     global arduino
#     #arduino.write(bytes("155\n", "utf-8"))   
#     arduino.write(b'155')                                             
#     #reachedPos = str(arduino.readline())  
      

# while True:
#     lock()
