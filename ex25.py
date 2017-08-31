#--coding: utf-8 --
#Date:20170830
#Title:ex25 更多更多的练习

#使用.split方法，分割句子里的单词，放到一个list。
def break_words(stuff):
	'''This function will break up words for us.'''
#分割符为空格‘ ’，生成一个list，赋值给words
	words = stuff.split(' ')
	return words

#对单词进行排序
def sort_words(words):
	"""Sorts the word."""
#对list里的word进行排序，并将排序后的列表作为返回值
	return sorted(words)

#打印list中的第一个单词
def print_first_word(words):
	"""Prints the first word after popping it off."""
#通过pop删除list中的第一个单词，并将这个单词赋值给word
	word =  words.pop(0)
	print(word) 

#打印list的最后一个单词
def print_last_word(words):
	"""Prints the last word after popping it off."""
#通过pop删除list中的最后一个单词，并将这个单词赋值给word
	word = words.pop(-1)
	print(word)

#对句子进行排序
def sort_sentence(sentence):
	"""Takes in a  full sentence and returns the sorted words. """
#调用break_words()函数，将sentence变成list
	words = break_words(sentence)
#调用sort_words()函数，对list进行排序，并将排序后的列表作为sort_sentence()函数的返回值
	return sort_words(words)

#打印句子的第一个和最后一个单词
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
#调用break_words()函数，生成list，并赋值给words
	words = break_words(sentence)
#调用prit_first_word()函数
	print_first_word(words)
#调用prit_last_word()函数
	print_last_word(words)

#打印排序后的第一个和最后一个单词
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
#调用sort_setence()，对句子排序
	words = sort_sentence(sentence)
#调用prit_first_word()函数
	print_first_word(words)
#调用prit_first_word()函数
	print_last_word(words)

#如果要导入ex25，需要在Python 3.5.0 Shell里进入benpython文件夹。
# 加分题
# #引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# 研究答案中没有分析过的行，找出它们的来龙去脉。确认自己明白了自己使用的是模组 ex25 中定义的函数。
# 试着执行 help(ex25) 和 help(ex25.break_words) 。这是你得到模组帮助文档的方式。 所谓帮助文档就是你定义函数时放在 """ 之间的东西，它们也被称作 documentation comments （文档注解），后面你还会看到更多类似的东西。
# 重复键入 ex25. 是很烦的一件事情。有一个捷径就是用 from ex25 import * 的方式导入模组。这相当于说：“我要把 ex25 中所有的东西 import 进来。”程序员喜欢说这样的倒装句，开一个新的会话，看看你所有的函数是不是已经在那里了。
# 把你脚本里的内容逐行通过 python 编译器执行，看看会是什么样子。你可以执行CTRL-D (Windows 下是 CTRL-Z)来关闭编译器。
	
