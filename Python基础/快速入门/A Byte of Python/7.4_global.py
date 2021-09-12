#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

def global_para():
	global x
	print 'x is', x
	x = 2
	print 'Change global x is', x

x = 50
global_para()
print 'Value of x is', x