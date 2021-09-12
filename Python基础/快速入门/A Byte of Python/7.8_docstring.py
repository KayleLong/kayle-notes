#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

def print_max(x, y):
	'''Print the maximum of two numbers
	
	The two values must be integers.''' #这是一个函数文档说明，第一行是开始，第二行是空白，第三行是详细说明
	x = int(x) #convert to integers, ifpossible
	y = int(y)
	
	if x>y:
		print '%d is maximum.' % (x)
	else:
		print '%d is maximum.' % (y)
		
print_max(3, 5)
print print_max.__doc__ #注意__是双下划线