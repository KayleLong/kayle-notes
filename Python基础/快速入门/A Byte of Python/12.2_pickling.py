#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

import cPickle as p #导入模块

shop_list_file = 'shoplist.data' #the name of the file where we will store the objet

shoplist = ['apple', 'banana', 'mango', 'carrot']

#write to the file
f = file(shop_list_file, 'w')
p.dump(shoplist, f) #dump the objet to a file
f.close()

del shoplist # remove the shoplist

#Read back from the storage
f = file(shop_list_file) #Read mode
storedlist = p.load(f) #使用pickle模块的load函数的返回来取对象，这个过程称为取存储
print storedlist