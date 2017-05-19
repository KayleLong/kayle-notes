#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

zoo=("wolf", "elephant", "penguin")
print "number of animals in the zoo is", len(zoo)

new_zoo=("monkey", "dolphin", zoo) #在元组中包含另一个元组
print "number of animals in the new zoo is", len(new_zoo)
print "all animals in new zoo are", new_zoo

print "animals brought from old zoo are", new_zoo[2]
print "last animal brought from old zoo is", new_zoo[2][2]