#coding:utf-8
import serial
ser = serial.Serial()
ser.port = 'COM8'
ser.timeout = 1
ser.open()
ser.write("AT\n")
ser.write("at+sgmr?\n") #模組版本
ser.write("AT+csf?\n") #SP Value
ser.write("at+sgmd?\n") #Mac Addr，SN
ser.write("AT+GADM=1,Gemtek888\n")
ser.write("AT+GPIN?\n") #Mac Addr，SN

for line in ser.readlines():
    line = line.strip() #前後去掉空白及換行符號
    if not len(line) or line.startswith('O'):  # 判断是否是空行或“O”開頭
        continue  # 是的话，跳过不处理
    print line

