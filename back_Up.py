#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : back_Up.py

import os
import time

source = ["/home/shiyanlou/Code/"]
target_dir = "/home/shiyanlou/Desktop/"

today_dir = target_dir + time.strftime('%Y%m%d')
time_dir = time.strftime('%H%M%S')

touch = today_dir + os.sep + time_dir + '.zip'
command_touch = "zip -qr " + touch ' '+ ' '.join(source)

if os.path.exists(today_dir)==0:
	os.mkdir(today_dir)
if os.system(command_t)==0:
	print 'Successful backup'
else:
	print 'Failed backup'
