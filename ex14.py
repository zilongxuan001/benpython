#--coding: utf-8 --
#Date:20170821
#Title:ex14 提示和传递

#从模组sys导入函数argv
from sys import argv

#将argv赋予给script和user_name
script, user_name= argv

#将>赋予给prompt
prompt = ' >'

#打印：你好，XX，我是XX的脚本
print("Hi %s, I'm the %s script." %(user_name, script))

#打印：我喜欢问你几个问题。
print("I'd like to ask you a few questions.")

#打印：你喜欢我吗？XX
print('Do you like me, %s?' %user_name)

#打印>，将输入值赋予给likes
likes =  input(prompt)

#打印：你住在哪里？XX
print('Where do you live, %s?' % user_name)
#打印>，将输入赋予给lives
lives = input(prompt)

#打印：你有什么样的电脑？
print('What kind of computer do you have?')
#打印>，将输入赋予给compuders.
computer = input(prompt)

#打印：好吧，如此你说你是否喜欢我。你住在XX。不确定是在哪里。你有一个XX电脑，真好。
print("""
Alrigt, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))



#add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# >查一下 Zork 和 Adventure 是两个怎样的游戏。 看看能不能下载到一版，然后玩玩看。
# >将 prompt 变量改成完全不同的内容再运行一遍。
# >给你的脚本再添加一个参数，让你的程序用到这个参数。
# >确认你弄懂了三个引号 """ 可以定义多行字符串，而 % 是字符串的格式化工具。


#print和()之间不能有空格。
#print("Hi %s, I'm the %s script." %(user_name, script)少了一个括号，
#应为print("Hi %s, I'm the %s script." %(user_name, script)))

#运行ex14.py——在cmd里输入 python ex14.py username。

