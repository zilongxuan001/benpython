#--coding:utf-8--
#Date:20170811
#Title:ex04 变量(variable)和命名

#汽车的数量是100辆。
cars = 100

#车的座位数是4个。
space_in_a_car =4.0

#司机数量是30名。
drivers=30

#乘客数量是90名。
passengers=90

#不能开的车的数量是汽车的数量减去司机的数量
cars_not_driven=cars - drivers

#能开的车的数量是司机的数量
cars_driven=drivers

#汽车的承载能力是能开的车的数量乘以车的座位数。
carpool_capacity = cars_driven * space_in_a_car

#每辆车的平均乘客数量是乘客数量除以能开的车数量。
average_passengers_per_car = passengers / cars_driven


#打印'有多少车可以用。'
print('There are', cars, 'cars available.')

#打印‘只有多少个司机可以用。’
print('There are only', drivers, 'drivers available.')

#打印‘今天有多少辆空车。’
print('There will be', cars_not_driven,'empty cars today.')

#打印‘我们今天可以承载多少个人。’
print('We can transport', carpool_capacity,'people today.')

#打印‘我们今天有多少个乘客需要承载。’
print('We have', passengers,'to carpool today.')

#打印‘我们需要在每个车里放多少个乘客。’
print('We need to put about', average_passengers_per_car,'in each car.')

#加分题
#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/
#>我在程序里用了 4.0 作为 space_in_a_car 的值，这样做有必要吗？如果只用 4 会有什么问题?
#>记住 4.0 是一个“浮点数”，自己研究一下这是什么意思。
#>在每一个变量赋值的上一行加上一行注解。
#>记住 = 的名字是等于(equal)，它的作用是为东西取名。
#>记住 _ 是下划线字符(underscore)。
#>将 python 作为计算器运行起来，就跟以前一样，不过这一次在计算过程中使用变量名来做计算，常见的变量名有 i, x, j 等等。

#NameError: name 'car_pool_capacity' is not defined
#解释：
#名称错误：名称'car_pool_capacity'没有被定义

area_northhouse=40.2
area_southhouse=50.1
area_westhouse=20.5
price_percenge=0.3199
price_zhuangshi=0.03

area=area_northhouse+area_southhouse+area_westhouse
price=(price_percenge+price_zhuangshi)*area

print('The northhouse have',area_northhouse,'square meter.')
print('The southhouse have',area_southhouse,'square meter.')
print('The westhouse have',area_westhouse,'square meter.')
print('The house have', area,'square meter.')
print('The value of the house is', price,'yuan.')



