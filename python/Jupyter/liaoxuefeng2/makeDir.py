#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-26 11:41:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

with open('dirName.txt', 'r') as f:#open and read file
    str_dir = f.read()

list_dir = str_dir.split('\n')#split the string, then to list
for name in list_dir:
    #makedir
    #os.mkdir(name)
    #removedir
    os.rmdir(name)