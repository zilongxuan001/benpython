#--coding: utf-8 --

from sys import argv

sricpt, filename=argv

# txt=open(filename,'w')
# print(txt.write('This is an egg.'))
# txt.close

txt=open(filename)
print(txt.read())

#直接打印write,显示的是字符串的字符数。
#通过read,显示的是文件内容。
#通过read,可以直接打开py文件内容哦。
#不能运行自己打开自己的文件。 即不能在cmd里 python ex15_04.py  ex15_04.py




