#--coding: utf-8 --
#Date:20170814
#Title:ex05 更多的变量和打印

my_name='Zed A. Shaw'
my_age=35 #not a lie
my_height=74 #inches
my_weight=180 #lbs ,磅
my_eyes='Blue'
my_teeth='White'
my_hair='Brown'

print('Let\'s talk about %s.' %my_name)
print('He\'s %d inches tall.' %my_height)
print('He\'s %d pounds heavy.' %my_weight)
print('Actually that\'s not too heavy.')
print('He\'s got %s eyes and %s hair.' %(my_eyes, my_hair))
print('His teeth are usually %s depending on the coffee.' %my_teeth)

#this line is tricky, try to get it exactly right
print('If I add %d, %d, and %d I get %d.' %(my_age, my_height, my_weight, my_age + my_height + my_weight))

#add score
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
#>修改所有的变量名字，把它们前面的``my_``去掉。确认将每一个地方的都改掉，不只是你使用``=``赋值过的地方。
#>试着使用更多的格式化字符。例如 %r 就是是非常有用的一个，它的含义是“不管什么都打印出来”。
#>在网上搜索所有的 Python 格式化字符。
#>试着使用变量将英寸和磅转换成厘米和千克。不要直接键入答案。使用 Python 的计算功能来完成。


print('\n','add score 1','\n','------------------\n')
name= 'Bruce Cao'
age= 32 # not a lie
height= 180 # cm
weight=140 #kg
eyes='Black'
teeth='Yellow'
hair='Black'

print('Let\'s talk about %s.' %name)
print('He\'s %d cm tall.' %height)
print('He\'s %d kg heavy.' %weight)
print('Actually that\'s not too heavy.')
print('He\'s got %s eyes and %s hair.' %(eyes,hair))
print('His teeth are usually %s depending on the coffee.' %teeth)

#this line is tricky,try to get it exactly right
print('If I add %d, %d, and %d  I get %d.' %(age, height, weight, age + height + weight))


#add score
print('\n','add score 2','\n','------------------\n')

age=30
name='GouSheng'
print('%r \'s age is %r' %(name, age))

#%r不考虑类型，是通用的格式化字符串

#add score
print('\n','add score 3','\n','------------------\n')

name=2
tian='good\n'
good=1865986
pi=356

print('%c' %name)
print('%+6d'%name)
print('%5s' %tian)
print('%r' %tian)
print('good is %#o' %good)
print('good is %+e' %good)
print('tian is %*s'%(15,tian))


student=[{'name':'wanger','grade':1},{'name':'zhaosi','grade':2}]
print('name: %10s,age:%10d'%(student[0]['name'],student[0]['grade']))
print('name: %*s,age:%0*d'%(10,student[1]['name'],10,student[1]['grade']))

h=123.2356
print('The tree is %.2f high.' %h)



#add score
print('\n','add score 4','\n','------------------\n')

height=74 #inches
weight=180 #lbs

print('He\'s %d inches.' %(height))
print('He is %d cm.\n' %(height*2.54))
print('He\'s %.2f lbs.'%(weight))
print('He is %.3f kg.' %(weight*0.4635924))
