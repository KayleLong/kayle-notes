#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

#This is my shopping list
shop_list = ['apple', 'mango', 'pear', 'banana']
print 'I hava %d items to pruchase.' % (len(shop_list))

print 'These itmes are:'
for itme in shop_list:
	print itme

print '\nI also hava to buy some rice.'
shop_list.append('rice')
print 'My shopping list is now', shop_list

print 'I will sort my shopping list.'
shop_list.sort()
print 'Sorted shopping list is', shop_list

print 'The first item I will buy is', shop_list[0]
olditem=shop_list[0]
shop_list.pop(0)
print 'I bought the', olditem
print 'My shopping list is now', shop_list