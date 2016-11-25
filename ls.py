#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import sys
import argparse
parser = argparse.ArgumentParser(description = '抓取該目錄下的檔名')
args = parser.parse_args()
print sys.argv
#if sys.argv[1] is None:
#	sys.argv[1] = "/Users"
#print sys.argv[1]
#print(os.listdir(sys.argv[1]))
