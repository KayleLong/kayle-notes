#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

import time

try:
	f = file('poem.txt')
	while Ture: #our usuall file-reading idiom
		line = f.readline()
		if len(line) == 0:
			break
		time.sleep(2)
		print line,
finally:
	f.close()
	print 'C leadning up...closed the file'