print("You enter a dark room with three doors.  Do you go through door #1 or door #2 or door #3")
n=0
while n <5:

	n=n+1
	
	door = input("> ")

	if door == '1':
		print("There's a giant bear here eating a cheese cake. What do you do ?")
		print("1. Take the cake.")
		print("2. Scream at the bear.")
		
		bear = input("> ")
		
		if bear == "1":
			print("The bear eats your face off. Good job!")
		elif bear =="2":
			print("The bear eats your legs off. Good job!")
		else:
			print("Well, doing %s  is property better. Bear runs away." %bear)
			
	elif door == '2':
		print("You stare into the endless asbyss at Cthulhu's retina.")
		print("1. Blueberries.")
		print("2. Yellow jacket clothespins.")
		print("3. Understanding revolevers yelling melodies.")
		
		insanity = input("> ")
		
		if insanity =="1" or insanity == "2":
			print("Your body survives powered by a mind of jello. Good job!")
		else:
			print("The insanity rots your eyes into a pool of muck. Good job!")

	elif door =='3':
		print("You stand on a green land .there are a beautiful girl.What do you do?")
		print("1. talk with her.")
		print("2. fuck her.")
		print("3. don't look at her.")
		
		girl= input("> ")
		
		if girl =='1':
			print("She will be glad , and be your friend.")
		elif girl == '2':
			print("She will become a tiger, and eat you.")
		elif girl =='3':
			print("She will be very sad.")
		else :
			print("She don't know what to do.")

	else:
		print("You stumble around and fall on a knife and die. Good job!")