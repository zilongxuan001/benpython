#--coding: utf-8 --
#Date:20170825
#Title:ex21 函数可以返回东西

#定义函数add,打印“ADDING a+b”,返回a+b的和
def add(a,b):
	print("ADDING %d +%d" %(a,b))
	return a+b

#定义函数subtract,打印“SUBTRACT a-b”,返回a-b的差
def subtract(a,b):
	print("SUBTRACT %d - %d" % (a,b))
	return a-b

#定义函数multiply,打印：“MULTIPLYING a*b”,返回a*b的乘积
def multiply(a, b):
	print("MULTIPLYING %d * %d" %(a,b))
	return a * b

#定义函数divide,打印：“DIVIDING a/b”,返回a/b
def divide(a,b):
	print("DIVIDING %d / %d" %(a,b))
	return a/b

#打印：让我们用这些函数做些数学题。
print("Let's go some math with just functions!")

#将add(30,5)的值赋值给age
age =add(30,5)

#将subtract(78,4)的值赋给height
height= subtract(78,4)

#将multiply(90,2)的值赋给weight
weight = multiply(90,2)

#将divide(100,2)的值赋值给iq
iq = divide(100,2)

#打印：Age:   ,Height:   ,Weight:  ,IQ:  .
print("Age: %d, Height: %d, Weight: %d, IQ: %d" %(age,height, weight,iq))

#有一个额外的小谜题，打印出来
#A puzzle for the extra credit, type it in anyway.
#打印：这里有一个谜题。
print("Here is a puzzle.")

#将divibe(),multiply(),subtract(),add()函数调用一遍，将值赋给what

#what=age+（height-（weight*(iq/2)））
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

#打印： 这个值是  ，你能用手算出来吗？
print("That becomes:",what,"Can you do it by hand?")

what_01=age+(height-(weight *(iq/2)))
print("what_01=age+(height-(weight *(iq/2)))")
print("I type the same :",what_01)

d=divide(iq,2)
m=multiply(weight,d)
s=subtract(height,m)
what_02=add(age,s)

print("I do it again:%d",what_02)

what_03 = add(5, subtract(6, multiply(7, divide(2,2))))
print("I change the numbers:%d"%what_03)


# add score
# #引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# 如果你不是很确定 return 的功能，试着自己写几个函数出来，让它们返回一些值。你可以将任何可以放在 = 右边的东西作为一个函数的返回值。
# 这个脚本的结尾是一个迷题。我将一个函数的返回值用作了另外一个函数的参数。我将它们链接到了一起，就跟写数学等式一样。这样可能有些难读，不过运行一下你就知道结果了。接下来，你需要试试看能不能用正常的方法实现和这个表达式一样的功能。
# 一旦你解决了这个迷题，试着修改一下函数里的某些部分，然后看会有什么样的结果。你可以有目的地修改它，让它输出另外一个值。
# 最后，颠倒过来做一次。写一个简单的等式，使用一样的函数来计算它。
# 这个习题可能会让你有些头大，不过还是慢慢来，把它当做一个游戏，解决这样的迷题正是编程的乐趣之一。后面你还会看到类似的小谜题。


























