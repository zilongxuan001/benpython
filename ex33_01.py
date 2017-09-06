#--coding: utf-8 --
#Date:20170906

#不同数字测试

# def number(var):
	# i = 0
	# numbers = []
	# while i <var:
		# print("At the top i is %d"%i)
		# numbers.append(i)
		
		# i= i+1
		# print("Numbers now: ",numbers)
		# print("At the bottom i is %d" %i)

# number(6)
# print("\n...........")
# number(2)
# print("\n...........")
# number(-5)
# print("\n...........")
# number(0)
# print("\n...........")

#增加函数参数
# def number(var, x):
	# i = 0
	# numbers = []
	# while i <var:
		# print("At the top i is %d"%i)
		# numbers.append(i)
		
		# i= i+ x
		# print("Numbers now: ",numbers)
		# print("At the bottom i is %d" %i)

# number(6,2)
# print("\n...........")
# number(6,3)
# print("\n...........")
# number(7,4)


#重写脚本
# def number(var, x):
	# i = 0
	# numbers = []
	# while i <var:
		# print("At the top i is %d"%i)
		# numbers.append(i)
		
		# i= i+ x
		# print("Numbers now: ",numbers)
		# print("At the bottom i is %d" %i)
	# return numbers
	
# list=number(8,3)

# print("The numbers now:",)

# for num in list:
	# print(num)

	
#用for-loop和range写脚本

numbers =[]

for i in range(6):
	print("At the top i is %d"%i)
	numbers.append(i)
	
	# i= i+1
	print("Numbers now: ", numbers)
	print("At the bottom i is %d" %i)

print("The numbers: ")

for num in numbers:
	print(num)
	
# for循环中，i值没有受到 i=i+1的影响。
#如果去掉i=i+1,则At the bottom和At the top的值是一样的，但numbers不受影响。
	
	


