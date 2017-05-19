#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

#这是一个父类
class School_member(object):
	'''Represents any school member'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print 'Initialized School_member: %s' % (name)

	def tell(self):
		'''Tell my details'''
		print 'Name:%s, Age:%s' % (self.name, self.age)

#这是一个继承自School_member父类的Teacher子类
class Teacher(School_member):
	"""Pepresets a teacher"""
	def __init__(self, name, age, salary):
		School_member.__init__(self, name, age)
		self.salary = salary
		print 'Initialized Teacher:%s' % (self.name)
	
	def tell(self):
		School_member.tell(self)
		print 'Salary:%d' % (self.salary)

#这是一个继承自School_member父类的Student子类
class Student(School_member):
	"""Pepresets a student"""
	def __init__(self, name, age, marks):
		School_member.__init__(self, name, age)
		self.marks = marks
		print 'Initialized Student:%s' % (self.name)
	
	def tell(self):
		School_member.tell(self)
		print 'marks:%d' % (self.marks)
						
t = Teacher('Mrs.Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

print #prints a blak line

members = [t, s]
for member in members:
	member.tell ()