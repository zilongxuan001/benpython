#--coding: utf-8 --
#Date:20170823
#Title:ex18 命名、变量、代码、函数

#这个就像你的argv的脚本
#this one is like your scipts  with argv

#定义print_two函数，将args赋值给arg1和arg2,打印 arg1:  ,arg2:
def print_two(*args):
	arg1, arg2 =args
	print('arg1: %r , arg2: %r' %(arg1,arg2))

#o好了，这个*args确实没有意义，我们可以只这样做
#ok, that *arg is actually pointless, we can just do this 
#定义print_two_again函数，arg1和arg2作为参数，打印 arg1:  ,arg2:
def print_two_again(arg1, arg2):
	print('arg1: %r , arg2: %r' %(arg1,arg2))

#这个函数只接受一个参数
#this just takes one argument
#打印print_one函数，打印arg1:
def print_one(arg1):
	print('arg1: %r'%arg1)

#这个函数没有参数，打印 我什么都没得到。
#this one takes no argument
def print_none():
	print('I got nothin.')

#运行函数print_two,print_two_again,print_one,print_none
print_two('Zed','Shaw')
print_two_again('Zed','Shaw')
print_one('First!')
print_none()


# add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# 为自己写一个函数注意事项以供后续参考。你可以写在一个索引卡片上随时阅读，直到你记住所有的要点为止。注意事项如下：

# 函数定义是以 def 开始的吗？
# 函数名称是以字符和下划线 _ 组成的吗？
# 函数名称是不是紧跟着括号 ( ？
# 括号里是否包含参数？多个参数是否以逗号隔开？
# 参数名称是否有重复？（不能使用重复的参数名）
# 紧跟着参数的是不是括号和冒号 ): ？
# 紧跟着函数定义的代码是否使用了 4 个空格的缩进 (indent)？
# 函数结束的位置是否取消了缩进 (“dedent”)？

# 当你运行（或者说“使用 use”或者“调用 call”）一个函数时，记得检查下面的要点：

# 调运函数时是否使用了函数的名称？
# 函数名称是否紧跟着 ( ？
# 括号后有无参数？多个参数是否以逗号隔开？
# 函数是否以 ) 结尾？
# 按照这两份检查表里的内容检查你的练习，直到你不需要检查表为止。

# 最后，将下面这句话阅读几遍：

# “‘运行函数(run)’、‘调用函数(call)’、和 ‘使用函数(use)’是同一个意思”


