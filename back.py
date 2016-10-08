#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename : back.py

import os
import time

source = ['/home/shiyanlou/Code/']
target_dir = '/home/shiyanlou/Desktop/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
print target

sou = ''.join(source)
print sou
print type(source),type(sou)

#zip_command = "zip -qr %s %s" %(target, ''.join(source))

#if os.system(zip_command) = 0:
#	print 'Successful backup'
#else :
#	print 'Backup Failed'
