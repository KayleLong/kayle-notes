#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

def fun_key(a, b=5, c=10): #形参b和c，是默认参数。默认参数放在必选参数之后，避免歧义
	print 'a is %d, b is %d, c is %d' %(a, b, c)

fun_key(3, 7) #a=3,b=5,c=7
fun_key(25, c=24) #a=25,b=5,c=10
fun_key(c=50, a=100) #a=100,b=5,c=50