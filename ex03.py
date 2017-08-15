# -- coding: utf-8 --
#Date:20170811
#Title:ex03 数字和数学计算

#打印 I will now count my chickens:
print( 'I will now count my chickens:')

#计算Hens的数量 ,Hens=25+30/6
print('Hens',25 +30 /6)
#计算Roosters的数量 Roosters=100-25*3%4
print('Roosters', 100 -25 * 3 %4)

#打印 Now I will count the eggs:
print('Now I will count the eggs:')

#计算 3+2+1-5+4%2-1/4+6的值
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 +6)

#打印 Is it true that 3+2<5-7?
print('Is it true that 3 + 2 < 5 -7?')

#打印 What is 3+2? ,给出3+2的和
print('What is 3 + 2?', 3 + 2)
#打印 What is 5-7,给出5-7的差
print ('what is 5 - 7?', 5 - 7)

#打印 How about some more.
print('How about some more.')

#打印 Is it greater? 判断 5>=-2是否真实，如果是真，则返回True;如果是假，则返回False.
print('Is it greater?', 5>= -2)
#打印  Is it greater or equal?判断 5>=-2是否真实，如果是真，则返回True;如果是假，则返回False.
print('Is it greater or equal?', 5>=-2)
#打印 Is it less or equal? 判断 5<=-2是否真实，如果是真，则返回True;如果是假，则返回False.
print('Is it less or equal?', 5<=-2)


#加分题
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
#>使用 # 在代码每一行的前一行为自己写一个注解，说明一下这一行的作用。
#>记得开始时的 <练习 0> 吧？用里边的方法把 Python 运行起来，然后使用刚才学到的运算符号，把Python当做计算器玩玩。
#>自己找个想要计算的东西，写一个 .py 文件把它计算出来。
#>有没有发现计算结果是”错”的呢？计算结果只有整数，没有小数部分。研究一下这是为什么，搜索一下“浮点数(floating point number)”是什么东西。
#>使用浮点数重写一遍 ex3.py，让它的计算结果更准确(提示: 20.0 是一个浮点数)。
#计算器
print('The area of my house',80.84+25.01)
print('The price of my house',(122.89+37.55473)*(0.3199+0.03)+0.03)
print(1584+280+450+700+400+150+30+40+110+900+4644)

#带浮点数
print('I will now count my chickens:')

print('Hens',25.0 + 30.0/6.0)
print('Roosters',100.0 - 25.0 * 3.0 %4.0)

print('Now I will count the eggs:')

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0% 2.0 - 1.0/ 4.0 +6.0 )

print('Is it true that  3.0 + 2.0 < 5.0 - 7.0?')

print( 3.0 + 2.0 < 5.0- 7.0)

print('what is 3.0+2.0?', 3.0 +2.0)
print('What is 5.0-7.0?', 5.0 -7.0)

print('Oh, that\'s why it\'s False.')

print('How about some more.')

print('Is it greater?', 5.0 > 2.0)
print('Is it greater or equal?', 5.0 >=-2.0)
print('Is it less or equal?', 5.0<= -2.0)


