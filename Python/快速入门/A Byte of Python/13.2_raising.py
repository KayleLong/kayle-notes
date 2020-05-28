#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

class ShortInputException(Exception):
	"""A suer-defined exception class"""
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast
try:
	s = raw_input('Enter something ->')
	if len(s) < 3:
		raise ShortInputException(len(s), 3)
		#Other work can continue asusual here
except EOFError:
	print '\nWhy did you do an EOF on me?'
except ShortInputException, x:
	print 'ShortInputException:The input was of length %d was excepting at least %d' % (x.length, x.atleast)
else:
	print 'No exception was rasised.'	