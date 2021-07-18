import serial
import time
import json
from datetime import datetime

# set up the serial line
ser = serial.Serial('COM6', 115200)


while True:
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r

    sterilizedOutput =  json.loads(string)

    with open("dataDump.txt","a") as b:
        mid = str(time.ctime()),str(sterilizedOutput["percentage"])
        output = ",".join(mid)
        b.write(output)
        b.write("\n")

    print(string)
    time.sleep(0.1)            # wait (sleep) 0.1 seconds

ser.close()