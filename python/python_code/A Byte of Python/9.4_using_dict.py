#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

#'ab' is short for  'a'ddress 'b'ook
ab = {'Swaroop' 	: 'swroopch@byte-of-python',
	  'Larry' 		: 'larry@wall.org',
	  'Mastumoto' 	: 'matz@ruby-lang.org',
	  'Spammer' 	: 'spamerr@hotmail.com'
}

print 'Swaroop\'s address is %s' % (ab['Swaroop'])

#Adding a key/value pair
ab['Guido'] = 'guido@python.org'

#deleting a key/value pair
del ab['Swaroop']

print '\nThere are %d contacts in the address-book\n' % (len(ab))
for name, address in ab.items(): #使用字典的items方法，来使用字典中的每个键/值
	print 'Contact %s at %s' % (name, address)

if 'Guido' in ab: #使用in操作符，来检验一个键/值是否在字典中
	print '\nGuido\'s address id %s' % (ab['Guido'])