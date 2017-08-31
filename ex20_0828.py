#--coding: utf-8 --
#Date:20170828
#Title:ex20 函数和文件

from sys import argv

scipt, input_file =argv 

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
	print(line_count, f.readline())

current_file = open(input_file)

print("File let's print the whole file:\n")

print_all(current_file)

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line=current_line+1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)

#错误：出现：built-in method readline of _io.TextIOWrapper object at 0x0055B430
#原因：f.readline应该加()，