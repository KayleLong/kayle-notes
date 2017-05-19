###### Date:2017.03.12
###### Code:Kayle Long
###### Note:《Python简明教程》中的实例 

### 3.最初的步骤

##### 3.1_hello

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

print 'Hello word' #井号“#”为注释符
print 'Hello word' #这个注释是为了出现滚动条，这是有道云笔记的一个bug吧。目前没有发现更好的办法，所以在第一个代码块中写入很长的注释，使得第一个代码块中会出现滚动条。
```
##### 输出结果

```
Hello word
```

### 4.基本概念

##### 4.1_var

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

i = 5
print 'i=%d' % (i)
i = i + 1
print 'i+1=%d' % (i)
s = '''This is a muti-line string.
This is the second line.''' #三个引号’，表示多行输出
print 's=%s' % (s)
```
##### 输出结果

```
i=5
i+1=6
This is a muti-line string.
This is the second line.
```


### 5.运算符与表达式

##### 5.1_expression


```
#!/usr/bin/env python
#-*- coding: utf-8 -*

length = 5
breadth = 2
area = length * breadth
# 字符串拼接，适用于参数少
print 'Area is', area
# 格式化输出，适用于多参数，类型少
print 'Area is %d' % (area)
# format()输出，适用于多参数，多类型，参数很灵活
print 'Area is {t_area}'.format(t_area=area)

print 'Perimeter is %d' % (2*(length+breadth))
print 'Perimeter is', 2*(length+breadth)
print 'Perimeter is {t_perimeter}'.format(t_perimeter=2*(length+breadth))
```

##### 输出结果

```
Area is 10
Area is 10
Area is 10

Perimeter is 14
Perimeter is 14
Perimeter is 14
```


### 6.控制流

##### 6.1_if

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

number = 23
guess = int(raw_input('Enter an intrger:'))

if guess == number:
	print 'Congratulations, you guessed it.'
elif guess < number:
	print 'No, it is a little higter than that.'
else:
	print 'No, it is a little lower than that.'
	
print 'Done'
```
##### 输出结果

```
Enter an intrger:50
No, it is a little lower than that.
Done

Enter an intrger:22
No, it is a little higter than that.
Done

Enter an intrger:23
Congratulations, you guessed it.
Done
```

##### 6.2_while

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

number = 23
running = True # 写成true,是错误的

while running:
  guess = int(raw_input('Enter an integer:'))
  if guess == number:
        print 'Congratulation, you guessd it.'
        running=False
  elif guess<number:
        print 'No, it is a little higher'
  else:
        print 'No, it is a little lower'
else:
  print 'the while loop is over.'
  
print 'Done'
```
##### 输出结果

```
Enter an intrger:50
No, it is a little higher

Enter an intrger:22
No, it is a little higher

Enter an intrger:23
Congratulation, you guessd it.
Done
```

##### 6.3_for

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

for i in range(1, 5): #相当于C语言中for(i=1;i<5;i++)，range 范围是左闭右开
	print 'i=', i
else:
	print 'The for loop is over.'
```
##### 输出结果

```
i=1
i=2
i=3
i=4
The for loop is over.
```

##### 6.4_break

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

while True:
	s = raw_input('Enter something:')
	if s == "quit": #在python2.7中，建议写成 if s=="quit"，使用'quit'会被认为是关键字
		break
	print 'Length of the string is', len(s)
	
print 'Done'
```
##### 输出结果

```
Enter something:abcde 
Lenght of the string is 5
Enter something:Quit
Lenght of the string is 4
Enter something:quit 
Done
```

##### 6.5_continue

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

while True:
	s = raw_input('Enter something:')
	if s == "quit":
		break #直接跳出整个循环
	if len(s) < 3:
		continue #跳出当前循环，然后继续进行下一个循环
	print 'Input is of sufficient length.'
```
##### 输出结果

```
Enter something:a
Enter something:12
Enter something:abc
Input is of siffcien lenth
Enter something:quit  
```


### 7.函数

##### 7.1_function

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

def say_hello():
	print 'Hello, welcome to Python.'

say_hello()
```
##### 输出结果

