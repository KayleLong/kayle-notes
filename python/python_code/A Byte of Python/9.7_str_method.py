#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

name = 'Swaroop' #This is a string objet

if name.startswith('Swar'): #使用了 string的startswith()方法
	print 'Yes, the string startswith"Swar"'

if 'a' in name: #使用了 in 操作符
	print 'Yes, it contains the string "a"'

if name.find('war') != -1: #if not find, return -1
	print 'Yes, it contains the string"war"'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)