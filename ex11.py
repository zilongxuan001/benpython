#--coding: utf-8 --
#Date:20170818
#Title:ex11 提问

#打印：你几岁了？
print ('How old are you?')

#输入：岁数
age = input()

#打印：你多高？
print ('How tall are you?',)

#输入：高度
height = input()

#打印：你多重？
print('How much do you weigh?',)

#输入：重量
weight =input()

#打印：因此，你  几岁 ，多高 ，多重。
print("So, you're %r old, %r tall and %r heavy." %(age, height, weight))


#注意
#python3没有raw_input()函数了，只有input()函数。
#python3在每行的最后面加上逗号，不能把下边一行和本行合成一行

#add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# >上网查一下 Python 的 raw_input 实现的是什么功能。
# >你能找到它的别的用法吗？测试一下你上网搜索到的例子。
# >用类似的格式再写一段，把问题改成你自己的问题。
# >和转义序列有关的，想想为什么最后一行 '6\'2"' 里边有一个 \' 序列。单引号需要被转义，从而防止它被识别为字符串的结尾。有没有注意到这一点？

x=input('x=')
print(x)
print(x*3)
x= int(input('x='))
print(x*3)
#input()将所有的输入都按照字符串进行处理，并返回一个字符串