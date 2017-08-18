from sys import argv

script, first, second, forth,fifth=argv

a=first
b=int(second)
c=input('input a string:')


print(first*b)
print(c*b)

print(forth+fifth)

#argv赋予给script, first, second, forth,fifth，
#在cmd里输入argv赋值的参数时，默认为输入的是字符串，不能输入句子。
#input()可以输入句子。