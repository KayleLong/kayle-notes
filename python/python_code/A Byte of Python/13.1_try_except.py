#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

import sys

try:
	s = raw_input('Enter something ->')
except EOFError:
	print '\nWhy did you do an EOF on me?'
	sys.exit() #exit the program
except:
	print '\n Some error/exception occurred.'
	#Here, we are not excepting the program
print 'Done'