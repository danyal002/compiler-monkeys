import serial                                           # import serial library













# SPACE BELOW FOR HARWARE STUFF - DO NOT TYPE ABOVE THIS LINE LOLOLOL
arduino = serial.Serial('/dev/cu.usbserial-1410', 9600)   

while True:                                             # create loop
    command = str(input ("Servo position: "))       # query servo position
    arduino.write(bytes(command, 'utf-8'))                          # write position to serial port
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
