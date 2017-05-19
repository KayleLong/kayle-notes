#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

shoplist = ['apple', 'banana', 'mango', 'pear']

#Indexing or 'Subcription' operation

print 'Itme 0 is', shoplist[0]
print 'Itme 1 is', shoplist[1]
print 'Itme 2 is', shoplist[2]
print 'Itme 3 is', shoplist[3]
print 'Itme -1 is', shoplist[-1]
print 'Itme -2 is', shoplist[-2]

#Slicing on a list

print 'Itme 1 to 3 is', shoplist[1:3]
print 'Itme 2 to end is', shoplist[2:]
print 'Itme 1 to -1 is', shoplist[1:-1]
print 'Itme start to end is', shoplist[:] #索引是可选的，冒号是必须的

#Slicing on a string
name = 'Swaroop'

print 'chaeracters 1 to 3 is', name[1:3]
print 'chaeracters 2 to end is', name[2:]
print 'chaeracters 1 to -1 is', name[1:-1]
print 'chaeracters start to end is', name[:]