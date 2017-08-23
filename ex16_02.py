#从sys模块中导入argv
from sys import argv

#将argv赋值给scipt和filename
script, filename =argv

#打印：我们要清除文件的内容
print("We're going to erase %r."%filename)
#打印：如果你不想清除，请按CTRL-C
print("If you don't what that, hit CTRL-C (^C).")
#打印：如果你想清除，点击RETURN.
print('If you do want that, hit RETURN.')

#输入？ 
input('?')

#打印：打开文件
print('Opening the file...')
#打开文件，可以写入，这个函数赋给target
target = open(filename,'w')

#打印：清空文件，再见！
print('Truncating the file. Goodblye!')
#清空文件
target.truncate()

#打印：现在，我要你写三行。
print("Now I'm going to ask you for three line.")

#输入第一行，并赋值给line1
line1 = input('line 1: ')
#输入第二行，并赋值给line2
line2 = input('line 2: ')
#输入第三行，并赋值给line3
line3 = input('line 3: ')

#打印：我要把这些写入文件了。
print("I'm going to write these to the file.")


target.write(line1+'\n'+line2+'\n'+line3+'\n')


#结束了，我们关闭文件。
print('And finally, we close it.')
#关闭文件。
target.close()

#打开文件，权限为只读，赋予给good。
good=open(filename,'r')

#打印：文件第一行。
print(good.readline())
#打印：文件剩余内容。
print(good.read())