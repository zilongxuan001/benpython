#--coding: utf-8 --
#Date:20170906

#��ͬ���ֲ���

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

#���Ӻ�������
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


#��д�ű�
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

	
#��for-loop��rangeд�ű�

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
	
# forѭ���У�iֵû���ܵ� i=i+1��Ӱ�졣
#���ȥ��i=i+1,��At the bottom��At the top��ֵ��һ���ģ���numbers����Ӱ�졣
	
	


