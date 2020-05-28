###### Date:2017.05.18
###### Code:Kayle Long
###### Note:使用Python 3.5 安装IPython，遇到很多奇葩的问题。

## 参考链接

[ iPython的安装过程 ](http://blog.csdn.net/u012587561/article/details/50900781)

[Setuptools version 0.6c11 or greater has been installed 问题](http://www.oicqzone.com/pc/2016091523486.html)

[Centos6.7升级到Python3.5.2以及easy_install、pip的安装](http://blog.csdn.net/zhihaoma/article/details/52385947)


首先可以明确安装步骤为：
1. 下载，安装ez_setup.py
2. 在CMD 进入对应的目录下，执行python ez_setup.py 
3. 安装ipython

出现的问题：

1.Python3.5  安装ez_setup.py出现错误，

    File "ez_setup.py", line 106  
        except pkg_resources.VersionConflict, e:  

原因是因为这个py文件是用的python2的语法，改成python3的就可以了：
except pkg_resources.VersionConflict, e改成except pkg_resources.VersionConflict as e
print加括号。
再python ez_setup。

2.继续python ez_setup.py提示：
   
```
 Setuptools version 0.6c11 or greater has been installed.
    (Run "ez_setup.py -U setuptools" to reinstall or upgrade.)
```

    
解决方法：
使用命令

    python ez_setup.py build
    
    python ez_setup.py install
    
之后出现了

```
Setuptools version 0.6c11 or greater has been installed.
(Run "ez_setup.py -U setuptools" to reinstall or upgrade.)
```

[这时候需要安装pyreadline](https://pypi.python.org/pypi/pyreadline)
在大部分教程中都没有这一步。解压双击安装(Windows中IPython Notebook的安装需要pyreadline、pyzmq、tornado、mathjax等工具的支持.pyreadline 用于IPython颜色高亮)。最后输入 pip install ipython即可。

出现如下信息即表示安装IPython成功。
```
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' comm
and.
```

测试

输入pip --version

pip 1.5.6 from /usr/local/Python-3.5.2/lib/python3.5/site-packages/pip-1.5.6-py3.5.egg (python 3.5)