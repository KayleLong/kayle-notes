#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

#通过raw_inuput()函数获取一个name变量
name = raw_input('Please inout your name:')
#直接输出字符串
print'Hi,', name,'welcome to Python.'
#% 可以用来格式化字符串
print('Hi, %s welcome to Python.' % (name))
#另一种更加方便的格式化输出 format()
print'{0} wants to eat {1}.'.format('Anan', 'Apple')
#带参数的format()
print'{myname} wants to eat {food}.'.format(myname=name, food='Apple')