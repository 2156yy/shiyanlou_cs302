#!/usr/bin/python
# -*- coding: utf-8 -*-
#Filename : backUp.py

import Tkinter
import os
import time

def backup():
	global entry_source
	global entry_target
	source = entry_source.get()
	target_dir = entry_target.get()
	today_dir = target_dir + time.strftime('%Y%m%d')
	time_dir = time.strftime("%H%M%S")

	touch = today_dir + os.sep + time_dir + '.zip'
	command_touch = "zip -qr " + touch +' '+ source

	print command_touch
	print source
	print target_dir
	if os.path.exists(today_dir)==0:
		os.mkdir(today_dir)
	if os.system(command_touch)==0:
		print 'Success backup Up'
	else:
		print 'Failed backup'

root = Tkinter.Tk()
root.title('BackUp')
root.geometry("200x200")

lbl_source = Tkinter.Label(root, text='源地址')
lbl_source.grid(row=0, column=0)
entry_source = Tkinter.Entry(root)
entry_source.grid(row=0,column=1)

lbl_target = Tkinter.Label(root, text='目的地址')
lbl_target.grid(row=1, column=0)
entry_target = Tkinter.Entry(root)
entry_target.grid(row=1,column=1)

but_back = Tkinter.Button(root,text='备份')
but_back.grid(row=3, column= 0)
but_back["command"] = backup

root.mainloop()
