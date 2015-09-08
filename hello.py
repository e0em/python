#!/usr/bin/python
# -*- coding: utf8 -*-
# 加上 coding 解決中文問題
# This program says hello and asks for my name.
print('Hello world!世界，我來了！')
print('What is your name?')    # 問名字
myName=raw_input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge=input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
import os
print(os.getcwd())
