#--coding: utf-8 --
#Date:20170822
#Title:ex17 更多文件操作

#从sys模块中导入argv
from sys import argv
#从os.path模块中导入exists 
from os.path import exists

#将argv赋值给script, from_file, to_file
script, from_file, to_file = argv

#打印:从from_file文件拷贝到to_file中。
print('Copying from %s to %s' %(from_file, to_file))

#我们能够把这两行变成一行，怎么弄？
#we could do these two on one line too,how?
#把打开from_file赋值给input
input= open(from_file)
#把可阅读赋值给indata.
indata= input.read()

#打印：输入文件的字符有多长。
print('The input file is %d bytes long' % len(indata))

#打印：输出文件是否存在？
print('Does the output file exist? %r' %exists(to_file))

#打印：准备好了，按return就继续，按CTRL-C就放弃。
print('Ready, hit RETURN to continue, CTRL -C to abort.')

#将打开可写的to_file文件赋值给output
output = open(to_file, 'w')
#在to_file里写入from_file的文件
output.write(indata)

#打印：写好了，结束。
print('Alright, all done.')

#关闭to_file文件
output.close()
#关闭from_file文件
input.close()



#exists:将文件名字符串作为参数，如果文件存在的话，它将返回 True，否则将返回 False。

# add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# 再多读读和 import 相关的材料，将 python 运行起来，试试这一条命令。试着看看自己能不能摸出点门道，当然了，即使弄不明白也没关系。
# 这个脚本 实在是 有点烦人。没必要在拷贝之前问一遍把，没必要在屏幕上输出那么多东西。试着删掉脚本的一些功能，让它使用起来更加友好。
# 看看你能把这个脚本改多短，我可以把它写成一行。
# 我使用了一个叫 cat 的东西，这个古老的命令的用处是将两个文件“连接(con*cat*enate)”到一起，不过实际上它最大的用途是打印文件内容到屏幕上。你可以通过 man cat 命令了解到更多信息。
# 使用 Windows 的同学，你们可以给自己找一个 cat 的替代品。关于 man 的东西就别想太多了，Windows 下没这个命令。
# 找出为什么你需要在代码中写 output.close() 。

#windows的cmd中的操作命令
#dir  显示所有文件名称
#start+文件名称或软件名称 可以打开该文件或软件
#more  读取文件内容