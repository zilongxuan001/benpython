from sys import exit

#定义金房子，如果输入0或1则计算长度，否则执行dead函数。
def gold_room():
	print("This room is full of gold. How much do you take?")
	
	next = input("> ")
	if next.isdigit():
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

def girl_room():
	print("Here is a beautiful girl standing another door.")
	print("She is looking at you.")
	print("What do you want? Fuck or talk?")
	girl_smile = False
	
	while True:
		next = input("> ")
		
		if next=="fuck":
			dead("The girl becomes a tiger and eat you.")
		elif next == "talk" and not girl_smile:
			print("The girl smiles and be your friend.You can throug the door. Do you want to talk or open door?")
			girl_smile= True
		elif next == "talk" and girl_smile:
			bear_room()
		elif next == "open door" and girl_smile:
			gold_room()
		else:
			cthulhu_room()
		

#定义dead函数，打印why参数和Good job。
def dead(why):
	print(why, "Good job!")
	exit(0)

#定义start函数。打印：这是一个黑屋子。在你的左边或右边，各有一个门。你选哪个？
def start():
	print("You are in a dark room.")
	print("There is a door to your right, middle and left.")
	print("Which one do you take?")
	
	next = input("> ")
	
#如果输入left,则执行bear_room函数。
#如果输入右边，则执行cthulhu_room函数。
#否则，执行dead函数。
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	elif next == "middle":
	    girl_room()
	else:
		dead("You stumble around the room until you starve.")

#开始吧，执行start函数。
start()


#错误反思
#girl_room()里的 第二个elif next == "talk " and girl_smile: 中的talk,我多个一个空格
#应为 elif next == "talk" and girl_smile: