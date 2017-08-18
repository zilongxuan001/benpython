#--coding: utf-8 --
#Date:20170818
#Title:ex12 提示别人


age= input('How old are you?')
height=input('How tall are you?')
weight=input('How much do you weigh?')

print("So, you're %r old , %r tall and %r heavy." %(age, height, weight))

#add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# >在命令行界面下运行你的程序，然后在命令行输入 pydoc raw_input 看它说了些什么。如果你用的是 Window，那就试一下 python -m pydoc raw_input 。
# >输入 q 退出 pydoc。
# >上网找一下 pydoc 命令是用来做什么的。
# >使用 pydoc 再看一下 open, file, os, 和 sys 的含义。看不懂没关系，只要通读一下，记下你觉得有意思的点就行了。

#在cmd里使用 python -m pydoc 函数名 时，如果函数的含义太多，会出现 --More-- ，如果不想看，就按q键，退出pydoc.
#pydoc可以查看函数介绍。