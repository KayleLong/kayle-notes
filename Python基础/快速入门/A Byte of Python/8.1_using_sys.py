#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

import sys

print 'The command line arguments:' #输出 输入的命令，例如 Python 8.1_using_sys.py we are Pythoner
#运行程序后，输出如下：
#8.1_using_sys.py
#we
#are
#Pythoner
for i in sys.argv:
	print i

print '\n\nThe Python Path is %s \n' % (sys.path) #输出Path环境变量