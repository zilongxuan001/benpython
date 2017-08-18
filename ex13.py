
#导入模组sys。
from sys import argv


#将argv解包（unpack）,将所有的参数依次赋予给左边的script, first,second,third.
script,first,second, third =argv

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)

#在cmd里运行 python ex13.py  。其中ex13.py就是一个参数（argument）。

#如何运行ex13.py程序？ 在cmd里输入
#python ex13.py first 2nd 3rd
#python ex13.py cheese apples bread
#python ex13.py Zed A. Shaw
#注：其实，你在python ex13.py 后面输入任意三个参数都可以。


#脚本，就是你写的.py程序。
#argv，即 argument variable ,参数变量。
#模组，modules,又称库（libraries）

#add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# >给你的脚本三个以下的参数。看看会得到什么错误信息。试着解释一下。
# >再写两个脚本，其中一个接受更少的参数，另一个接受更多的参数，在参数解包时给它们取一些有意义的变量名。
# >将 raw_input 和 argv 一起使用，让你的脚本从用户手上得到更多的输入。
# >记住“模组(modules)”为你提供额外功能。多读几遍把这个词记住，因为我们后面还会用到它。

#如果运行ex13.py, 输入三个以下的参数，会出现 值错误：没有足够的值去解包（期待4个，得到3个）
##argv赋予给script, first, second, forth,fifth，
#在cmd里输入argv赋值的参数时，默认为输入的是字符串，不能输入句子。
#input()可以输入句子。
