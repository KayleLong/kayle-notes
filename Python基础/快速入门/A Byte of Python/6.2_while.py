#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

number = 23
running = True # 写成true,是错误的

while running:
  guess = int(raw_input('Enter an integer:'))
  if guess == number:
        print 'Congratulation, you guessd it.'
        running=False
  elif guess<number:
        print 'No, it is a little higher  than that.'
  else:
        print 'No, it is a little lower  than that.'
else:
  print 'the while loop is over.'
  
print 'Done'