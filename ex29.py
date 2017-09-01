#--coding: utf-8 --
#Date:20170901
#Title:ex29 如果(if)


people =20
cats =30
dogs =15

if people < cats:
	print("Too many cats! The world is doomed!")

if people> cats:
	print("Not many cats! The world is saved!")

if people < dogs:
	print("The world is drooled on!")

if people > dogs:
	print("The world is dry!")

dogs +=5

if people >=dogs:
	print("People are greater than or equal to dogs.")

if people <=dogs:
	print("People are less than or equal to dogs.")

if people ==  dogs:
	print("People are dogs.")

#加分题
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/	
# 猜猜“if语句”是什么，它有什么用处。在做下一道习题前，试着用自己的话回答下面的问题:

# 1.你认为 if 对于它下一行的代码做了什么？
# 2.为什么 if 语句的下一行需要 4 个空格的缩进？
# 3.如果不缩进，会发生什么事情？
# 4.把习题 27 中的其它布尔表达式放到``if语句``中会不会也可以运行呢？试一下。
# 5.如果把变量 people, cats, 和 dogs 的初始值改掉，会发生什么事情？

##回答
#1.如果if下面的语句是真的，则执行下面语句；如果不是，则不执行。
#2.缩进为了表示和if是一个代码块的，受if控制。
#3.如果不缩进，则该行不受if控制。
#4.好的。
#5.初始值变化，则if的判断条件变化。

