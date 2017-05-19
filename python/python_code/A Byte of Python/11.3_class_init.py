#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

class Person(object):
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print 'Hello, my name is', self.name

p = Person('Anan')
p.say_hi()
