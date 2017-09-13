#--coding: utf-8 --
#Date:20170911
#Title:ex36_01 设计游戏 魔法世界

from sys import exit,argv

script,name=argv

def secret_room():
	print("Now, %s are in Secret Room."%name)
	print("%s can see a box. Do you want to open it? Yes or No?"%name)
	box = input("> ")
	if box == "yes":
		print("Oh, %s can get a key." %name)
	else:
		print("%s get nothing." %name)
	
	print("There are a door and a window in front of you.")
	print("How do %s want go out? door or window?" %name)
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
	if open_palace== "yes":
		print("Ok, you can open the door.")
	else:
		dead("Sorry, you cann't go into the door.")
		secret_room()
	
	print("Oh, there many things in the palace. Threre are: ")
	palace_things=["king seat", "imperial crown", "wands", "the book on the art of war", "weapons","beautiful cloths", "jewellery"]
	for n in palace_things:
		print(n)
	
	print("\nHowever, a lion is in front of you.")
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
	way_if=True
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
	print("""There is a gost.
    It will ask you four questions.
    If you don't answer right.You will game over
    """)
	questions=['50*50=','18*12=','1+5+6+7=','25*25=']
	print("Which questions you want to answer.")
	answer=input(">Question:")
	
	if answer=='1':
		print(questions[0])
		answer_1=input(">Answer:")
		if answer_1=='2500':
			print("Congratulions! You are right!")
			gold_room()
		else:
			dead("Sorry, you are wrong.")
	elif answer=='2':
		print(questions[1])
		answer_2=input(">Answer:")
		if answer_2=='216':
			print("Congratulions! You are right!")
			gold_room()
		else:
			dead("Sorry, you are wrong.")
	elif answer=='3':
		print(questions[2])
		answer_3==input(">Answer:")
		if answer_3=='19':
			print("Congratulions! You are right!")
			gold_room()
		else:
			dead("Sorry, you are wrong.")
	elif answer=='4':
		print(questions[3])
		answer_4==input(">Answer:")
		if answer_4=='625':
			print("Congratulions! You are right!")
			gold_room()
		else:
			dead("Sorry, you are wrong.")
	else:
		print("you must select from 1 to 4.")
	
	
def brave_way():
	print("There is an eagle waiting for you.But it is locked.")
	print("Oh, there is a gold egg around the eagle. What do you want? unlock the eagle or get the gold egg?")
	want=input("unlock or egg?> ")
	eagle=True
	while eagle:
		if want=="unlock":
			print("Oh, the eagle fly away. You get the gold egg.")
			gold_room()
		elif want =="egg":
			dead("The eagle is angry and kill you.")
		else:
			print("Please write the right word.")

def beautiful_way():
	print("""How beautiful the forests!
But a snake is here.
It is hungry.
What do you want? flee or stay?""")
	snake=input("flee or stay?> " )
	if snake=="flee":
		palace()
	elif snake=="stay":
		dead("The snake enjoy a delicious food.")
	else:
		dead("You are too slowly.")
	

def gold_room():
	print("This room is full of gold. How much do you take?")
	
	next = input("> ")
	if next.isdigit():
		how_much = int(next)
	
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You greedy bastard!")
	
def dead(over):
	print(over,"Game over. %s" %name)
	exit(0)
	


secret_room()