```
Hello, welcome to Python.
```

##### 7.2_parameter

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

def max(a, b):
	if a > b:
		print 'a=%d, b=%d,\na is max number.' %(a, b) #\n 是换行
	else:
		print 'a=%d, b=%d,\nb is max number.' %(a, b)

max(7, 5)
x = 100
y = 200
max(x, y)
```
##### 输出结果

```
a=7, b=5,
a is max number
a=100, b=200,
b is max number
```

##### 7.3_local

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

def local_para(x):
	print 'x is', x
	x = 2
	print 'Change local x is', x

x = 50
local_para(x)
print 'Value of x is', x
```
##### 输出结果

```
x is 50
Change local x is 2
Value of x is 50
```

##### 7.4_global

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

def global_para():
	global x
	print 'x is', x
	x = 2
	print 'Change global x is', x

x = 50
global_para()
print 'Value of x is', x
```
##### 输出结果

```
x is 50
Change local x is 2
Value of x is 2
```

##### 7.5_default

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

def say(message, times=2):
	print message * times
	
say('Hello ')
say('Python ', 5)
```
##### 输出结果

```
Hello Hello 
Python Python Python Python Python 
```

##### 7.6_key

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

def fun_key(a, b=5, c=10): #形参b和c，是默认参数。默认参数放在必选参数之后，避免歧义
	print 'a is %d, b is %d, c is %d' %(a, b, c)

fun_key(3, 7) #a=3,b=5,c=7
fun_key(25, c=24) #a=25,b=5,c=10
fun_key(c=50, a=100) #a=100,b=5,c=50
```
##### 输出结果

```
a is 3, b is 5, c is 7
a is 25, b is 5, c is 10
a is 10, b is 5, c is 50
```

##### 7.7_return

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

def maximum(x, y):
	if x > y:
		return x
	else:
		return y

print maximum(2, 3)
```
##### 输出结果

```
3
```

##### 7.8_docstring

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

def print_max(x, y):
	'''Print the maximum of two numbers
	
	The two values must be integers.''' #这是一个函数文档说明，第一行是开始，第二行是空白，第三行是详细说明
	x = int(x) #convert to integers, ifpossible
	y = int(y)
	
	if x>y:
		print '%d is maximum.' % (x)
	else:
		print '%d is maximum.' % (y)
		
print_max(3, 5)
print print_max.__doc__ #注意__是双下划线
```

##### 输出结果

```
5 is maximum.
Print the maximum of two numbers
	
	The two values must be integers.
```


### 8.模块

##### 8.1_using_sys

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

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
```
##### 输出结果

```
$python using_sys.py we are pythoner
using_sys.py 
we 
are 
pythoner

The Python Path is['/usr/lib/python2.7……']
```

##### 8.2_using_name

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

if __name__ == '__main__':
	print 'This program id being run by itself'
else:
	print 'I am being imported form anther module'
```
##### 输出结果

```
$python using_name.py
This program id being run by itself
>>> import using_name
I am being imported form anther module
```

##### 8.3_using_my_module

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

import my_module

my_module.say_hi()
print 'Version is %s' % (my_module.version)
```

##### my_module.py

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

def say_hi():
	print 'Hi, this is my module speaking.'

version = '0.1'
```

##### 输出结果

```
Hi, this is my module speaking.
Version is 0.1
```


### 9.数据结构

##### 9.1_using_list

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

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
```
##### 输出结果

```
I have 4 items to purchase.
These items are: apple mango carrot banana 
I also have to buy rice.
My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
The first item I will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
```

##### 9.2_using_tuple

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

zoo=("wolf", "elephant", "penguin")
print "number of animals in the zoo is", len(zoo)

new_zoo=("monkey", "dolphin", zoo) #在元组中包含另一个元组
print "number of animals in the new zoo is", len(new_zoo)
print "all animals in new zoo are", new_zoo

