#--coding: utf-8 --
#Date:20170822
#Title:ex15 读取文件

#从sys模块中导入argv
from sys import argv

#把argv赋予给scipt和filename
script, filename =argv

#打开文件。
txt=open(filename)

#打印：这是你的文件：文件名。
print("Here's your file %r:" %filename)
#打印：文件内容
print(txt.read())

#打印：在打印文件名一次
print("Type the filename again:")
#输入>，文件名，赋值给file_again
file_again =input(">")

#打开文件
txt_again=open(file_again)

#打印文件内容。
print(txt_again.read())


#要运行ex15.py ,要提前加好文件 ex15_sample.txt，内容可以为
#This is stuff I typed into a file.
#It is really cool stuff.
#Lots and lots of fun to have in here.

#运行ex15.py：在cmd里输入 python ex15.py  ex15_sample.txt

# add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# 在每一行的上面用注解说明这一行的用途。
# 如果你不确定答案，就问别人，或者上网搜索。大部分时候，只要搜索 “python” 加上你要搜的东西就能得到你要的答案。比如搜索一下“python open”。
# 我使用了“命令”这个词，不过实际上它们的名字是“函数（function）”和“方法（method）。上网搜索一下这两者的意义和区别。看不明白也没关系，迷失在别的程序员的知识海洋里是很正常的一件事情。
# 删掉 10-15 行使用到 raw_input 的部分，再运行一遍脚本。
# 只是用 raw_input 写这个脚本，想想那种得到文件名称的方法更好，以及为什么。
# 运行 pydoc file 向下滚动直到看见 read() 命令（函数/方法）。看到很多别的命令了吧，你可以找几条试试看。不需要看那些包含 __ （两个下划线）的命令，这些只是垃圾而已。
# 再次运行 python 在命令行下使用 open 打开一个文件，这种 open 和 read 的方法也值得你一学。
# 让你的脚本针对 txt and txt_again 变量执行一下 close() ，处理完文件后你需要将其关闭，这是很重要的一点。


#pydoc用法：windows在cmd里输入 python -m pydoc open
