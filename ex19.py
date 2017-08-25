#--coding: utf-8 --
#Date:20170824
#Title:ex19 函数和变量

#定义函数cheese_and_crackers()
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#打印：有多少个奶酪。
	print('You have %d cheeses!'%cheese_count)
	#打印：你有多少盒饼干。
	print('You have %d boxes of crackers!'%boxes_of_crackers)
	#聚会的人够了。
	print("Man that's enough for a party!")
	#打印：给个毯子。
	print('Get a blanket.\n')

#打印：我们能够直接给两个功能数字。
print('We are just give the function numbers directly:')

#将20和30传入cheese_and_crackers()函数里。
cheese_and_crackers(20, 30)

#打印：哦，我可以用我们脚本里的变量
print('OR, we can use variables from our script:')
#将10赋值给变量amount_of_cheese
amount_of_cheese =10

#将50赋值给变量amount_of_crackers
amount_of_crackers = 50

#将参数amount_of_cheese,amount_of_crackers传到cheese_and_crackers函数里
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#打印：我们甚至能进行数学运算，再传到函数里
print('We can even do math inside too:')
#将参数10 + 20, 5+60传到cheese_and_crackers函数里
cheese_and_crackers(10 + 20, 5+6 )

#打印：我们能能够将变量和数学联合，再传入参数。
print('And we can combine the two, variables and math:')

#将参数amount_of_cheese+100, amount_of_crackers+1000传到cheese_and_crackers函数里
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)


# add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# 倒着将脚本读完，在每一行上面添加一行注解，说明这行的作用。
# 从最后一行开始，倒着阅读每一行，读出所有的重要字符来。
# 自己编至少一个函数出来，然后用10种方法运行这个函数。

#感悟：
#自定义函数，有标签——def ,说明我要定义一个函数了。
#有函数名称，说明我要定义的函数叫什么名字，方便你调用。
#有输入的原料（参数），这是要加工的原料。
#有操作流程(函数体)，对原料进行加工。
#有输出（返回），就是加工后的成品。
#一个函数就是一把雕刻刀，对原料进行加工，雕刻成佛像，或者玩偶。
#一个函数就是一个模具，原料进去，模型出来。
#变量就是一个杯子，你往里面倒进去什么，他就是什么。
#函数的参数就是输入，返回就是输出，有return就输出一个值，没return就输出一个None.