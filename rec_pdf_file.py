import os
import serial

save_path = os.path.join(os.path.expanduser('~'),'Documents/LiFi/Recieved_files') 
ser  = serial.Serial('/dev/ttyUSB1',9600,timeout=0)

while(1):
    if ser.inWaiting():
        readf = ser.read()

filew = open(os.path.join(save_path,base_path),"wb")
filew.write(readf)