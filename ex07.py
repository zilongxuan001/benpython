#--coding: utf-8 --
#Date:20170815
#Title:ex07 更多打印

#打印：马瑞有一只小羊。
print('Mary had a little lamb.')

#打印：小羊的羊毛像雪一样白。
print('Its fleece was white as %s.'%'snow')

#打印：马瑞想去哪儿。
print('And everywhere what Mary went.')

#打印10个.  #这个是干什么的？
print('.'*10) #what'd that do?

#把‘C’赋值给end1
end1='C'

#把‘h’赋值给end2
end2='h'

#把‘e’赋值给end3
end3='e'

#把‘e’赋值给end4
end4='e'

#把‘s’赋值给给end5
end5='s'

#把‘e’赋值给end6
end6='e'

#把‘B’赋值给end7
end7='B'

#把‘u’赋值给end8
end8='u'

#把‘r’赋值给end9
end9='r'

#把‘g’赋值给end10
end10='g'

#把‘e’赋值给end11
end11='e'

#把‘r’赋值给end12
end12='r'



#观察最后面的逗号，试着去掉它，看能发生什么。
#watch that comma at the end. try removing it to see what happens

#打印：Cheese
print(end1 + end2 + end3 + end4 + end5  + end6,)

#打印：Burger
print(end7 + end8 + end9 + end10 + end11 + end12) 




#python3和python2不一样，python2在‘end6’后加上逗号，两个print可以合成一行，
#但在python3里是两行，只有在一个print里，在两个变量之间加上逗号，才能变成一行。

#打印：Cheese Burger
print(end1 + end2 + end3 + end4 + end5  + end6，end7 + end8 + end9 + end10 + end11 + end12)

#add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
#>逆向阅读，在每一行的上面加一行注解。
#>倒着朗读出来，找出自己的错误。
#>从现在开始，把你的错误记录下来，写在一张纸上。
#>在开始下一节习题时，阅读一遍你记录下来的错误，并且尽量避免在下个练习中再犯同样的错误。
#>记住，每个人都会犯错误。程序员和魔术师一样，他们希望大家认为他们从不犯错，不过这只是表象而已，他们每时每刻都在犯错。

#总结起来，就是
#1.加上注释。

#2.倒着朗读，找出错误。

#3.记录错误。

#4.回顾错误。
print('\n','add score 1','\n','------------------\n')
#加上注释。
#心得：
#如果字符串里有‘，则字符串两边最好加上" ",而不是'',这样就不会出现语法错误，也避免在字符串里使用转义符号\。

