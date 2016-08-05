#! /usr/bin/python

# (C) 2002-2006 Chris Liechti <cliechti@gmx.net>
# redirect data from a TCP/IP connection to a serial port and vice versa
# requires Python 2.2 'cause socket.sendall is used

import serial
def send(data):
    try:
        ser.write(data)
        print("write to modules:" + data)
    except Exception as e:
        print "Couldn't send data to serial port: %s" % str(e)
    else:
        try:
            data = ser.readline()
        except Exception as e:
            print "Couldn't read data from serial port: %s" % str(e)
        else:
           if data:  # If data = None, timeout occurr
               n = ser.inWaiting()
               if n > 0: data += ser.read(n)
               return data
ser = serial.Serial()
ser.port = 'COM5'
ser.baudrate = 9600
ser.rtscts  = False
ser.xonxoff = False
ser.timeout = 1
print(ser)
ser.open()
print(send("AT"))
