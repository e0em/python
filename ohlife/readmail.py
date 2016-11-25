#!/usr/bin/python
import sys 
data = sys.stdin.readlines()
#print data
fi = open('/tmp/savemail.txt','w+')
fi.writelines(data)
fi.close()