print "animals brought from old zoo are", new_zoo[2]
print "last animal brought from old zoo is", new_zoo[2][2]
```
##### 输出结果

```
number of animals in the zoo is 3
number of animals in the new zoo is 3
all animals in new zoo are ('monkey', 'dolphin', ('wolf', 'elephant', 'penguin'))
animals brought from old zoo are ('wolf', 'elephant', 'penguin')
last animal brought from old zoo is penguin
```

##### 9.3_print_tuple

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

age = 22
name = "Swaroop"

print '%s is %d years old' % (name, age)
print 'Why is %s playing with that python' % (name)
```
##### 输出结果

```
Swaroop is 22 years old
Why is Swaroop playing with that python
```

##### 9.4_using_dict

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

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
```
##### 输出结果

```
There are 4 contacts in the address-book
Contact swaroop at ...
Contact Larry
Contact Matsumoto
Contact Guido
```

##### 9.5_using_seq

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

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
```
##### 输出结果

```
Itme 0 is apple
Itme 1 is banana
Itme 2 is mango
Itme 3 is pear
Itme -1 is pear
Itme -2 is mango
Itme 1 to 3 is ['banana', 'mango']
Itme 2 to end is ['mango', 'pear']
Itme 1 to -1 is ['banana', 'mango']
Itme start to end is ['apple', 'banana', 'mango', 'pear']
chaeracters 1 to 3 is wa
chaeracters 2 to end is aroop
chaeracters 1 to -1 is waroo
chaeracters start to end is Swaroop
```

##### 9.6_using_reference

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

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
```
##### 输出结果

```
Simple A ssignment
shoplist is['apple', 'banana', 'pear', 'mango']
mylist is['apple', 'banana', 'pear', 'mango']
Copy by making a full slice
shoplist is['apple', 'banana', 'pear', 'mango']
mylist is['banana', 'pear', 'mango']
```

##### 9.7_str_method

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

name = 'Swaroop' #This is a string objet

if name.startswith('Swar'): #使用了 string的startswith()方法
	print 'Yes, the string startswith"Swar"'

if 'a' in name: #使用了 in 操作符
	print 'Yes, it contains the string "a"'

if name.find('war') != -1: #if not find, return -1
	print 'Yes, it contains the string"war"'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)
```
##### 输出结果

```
Yes, the string startswith"Swar"
Yes, it contains the string "a"
Yes, it contains the string"war"
Brazil_*_Russia_*_India_*_China
```


### 11.面向对象的编程

##### 11.1_silple_class

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

class Person:
	pass #An empty block

p = Person()
print p
```
##### 输出结果

```
<__main__.Person instance at 0x022E3800>
```

##### 11.2_mothod

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

class Person(object):
	def say_hi(self):
		print 'Hello, welcome to using the class\'s method'

p = Person()
p.say_hi()
```
##### 输出结果

```
Hello, welcome to using the class's method
```

##### 11.3_class_init

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

class Person(object):
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print 'Hello, my name is', self.name

p = Person('Anan')
p.say_hi()
```
##### 输出结果

```
Hello, my name is Anan
```

##### 11.4_class_objval

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

class Person(object):
	# Person属性
	popilation = 0

	# 初始化Person类的实例
	def __init__(self, name):
		self.name = name
		print 'Initializing %s' % (self.name)

		Person.popilation += 1

	# 销毁Person类的实例 
	def __del__(self):
		print '%s says bye' % (self.name)

		Person.popilation -= 1

		if Person.popilation == 0:
			print 'I\'m the last one.'
		else:
			print 'There are still %d people left.' % (Person.popilation)

	# 定义Person类的方法
	def say_hi(self):
		print 'Hi, my name is %s.' % (self.name)

	def howmany(self):
		if Person.popilation == 1:
			print 'I\'m the only person here.'
		else:
			print 'We are %d persons here.' % (Person.popilation)

swaroop = Person('Swaroop')
swaroop.say_hi()
swaroop.howmany()

kalam = Person('Abdul Kalam')
kalam.say_hi()
kalam.howmany()

swaroop.say_hi()
swaroop.howmany()
```
##### 输出结果

```
Hi, my name is
i+1=6
Hi, my name is
Hi, my name is
This is a muti-line string.
This is the second line.
```

##### 11.5_class_inherit

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

