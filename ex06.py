#--coding: utf-8 --
#Date:20170815
#Title:ex06 字符串(string)和文本

#把"这里有10种类型的人"赋值给x
x='There are %d types of people.' %10

#把”二级制“赋值给binary
binary ='binary'

#把“don't”赋值给do_not
do_not='don\'t'

#把“知道二进制的人和不知道的人”赋值给y
y= 'Those who know %s and those who %s.' %(binary,do_not)

#打印x
print(x)

#打印y
print(y)

#打印：我说这里有10种类型的人。
print('I said: %r.' %x)

#打印：我也说过：知道二进制的人和不知道的人。
print('I also said:\'%s\'.'%y)

#把“错误”赋值给hilarious(令人捧腹的)
hilarious=False
#把“这个笑话好笑吗？“赋值给joke_evaluation(笑话评价)
joke_evaluation ='Isn\'t that joke so funny?! %r'

#打印：这个笑话好笑吗？不好笑
print(joke_evaluation % hilarious)

#把“这是左边的....”赋值给w
w='This is the left side of...'

#把“右边的字符串”赋值给e
e='a string with a right side.'

#打印；“这是左边的....右边的字符串”
print(w+e)


#add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
#>通读程序，在每一行的上面写一行注解，给自己解释一下这一行的作用。
#>找到所有的”字符串包含字符串”的位置，总共有四个位置。
#>你确定只有四个位置吗？你怎么知道的？没准我在骗你呢。
#>解释一下为什么 w 和 e 用 + 连起来就可以生成一个更长的字符串。

print('\n','add score 1','\n','------------------\n')

#加上注释

#add score
print('\n','add score 2','\n','------------------\n')

#找出4个字符串包含字符串的位置
#y= 'Those who know %s and those who %s.' %(binary,do_not)
#print('I said: %r.' %x)
#print('I also said:\'%s\'.'%y)
#print(joke_evaluation % hilarious)

#add score
print('\n','add score 3','\n','------------------\n')
#确定只有四个位置，是字符串包含字符串。

#add score
print('\n','add score 4','\n','------------------\n')

#字符串可以相加，相乘

a="a big apple. "
apple='apple'
I="Tom's %s is "
Tom=I % apple


print(Tom+a)
print(a*3)
print(Tom+a*3)


