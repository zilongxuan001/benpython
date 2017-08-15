#--coding: utf-8 --
#Date:20170815
#Title:ex08 打印，打印

#把 ’%r %r %r %r‘赋值给formatter.%r的意思是无论什么都打印出来，不限制格式。
formatter = '%r %r %r %r'

#打印1,2,3,4
print( formatter % (1, 2, 3, 4))

#打印‘one’，‘two’,‘three’,‘four’
print( formatter % ('one', 'two', 'three', 'four'))

#打印‘True’,‘False’,‘False’,‘True’
print( formatter % (True, False, False, True))

#打印四个’%r %r %r %r‘
print( formatter % (formatter, formatter, formatter, formatter))

#打印‘I had this thing.’‘That you could type up right’‘But it didn't sing’‘So I said goodnight.’
print( formatter % (
      "I had this thing.",
	  "That you could type up right.",
	  "But it didn't sing.",
	  "So I said goodnight.")
)
	  

#add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
#>自己检查结果，记录你犯过的错误，并且在下个练习中尽量不犯同样的错误。
#>注意最后一行程序中既有单引号又有双引号，你觉得它是如何工作的？

print('\n','add score 1','\n','------------------\n')
#加上注释

#add score
print('\n','add score 2','\n','------------------\n')	  
#错误
#1.拼写错误 fromatter——>formatter
#2.最后一个print,多个变量不加括号的错误，导致出现“参数不够”的提示。

#add score
print('\n','add score 3','\n','------------------\n')
# %r后的字符串，如果有字符串里有’，则打印时字符串两边出现"。如果字符串里没有‘，则字符串两边为’。