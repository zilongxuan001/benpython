#--coding: utf-8 --
#Date:20170908
#Title:ex35 分支和函数

from sys import exit

#定义金房子，如果输入0或1则计算长度，否则执行dead函数。
def gold_room():
	print("This room is full of gold. How much do you take?")
	
	next = input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	
	else:
		dead("Man, learn to type a number.")
#如果函数小于50，则打印：不错，你不贪，你赢了。否则执行dead函数	
	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You greedy bastard!")

#定义熊屋，打印：这是熊屋。熊有很多蜂蜜。胖熊在另一个门前。你怎么把熊赶走？
def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False
#如果输入take honeny,则执行dead函数。
#如果输入taunt bear,且熊没动，打印：熊从这个门前移开，你可以穿过。
#如果再次输入taunt bear,且熊动了，则执行deadh函数。	
#如果再次输入open door,且熊动了，则执行gold_room()函数。
#否则，打印：我没搞清楚意思。
	while True:
		next = input("> ")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next =="taunt bear" and not bear_moved:
			print("The bear has moved from the door. You can go through it now.")
			bear_moved= True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")

#定义邪神屋，打印：现在你看见了邪神克鲁苏。只要他或它看你一眼，你就会发疯。你是保命离开还是让他吃了你？			
def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")
	
	next= input("> ")
#如果输入离开，则执行start函数。
#如果输入head, 则执行dead函数。
#否认，执行cthulhu_room函数。
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

#定义dead函数，打印why参数和Good job。
def dead(why):
	print(why, "Good job!")
	exit(0)

#定义start函数。打印：这是一个黑屋子。在你的左边或右边，各有一个门。你选哪个？
def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")
	
	next = input("> ")
	
#如果输入left,则执行bear_room函数。
#如果输入右边，则执行cthulhu_room函数。
#否则，执行dead函数。
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

#开始吧，执行start函数。
start()




#感悟熊屋设置的巧妙之处：
#设置bear_room()函数时，必须输入一次taunt bear，才能输入一次open door，打开金屋。
#因为第一次输入taunt bear，bear_moved被赋值为True.
# 第二次输入tanut bear时，会执行第二个eilf。

#sys.exit(n)
#如果是exit(0),则是正常退出，如果是其他数字，则是非正常退出。


#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/	
# 加分习题
# 1.把这个游戏的地图画出来，把自己的路线也画出来。
# 2.改正你所有的错误，包括拼写错误。
# 3.为你不懂的函数写注解。记得文档注解该怎么写吗？
# 4.为游戏添加更多元素。通过怎样的方式可以简化并且扩展游戏的功能呢？
# 5.这个 gold_room 游戏使用了奇怪的方式让你键入一个数字。这种方式会导致什么样的 bug？ 你可以用比检查 0、1 更好的方式判断输入是否是数字吗？int() 这个函数可以给你一些头绪。
	
# 4.先画路线图，再定义函数，可以简化并扩展游戏的功能。
# 5. 如果是十六进制带ABCDEF，如1F，虽然带有1，但是不是十进制，就会出现错误。如果写出二级制，也会默认为十进制。
#    可以用 next.isdigit()，判断是否全部为数字。