#--coding: utf-8 --
#Date:20170911
#Title:ex36_01 设计游戏 魔法世界

from sys import exit

def secret_room():
	print("Now, you are in Secret Room.")
	print("You can see a box. Do you want to open it? Yes or No?")
	box = input("> ")
	if box == "Yes":
		print("Oh, you can get a key.")
	else:
		print("You get nothing")
	
	print("There are a door and a window in front of you.")
	print("How do you want go out? door or window?")
	go_out=input("> ")
	if go_out=="door":
		print("Oh, there is a magnificent palace.")
		palace()
	else:
		dead("There is a cliff.")

def palace():
	print("Welcome to the king palace.")
	print("Do you have the key which can open the palace? Yes or No.")
	open_palace=input("> ")
	if open_palace== "Yes":
		print("Ok, you can open the door.")
	else:
		dead("Sorry, you cann't go into the door.")
		secret_room()
	
	print("Oh, there many things in the palace.")
	palace_things=["king seat", "imperial crown", "wands", "the book on the art of war", "weapons","beautiful cloths", "jewellery"]
	for n in palace_things:
		print(n)
	
	print("However, a lion is in front of you.")
	print("""He ask a question for you:
who have four legs in the morning?
who have two legs in the afternoon?
who have three legs in the evening?
		""")
	
	question=input("> ")
	if question =="people" or "mankind" or "man":
		print("""You are right.
The lion is run away.
You can get a diamond and go to the next way.""")
		next_way()
	else:
		dead("Sorry, you will become a delicious food for lion.")

def next_way():
	print("There are three ways for you.")
	print("""The right way is the Wisdom Way.
The middle way is the Brave Way.
The left way is the Beautiful Way.
What do you want? wisdom, brave, or beautiful? 
			""")
	way = input("> ")
	way_if==True
	while way_if:
		if way=="wisdom":
			wisdom_way()
			break
		elif way=="brave":
			brave_way()
			break
		elif way =="beautiful":
			beautiful_way()
			break
		else:
			print("I don't now what your means.")


def wisdom_way():
	pass
			
def brave_way():
	pass

def beautiful_way():
	pass



def dead(over):
	print(over,"Game over.")
	exit(0)
	


secret_room()
