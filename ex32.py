the_count= [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'appicous']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
	print("This is count %d" %number)

# same as above
for fruit in fruits:
	print("A fruit of type: %s" %fruit)

#also we can go through mixes lists too
#notice we have to use %r since we don't know what's in it
for i in change:
	print("I got %r"%i)

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print("Adding %d to the list." %i)
	#append is a function that lists understand
	elements.append(i)

#now we can print them out too
for i in elements:
	print("Element was: %d" %i)

#面对不会的东西时，你应该怎么做？

# 习惯性思维告诉你的大脑大地是平的。记得上一个练习中的 if 语句嵌套吧，你可能觉得要理解它有些难度，因为生活中一般人不会去像这样的问题，但这样的问题在编程中几乎到处都是。你会看到一个函数调用另外一个包含 if 语句的函数，其中又有嵌套列表的列表。
# 如果你看到这样的东西一时无法弄懂，就用纸笔记下来，手动分割下去，直到弄懂为止。

#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/	
#加分题
# 1.注意一下 range 的用法。查一下 range 函数并理解它。
# 2.在第 22 行，你可以不可以直接将 elements 赋值为 range(0,6)，而无需使用 for 循环？
# 3.在 Python 文档中找到关于列表的内容，仔细阅读以下，除了 append 以外列表还支持哪些操作？


#1. range用法
# （1） range(1,5) 从1到5，但不包含5
# （2） range(1,5,2) 从1到5，但不包含5，间隔2
# （3） range(5)   从0到5，但不包含5

#2. 可以
# elements.append(0)
# elements.append(1)
# elements.append(2)
# elements.append(3)
# elements.append(4)
# elements.append(5)

#3. list的操作
#（1）pop 删除某个位置上的元素,返回的是删除的元素  
# 例如 删除末尾元素 elements.pop()
#      删除特定位置元素 elements.pop(4)

#（2）del 删除某个位置上的元素，直接删除
# 例如  del elements[0]

#（3）inert 在某个位置上插入某个元素 insert(插入位置，元素名称)
# 例如 elements.insert(3,'good')

# （4）remove 删除某元素,若list里有多个相同元素，则删除第一个相同元素。
# 例如  elements.remove('good')

#（5）count 计算该元素在list中出现的次数。
#例如 elements.count('good')

# (6) index 计算该元素在list中的位置，如该元素不存在，则抛出异常。如有多个相同元素，则给出第一个元素位置。
#例如 elements.index('good')

# （7）append 在列表末尾添加元素
#例如 elements.append(4) 

# （8）extend  将某个列表中的元素合并到列表的末尾
#例如  elements.extend(['today','morning'])

# （9）sort 对列表的元素进行排序,同时存在字符串和数字，则无法排序。
#例如 elements.sort()

# （10）reverse 对列表的元素进行倒序,同时存在字符串和数字，则无法排序。
#例如 elements.reverse()
