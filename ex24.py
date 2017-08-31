#--coding: utf-8 --
#Date:20170828
#Title:ex24 更多练习

print("Let‘s practice everything.")
print("You\'d need to know \'bout secape with \\ that do \n newlines and \t tabs.")

poem= """
\t The lovely world
with logic so firmly planted
connot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("----------------")
print(poem)
print("----------------")

five = 10 - 2 +3 -6
print("This should be five:%s" %five)



def secret_formula(started):
	jelly_beans =started *500
	jars = jelly_beans/1000
	crates = jars /100
	return jelly_beans, jars, crates


start_point  = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates."%(beans, jars, crates))

start_point =start_point/10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates."%secret_formula(start_point))


#新知识
#1. 如果def的函数return三个值的话，那么可以直接赋值给三个变量
#beans, jars, crates = secret_formula(start_point)

#2. 如果def的函数return三个值的话，那么可以在三个格式化符号后直接加上这个函数
# print("We'd have %d beans, %d jars, and %d crates."%secret_formula(start_point))

#加分题
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# 记得仔细检查结果，从后往前倒着检查，把代码朗读出来，在不清楚的位置加上注释。
# 故意把代码改错，运行并检查会发生什么样的错误，并且确认你有能力改正这些错误。
