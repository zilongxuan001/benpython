#--coding: utf-8 --
#Date:20170822
#Title:ex16 读写文件

#从sys模块中导入argv
from sys import argv

#将argv赋值给scipt和filename
script, filename =argv

#打印：我们要清除文件的内容
print("We're going to erase %r."%filename)
#打印：如果你不想清除，请按CTRL-C
print("If you don't what that, hit CTRL-C (^C).")
#打印：如果你想清除，点击RETURN.
print('If you do want that, hit RETURN.')

#输入？ 
input('?')

#打印：打开文件
print('Opening the file...')
#打开文件，可以写入，这个函数赋给target
target = open(filename,'w')

#打印：清空文件，再见！
print('Truncating the file. Goodblye!')
#清空文件
target.truncate()

#打印：现在，我要你写三行。
print("Now I'm going to ask you for three line.")

#输入第一行，并赋值给line1
line1 = input('line 1: ')
#输入第二行，并赋值给line2
line2 = input('line 2: ')
#输入第三行，并赋值给line3
line3 = input('line 3: ')

#打印：我要把这些写入文件了。
print("I'm going to write these to the file.")

#写入第一行。
target.write(line1)
#另起一行。
target.write('\n')
#写入第二行。
target.write(line2)
#另起一行。
target.write('\n')
#写入第三行。
target.write(line3)
#另起一行。
target.write('\n')


#结束了，我们关闭文件。
print('And finally, we close it.')
#关闭文件。
target.close()

#打开文件，权限为只读，赋予给good。
good=open(filename,'r')

#打印：文件第一行。
print(good.readline())
#打印：文件剩余内容。
print(good.read())



#写大文件技巧：可以先写几行，运行起来。再写五行，再运行起来。直到整个脚本运行起来。
#open(filename,'w')，可以write，可以truncate,可以关闭，但不能read。
#read如果在readline前先执行，那么readline就读取的文件内容为空。
#read如果在readline后执行，那么read读取的是readline读取后剩下的内容。
#如何运行? 在cmd里输入 python ex16.py filename。如果file没有建立的话，会自动建立一个以filename命名的文件。

# add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# 如果你觉得自己没有弄懂的话，用我们的老办法，在每一行之前加上注解，为自己理清思路。就算不能理清思路，你也可以知道自己究竟具体哪里没弄明白。
# 写一个和上一个练习类似的脚本，使用 read 和 argv 读取你刚才新建的文件。
# 文件中重复的地方太多了。试着用一个 target.write() 将 line1, line2, line3 打印出来，你可以使用字符串、格式化字符、以及转义字符。
# 找出为什么我们需要给 open 多赋予一个 'w' 参数。提示： open 对于文件的写入操作态度是安全第一，所以你只有特别指定以后，它才会进行写入操作。



# close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
# read – 读取文件内容。你可以把结果赋给一个变量。
# readline – 读取文本文件中的一行。
# truncate – 清空文件，请小心使用该命令。
# write(stuff) – 将stuff写入文件。