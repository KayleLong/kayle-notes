#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

number = 23
guess = int(raw_input('Enter an intrger:'))

if guess == number:
	print 'Congratulations, you guessed it.'
elif guess < number:
	print 'No, it is a little higter than that.'
else:
	print 'No, it is a little lower than that.'
	
print 'Done'