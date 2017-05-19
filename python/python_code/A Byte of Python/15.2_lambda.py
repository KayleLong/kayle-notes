#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

def make_repeter(n):
	return lambda s:s*n

twice = make_repeter(2)

print twice('word')
print twice(5)