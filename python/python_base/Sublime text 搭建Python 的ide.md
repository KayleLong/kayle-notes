###### Date:2017.05.17
###### Code:Kayle Long
###### Note:相较于纯白如雪的原版idle,Sublime实在是色彩缤纷。将Sublime 搭建Python开发环境来促进学习和开发。

## 参考链接

[怎么用sublime text 3搭建python 的ide](https://www.zhihu.com/question/22904994)

[将Sublime Text 3设置为Python全栈开发环境](http://python.jobbole.com/81312/)

### 设置步骤
#### 1. 打开Sublime text  安装package control

Package Control用于管理安装插件，有了它就不需要自己去下载安装插件。

[Sublime Text 3 安装Package Control](http://www.cnblogs.com/luoshupeng/archive/2013/09/09/3310777.html)

#### 2.安装 SublimeREPL
用于让sublime里可以运行python xshell/Ipthon

Ctrl+shift+p 键入 install packages

![image](http://note.youdao.com/yws/api/personal/file/F950C65732404AF5ABD2BBF8C46883DE?method=download&shareKey=8629088d3ea8f2b9900957ecb726eff3)

稍等片刻后(有个下载的过程) 键入 SublimeREPL 安装即可

![image](http://note.youdao.com/yws/api/personal/file/61FBF591538740CCB7F9939DAF1F1F62?method=download&shareKey=8629088d3ea8f2b9900957ecb726eff3)

通过选项Tools->SublimeREPL->Python就可以看到效果了

![image](http://note.youdao.com/yws/api/personal/file/0FBBCFE5609E40C9A79E11389A21DBA3?method=download&shareKey=8629088d3ea8f2b9900957ecb726eff3)

#### 3. 键位绑定

当然每次通过Tools->SublimeREPL->Python这样的方式比较繁琐。
将这样的操作和一个按键如F1绑定后，就会方便很多啦。

e.g.打开Preferences->Key Bindings-User，复制一下代码：

```
{"keys":["f1"],//自己设置到的快捷键
"caption": "SublimeREPL: Python",
"command": "run_existing_window_command", "args":
{"id": "repl_python",
"file": "config/Python/Main.sublime-menu"}}
```

其实这是sublimerepl的配置文件，
"caption": "SublimeREPL: Python" 这句标签是指使用SublimeREPL中的Python，即原生的python。也可指定为Ipython。

![image](http://note.youdao.com/yws/api/personal/file/CEA3FE54F9924ED59CFD763193EC795A?method=download&shareKey=8629088d3ea8f2b9900957ecb726eff3)


#### Sublime插件安装
##### Anaconda

Anaconda是目前 Sublime 3 中最好的 Python 自动补全和语法提示插件, 并且提供了"跳转到定义", "查找使用", "显示文档", "自动重命名"等 IDE 中插件的功能.

## 有道云笔记 MarkDown 插入图片

1. 所有的图片放在一个专门的文件夹中，用普通模式设置同步笔记，然后设置为分享笔记。eg:Image
2. 设置为分享笔记之后，会有一个链接。使用浏览器进入链接，获取图片的网络地址（点击图片，右键-->复制图片地址）。再在Markdown文档中使用网络地址即可。