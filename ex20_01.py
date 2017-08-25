#实现从倒数一行往上读取文件。

from sys import argv

sccipt,input_file=argv

def print_all(f):
	print(f.read())

def print_one_line(line,f):
	print(line,f.readline(line))

def num_line(line):
	line=line-1
	return line

file= open(input_file)

print("This is the file:\n")
print_all(file)


print("\nLet's read the file from the last line:\n")

file.seek(0)

line1=file.readline()
line2=file.readline()
line3=file.readline()
line4=file.readline()
line5=file.readline()

print(line5,'\n',line4,line3,line2,line1)


#第一种方法：将file.readline()赋值给line X，然后倒着读取。
#第二种方法：将file.readline()赋值给line X，倒着导入另外一个文件，然后读取该文件。
#seek(0,2)是指针定位于文件的末尾，不是文件最后一行的开头。


