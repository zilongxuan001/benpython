test_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that")

stuff = test_things.split(" ")
print(stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff)!=10:
	next_one = more_stuff.pop()
	print("Adding: ",next_one)
	stuff.append(next_one)
	print("There's %d items now." %len(stuff))

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whaa！ fancy
print(stuff.pop())
print(" ".join(stuff)) #what?! cool
print("#".join(stuff[3:5])) #super stellar!







#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/	


# 当你看到像 mystuff.append('hello') 这样的代码时，你事实上已经在 Python 内部激发了一个连锁反应。以下是它的工作原理：

# 1.Python 看到你用到了 mystuff ，于是就去找到这个变量。也许它需要倒着检查看你有没有在哪里用 = 创建过这个变量，或者检查它是不是一个函数参数，或者看它是不是一个全局变量。不管哪种方式，它得先找到 mystuff 这个变量才行。
# 2.一旦它找到了 mystuff ，就轮到处理句点 . (period) 这个操作符，而且开始查看 mystuff 内部的一些变量了。由于 mystuff 是一个列表，Python 知道mystuff 支持一些函数。
# 3.接下来轮到了处理 append 。Python 会将 “append” 和 mystuff 支持的所有函数的名称一一对比，如果确实其中有一个叫 append 的函数，那么 Python 就会去使用这个函数。
# 4.接下来 Python 看到了括号 ( (parenthesis) 并且意识到, “噢，原来这应该是一个函数”，到了这里，它就正常会调用这个函数了，不过这里的函数还要多一个参数才行。
# 5.这个额外的参数其实是…… mystuff! 我知道，很奇怪是不是？不过这就是 Python 的工作原理，所以还是记住这一点，就当它是正常的好了。真正发生的事情其实是 append(mystuff, 'hello') ，不过你看到的只是 mystuff.append('hello') 。

#自己总结
#python如何读取mystuff.append("hello")
#（1）Python看到mystuff，就去寻找这个变量。看创建变量的位置，检查其是否是函数参数，或者是否是全局变量。
#（2）找到了mystuff，处理句点. 。查看mystuff内部变量，因为mystuff是个列表，所以Python知道mystuff支持列表的函数
#（3）处理append。将append的名称和mystuff支持的函数一一对比，如果有这个函数，则调用该函数。
#（4）处理括号。Python遇见括号，就知道这是个函数，开始调用函数。
#（5）如何调用函数。Python将apend('hello')转换为append(mystuff, 'hello')。


#字符串的split()用法
#（1）split自动去除字符串里的分割符（空格，换行符\n，制表符\t），返回含有该字符串的列表。
#（2）spilt(分隔符，数字)，这可以将字符串分割为“数字+1”部分。

# 参考：http://www.runoob.com/python/att-string-split.html

#字符串的join()用法
# （1）字符串.join(列表或元组)，将字符串加入列表中或元组中，返回字符串。

#参考：http://www.runoob.com/python/att-string-join.html

# 加分习题
# 将每一个被调用的函数以上述的方式翻译成 Python 实际执行的动作。例如： ' '.join(things) 其实是 join(' ', things) 。
# 将这两种方式翻译为自然语言。例如， ' '.join(things) 可以翻译成“用 ‘ ‘ 连接(join) things”，而 join(' ', things) 的意思是“为 ‘ ‘ 和 things 调用 join 函数”。这其实是同一件事情。
# 上网阅读一些关于“面向对象编程(Object Oriented Programming)”的资料。晕了吧？嗯，我以前也是。别担心。你将从这本书学到足够用的关于面向对象编程的基础知识，而以后你还可以慢慢学到更多。
# 查一下 Python中的 “class” 是什么东西。不要阅读关于其他语言的 “class” 的用法，这会让你更糊涂。
# dir(something) 和 something 的 class 有什么关系？
# 如果你不知道我讲的是些什么东西，别担心。程序员为了显得自己聪明，于是就发明了 Object Oriented Programming，简称为 OOP，然后他们就开始滥用这个东西了。如果你觉得这东西太难，你可以开始学一下 “函数编程(functional programming)”。