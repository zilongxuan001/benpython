#--coding: utf-8 --
#Date:20170825
#Title:ex20 函数和文件

#从模块sys导入argv
from sys import argv

#将argv赋值给script和input_file，即cmd输入时要加上文件名
script, input_file =argv

#定义函数print_all，功能是读取一个文件
def print_all(f):
	print(f.read(),'\n')

#定义函数rewind，功能是从新开始读取文件。
def rewind(f):
	f.seek(0)
#定义函数print_a_line，功能是输出1个值，读取文件1行。
def print_a_line(line_count,f):
	print(line_count,f.readline())

#将打开输入文件赋值给current_file
current_file = open(input_file)

#打印：首先，我们打印所有的文件
print("First let's print the whole file:\n")

#运行print_all，打印文件所有内容
print_all(current_file)

#打印：现在，让我们重新读取，就像录音机。
print("Now let's rewind,kind of like a tape.\n")

#将指针指向文件第一行
rewind(current_file)

#打印：让我们开始打印三行
print("Let's print three lines:")

#将1赋值给current_line
current_line = 1
#将current_line和current_file传入print_a_line，打印1和第一行
print_a_line(current_line,current_file)

#current_line加1
current_line= current_line + 1
#将current_line和current_file传入print_a_line，打印2和第二行
print_a_line(current_line,current_file)

#current_line加1
current_line= current_line+1
#将current_line和current_file传入print_a_line，打印3和第三行
print_a_line(current_line,current_file)

#将指针定位于第一行，偏移2个字符，从第一行第三个字符开始
current_file.seek(2,0)

#打印：文件第一行，从第一行第三个字符开始读取。
print('\n',current_file.readline())
#打印：打印剩余部分。
print('\n',current_file.read())


 

#file.seek(),seek是个指针，指向文件的各行，file.seek()可以让文件从头开始读取，无file.seek ,则f.readline()无读取的数据。
#seek()默认值是0，意思为指向文件开头。
#值为1，则从当前位置开始，值为2，则是指向文末结束位置。

# add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# 通读脚本，在每行之前加上注解，以理解脚本里发生的事情。
# 每次 print_a_line 运行时，你都传递了一个叫 current_line 的变量。在每次调用函数时，打印出 current_line 的值，跟踪一下它在 print_a_line 中是怎样变成 line_count 的。
# 找出脚本中每一个用到函数的地方。检查 def 一行，确认参数没有用错。
# 上网研究一下 file 中的 seek 函数是做什么用的。试着运行 pydoc file 看看能不能学到更多。
# 研究一下 += 这个简写操作符的作用，写一个脚本，把这个操作符用在里边试一下。

#自己尝试
#增加了
#current_file.seek(0)
# print('\n',current_file.readline())
# print('\n',current_file.read())
#试试把current_file.seek(0)改成
#current_file.seek(0,1) 0表示无字符偏移，1表示从当前位置开始
#current_file.seek(2,0) 2表示从偏移2个字符，从第三个字符开始读取。0表示从头开始。