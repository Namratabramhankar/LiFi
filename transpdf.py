import os
import serial
import time
import PyPDF2

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=0)

# file save location - works best with gui path picker
save_path = os.path.join(os.path.expanduser('~'),'Documents/LiFi/Recieved_files') 

# read any file
filer = open("test.pdf","rb")
base_path = os.path.basename(filer.name)
#image = filer.read()
page = base_path.getPage(0)
page_content = page.extractText()
ser.write(page_content)
print(page_content)
# filew = open(os.path.join(save_path,base_path),"wb")
# filew.write(image)
ser.close()