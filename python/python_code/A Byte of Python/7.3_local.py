#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

def local_para(x):
	print 'x is', x
	x = 2
	print 'Change local x is', x

x = 50
local_para(x)
print 'Value of x is', x