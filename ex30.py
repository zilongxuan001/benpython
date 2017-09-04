#--coding: utf-8 --
#Date:20170904
#Title:ex30 Else和if

#将30赋值给people,将40赋值给cars,将15赋值给buses.
people = 30
cars = 40
buses =15

#如果汽车比人多，则打印：“我们应该乘汽车。”
if cars > people:
	print("We should take the cars.")
#如果汽车比人少，则打印：“我们不应该乘汽车。”
elif  cars< people:
	print("We should not take the cars.")
#如果有其他情况，则打印：“我们决定不了。”
else:
	print("We can't decide.")

#如果巴士比汽车多，则打印：“太多巴士了。”
if buses>cars:
	print("That's too many buses.")
#如果巴士比汽车少，则打印：“我们应该乘坐巴士。”
elif buses<cars:
	print("Maybe we could take buses.")
#如果有其他情况，则打印：“我们仍然决定不了。”
else:
	print("We still can't decide.")

#如果人比巴士多，则打印：“好吧，让我们乘坐巴士。”
if people > buses:
	print("Alright, let's just take the buses.")
#如果有其他情况，则打印：“好吧，让我们待在家里。”
else:
	print("Fine, let's stay home again.")

#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/	
#ex29作者的解答
# 你认为 if 对于它下一行的代码做了什么？ If 语句为代码创建了一个所谓的“分支”，就跟 RPG 游戏中的情节分支一样。if 语句告诉你的脚本：“如果这个布尔表达式为真，就运行接下来的代码，否则就跳过这一段。”
# 为什么 if 语句的下一行需要 4 个空格的缩进？ 行尾的冒号的作用是告诉 Python 接下来你要创建一个新的代码区段。这根你创建函数时的冒号是一个道理。
# 如果不缩进, 会发生什么事情? 如果你没有缩进，你应该会看到 Python 报错。Python 的规则里，只要一行以“冒号(colon)” : 结尾，它接下来的内容就应该有缩进。
# 把习题 27 中的其它布尔表达式放到 if语句 中会不会也可以运行呢？试一下。 可以。而且不管多复杂都可以，虽然写复杂的东西通常是一种不好的编程风格。
# 如果把变量 people, cats, 和 dogs 的初始值改掉, 会发生什么事情? 因为你比较的对象是数字，如果你把这些数字改掉的话，某些位置的 if 语句会被演绎为 True，而它下面的代码区段将被运行。你可以试着修改这些数字，然后在头脑里假想一下那一段代码会被运行。

# ex30的加分习题
# 1.猜想一下 elif 和 else 的功能。
# 2.将 cars, people, 和 buses 的数量改掉，然后追溯每一个 if 语句。看看最后会打印出什么来。
# 3.试着写一些复杂的布尔表达式，例如 cars > people and buses < cars。
# 4.在每一行的上面写注解，说明这一行的功用。

#自己的回答：
#1.elif和else：if的判断语句不为真，如果elif的判断语句为真，则执行elif语句，跳过else语句。
#            如果if和elif的语句都不为真，则执行else语句。

#2.将if、elif和else执行一遍。
#第一种
# people = 70
# cars = 40
# buses =80

#第二种
# people = 70
# cars = 70
# buses =70

#3. 见ex30_01.py

