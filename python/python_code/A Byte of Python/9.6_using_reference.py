#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

print 'Simple A ssignment'
shoplist = ['apple', 'banana', 'pear', 'mango']
mylist = shoplist #mylist is just an other name pointing to the objet!

del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist

print  'Copy by making a full slice'
mylist = shoplist[:] #make a copy by doing a full slice
del mylist[0] #remove first item

print 'shoplist is', shoplist
print 'mylist is', mylist
#no tice that now the two lists are diffent