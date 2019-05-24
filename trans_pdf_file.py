import os
import serial

# file save location - works best with gui path picker
save_path = os.path.join(os.path.expanduser('~'),'Documents/LiFi/Recieved_files') 
ser  = serial.Serial('/dev/ttyUSB0',9600,timeout=0)
# read any file
filer = open("test.pdf","rb")
base_path = os.path.basename(filer.name)
image = filer.read()
ser.write(image)
print(image)
