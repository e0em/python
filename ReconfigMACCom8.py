#coding:utf-8
import serial
import time
ser = serial.Serial()
ser.port = 'COM8'
ser.timeout = 1
def  ReadAtEcho():
	for line in ser.readlines():
		line = line.strip() #前後去掉空白及換行符號
		if not len(line) or line.startswith('O'):  # 判断是否是空行或“O”開頭
			continue  # 是的话，跳过不处理
		print line

ser.open()
print ("Module current information:")
ser.write("AT+echo=0\n")
ser.write("at+sgmr?\n") #模組版本
ser.write("AT+csf?\n") #SP Value
ser.write("at+sgmd?\n") #Mac Addr，SN
ReadAtEcho()
MAC = raw_input('Enter your new Mac Address:')
SN = raw_input('Enter your new serial no.:')
SID = raw_input('Enter your new System ID:')
PIN = raw_input('Enter your new PIN code:')
print ("Star setting")
ser.write("AT+GADM=1,Gemtek888\n")
ReadAtEcho()
print ("Write Channel info")
ser.write("AT+GCH=923000000,924000000,925500000,926500000\n")
ReadAtEcho()
print ("Write CHO info")
ser.write("AT+GCHO=125000,375000\n")
ReadAtEcho()
print ("Write MTXP info")
ser.write("AT+GMTXP=20\n")
ReadAtEcho()
print ("Write SID info")
ser.write("AT+GSID=\""+SID+"\"\n")
ReadAtEcho()
print ("Write GKEY info")
ser.write("AT+GKEY=43610A1F04719BB807A8073F8AECB131,43610A1F04719BB807A8073F8AECB131\n")
ReadAtEcho()
print ("Write SYSC info")
ser.write("AT+GSYSC=0,1\n")
ReadAtEcho()
print ("Writing MAC address")
ser.write("AT+GGMD=\""+MAC+"\",\""+SN+"\"\n")
ReadAtEcho()
print ("Writing PIN")
ser.write("AT+GPIN="+PIN+"\n")
ReadAtEcho()
print ("writing the configure to default")
ser.write("AT&F\n")
time.sleep(3)
ReadAtEcho()
print ("Module new information")
ser.write("at+sgmr?\n") #模鈻扢鈻掓本
ser.write("AT+csf?\n") #SP Value
ser.write("at+sgmd?\n") #Mac Addr鈻掆枓SN
ReadAtEcho()

