#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
	use python!
'''

f = file('poem.txt', 'w') #open for 'w'riting
f.write(poem) #write text to file
f.close() #remenber to close the file

f =  file('poem.txt') #if nomode is specified, 'r'ead mode is assumed by default
while True:
	line = f.readline()
	if len(line) == 0: #Zero length in dicates EOF
		break
	print line, #Notice comma to avoid to matic new line added by python
	# 注意 line,后面加个一个逗号，作用是用于消除自动换行
f.close()