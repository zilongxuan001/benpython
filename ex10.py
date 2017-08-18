#--coding: utf-8 --
#Date:20170816
#Title:ex10 那是什么

print("I am 6'2\" tall.")
print('I am 6\'2" tall.')

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list;
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print( tabby_cat)
print( persian_cat)
print(backlash_cat)
print(fat_cat)



#add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# >上网搜索一下还有哪些可用的转义字符。
# >使用 ''' (三个单引号)取代三个双引号，看看效果是不是一样的？
# >将转义序列和格式化字符串放到一起，创建一种更复杂的格式。
# >记得 %r 格式化字符串吗？使用 %r 搭配单引号和双引号转义字符打印一些字符串出来。 将 %r 和 %s 比较一下。 注意到了吗？%r 打印出来的是你写在脚本里的内容，而 %s 打印的是你应该看到的内容。

print('\n','add score 1','\n','------------------\n')

#1.r ,显示带转义符的字符串
print(r'\tgood!')

#2.\，出现在行末，可以把两行显示为一行。

print('''This is a good day,\
just to play.''')

#3.\\,出现一个反斜杠\

print('\\You are a good boy.')

#4.\',\"，出现一个单引号，出现一个双引号。

print('I said,:\"Mum said \'it\' is a good apple.\"')


#5.\a ,带有系统响铃


print('\n','add score 2','\n','------------------\n')

print('\n','add score 3','\n','------------------\n')
fat_cat01 = '''
I'll do a list;
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(fat_cat01)