#这是一个父类
class School_member(object):
	'''Represents any school member'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print 'Initialized School_member: %s' % (name)

	def tell(self):
		'''Tell my details'''
		print 'Name:%s, Age:%s' % (self.name, self.age)

#这是一个继承自School_member父类的Teacher子类
class Teacher(School_member):
	"""Pepresets a teacher"""
	def __init__(self, name, age, salary):
		School_member.__init__(self, name, age)
		self.salary = salary
		print 'Initialized Teacher:%s' % (self.name)
	
	def tell(self):
		School_member.tell(self)
		print 'Salary:%d' % (self.salary)

#这是一个继承自School_member父类的Student子类
class Student(School_member):
	"""Pepresets a student"""
	def __init__(self, name, age, marks):
		School_member.__init__(self, name, age)
		self.marks = marks
		print 'Initialized Student:%s' % (self.name)
	
	def tell(self):
		School_member.tell(self)
		print 'marks:%d' % (self.marks)
						
t = Teacher('Mrs.Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)

print #prints a blak line

members = [t, s]
for member in members:
	member.tell ()
```
##### 输出结果

```
i=5
i+1=6
This is a muti-line string.
This is the second line.
```


### 12.输入/输出

##### 12.1_using_file

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

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
```
##### 输出结果

```
Programming is fun
When the work is done
if you wanna make your work also fun:
        use python!
```

##### 12.2_using_pickling

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

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
```
##### 输出结果

```
['apple', 'banana', 'mango', 'carrot']
```


### 13.异常

##### 13.1_try_exept

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

import sys

try:
	s = raw_input('Enter something ->')
except EOFError:
	print '\nWhy did you do an EOF on me?'
	sys.exit() #exit the program
except:
	print '\n Some error/exception occurred.'
	#Here, we are not excepting the program
print 'Done'
```
##### 输出结果

```
i=5
i+1=6
This is a muti-line string.
This is the second line.
```

##### 13.2_raising

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

class ShortInputException(Exception):
	"""A suer-defined exception class"""
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast
try:
	s = raw_input('Enter something ->')
	if len(s) < 3:
		raise ShortInputException(len(s), 3)
		#Other work can continue asusual here
except EOFError:
	print '\nWhy did you do an EOF on me?'
except ShortInputException, x:
	print 'ShortInputException:The input was of length %d was excepting at least %d' % (x.length, x.atleast)
else:
	print 'No exception was rasised.'
```
##### 输出结果

```
i=5
i+1=6
This is a muti-line string.
This is the second line.
```

##### 13.3_finally

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

import time

try:
	f = file('poem.txt')
	while Ture: #our usuall file-reading idiom
		line = f.readline()
		if len(line) == 0:
			break
		time.sleep(2)
		print line,
finally:
	f.close()
	print 'C leadning up...closed the file'
```
##### 输出结果

```
i=5
i+1=6
This is a muti-line string.
This is the second line.
```


### 14.Python标准库

##### 14.1_cat

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

import sys

def readfile(filename):
	'''Print a file to the standard output.'''
	f = file(filename)
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print line, #noticecomma
	f.close()

#Script starts from here
if len(sys.argv) < 2:
	print 'No action specified.'
	sys.exit()

if sys.argv[1].startswith('-'):
	option = sys.argv[1][2:]
	#fetch sys.argv[1], but without the first two characters
	if option == 'version':
		print 'Version 1.2'
	elif option == 'help'
		print '''\
This program prints files to the standard output
Any number of files can be specified.
Option include:
	-version :Print the version number
	-help :Display this help'''
	else:
		print 'Unknown option.'
	sys.exit()
else:
	for filename in sys.argv[1:]：
		readfile(filename)
```
##### 输出结果

```
i=5
i+1=6
This is a muti-line string.
This is the second line.
```


### 15.更多Python的内容

##### 15.1_list_comprehension

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i>2]
print listtwo
```
##### 输出结果

```
[4, 6, 8]
```

##### 15.2_lambda

```
#!/usr/bin/env python
#-*- coding: utf-8 -*

def make_repeter(n):
	return lambda s:s*n

twice = make_repeter(2)

print twice('word')
print twice(5)
```
##### 输出结果

```
word word
10
```