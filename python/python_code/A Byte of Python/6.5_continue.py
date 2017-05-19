#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

while True:
	s = raw_input('Enter something:')
	if s == "quit":
		break #直接跳出整个循环
	if len(s) < 3:
		continue #跳出当前循环，然后继续进行下一个循环
	print 'Input is of sufficient length.'