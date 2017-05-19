#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

class Person(object):
	# Person属性
	popilation = 0

	# 初始化Person类的实例
	def __init__(self, name):
		self.name = name
		print 'Initializing %s' % (self.name)

		Person.popilation += 1

	# 销毁Person类的实例 
	def __del__(self):
		print '%s says bye' % (self.name)

		Person.popilation -= 1

		if Person.popilation == 0:
			print 'I\'m the last one.'
		else:
			print 'There are still %d people left.' % (Person.popilation)

	# 定义Person类的方法
	def say_hi(self):
		print 'Hi, my name is %s.' % (self.name)

	def howmany(self):
		if Person.popilation == 1:
			print 'I\'m the only person here.'
		else:
			print 'We are %d persons here.' % (Person.popilation)

swaroop = Person('Swaroop')
swaroop.say_hi()
swaroop.howmany()

kalam = Person('Abdul Kalam')
kalam.say_hi()
kalam.howmany()

swaroop.say_hi()
swaroop.howmany()