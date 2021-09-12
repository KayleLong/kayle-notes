## 这个test文件夹中.py程序是《简明 python 教程》中的例子。
2. 命名格式  
如：3.1_hello.py   3.1表示第3章第1个例子，hello为文件名称，旨在表达
输出的是hello word。
3.文件注释
```
#!/usr/bin/env python
#-*- coding: utf-8 -*
#@Code:Kayle Long
#@Date 2017.02.06

```
第一个注释是针对Mac/linux 系统，指定用什么解释器运行脚本以及解释器所在的位置
第二个注释是设置编译器当前编码格式

通常，python源代码必须完全由ASCII集合组成，如果直接在python中添加中文注释的时候，
python执行时会引发异常，告知非ASCII字符语法错误。
SyntaxError: Non-ASCII character '/xd5' in file D:/Project/python/sort/quick_sort.py on line 9,
but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
这个时候的解决方法，就是在告知python使用的编码方式，告知方法是在源文件的初始部分，
也就是顶行加上一行注释，
```
#-*- coding: utf-8 -*
```
必须是这一行，否则不起作用！

当使用Notepad++进行编写程序时，需要设置“格式”-->“以UTF-8 格式编码”