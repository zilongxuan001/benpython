#--coding: utf-8 --
#Date:20170907
#Title:ex34 访问列表的元素 Accessing Elements of Lists

animals=['bear','python','peacock','kangaroo','whale','platypus']

print("The animal at 1 is the 2nd animal and is a %s." %animals[1])

print("The 3rd animal is at 2 and is a %s. "%animals[2])

print("The 1st animlal is at 0 and is a %s."%animals[0])

print("The animal at 3 is the 4th animal and is a %s."%animals[3])


print("The 5th animal is at 4 and is a %s." %animals[4])

print("The animal at 2 is the 3rd animal and is a %s."%animals[2])

print("The 6th animal is at 5 and is a %s."%animals[5])

print("The animal an 4 is the 5th animal and is a %s."%animals[4])

















#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/	

#知识
#“序数(ordinal number)”，表示的是事物的顺序。ordinal == 有序，以 1 开始；
#“基数(cardinal number)”:基数里的元素就像卡片，可以任意抓取，从0开始。cardinal == 随机选取, 以 0 开始。
# 换算： 基数=序数-1

# 列表的每一个元素都有一个地址，或者一个 “index（索引）”，而最好的方式是使用以 0 开头的索引。


#加分题
# 1.上网搜索一下关于序数(ordinal number)和基数(cardinal number)的知识并阅读一下。
# 2.以你对于这些不同的数字类型的了解，解释一下为什么 “January 1, 2010” 里是 2010 而不是 2009？（提示：你不能随机挑选年份。）
# 3.再写一些列表，用一样的方式作出索引，确认自己可以在两种数字之间互相翻译。
# 4.使用 python 检查自己的答案。

#1.序数就是表示是第几个数。
#2.因为没有公元0年，2010是个序数，而不是一个基数。