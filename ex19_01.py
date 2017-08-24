from sys import argv

script, user, num01,num02=argv

num01=int(num01)
num02=int(num02)

def num(man,num1,num2):
	print('Hello,%s!'%user)
	print('you will get %r!'%(num1+num2))
	

num(user,num01,num02)


apple=int(input('apple '))
orange=int(input('orange '))

num(user,apple,orange)