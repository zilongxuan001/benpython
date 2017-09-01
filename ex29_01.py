people=int(input('Peopele:'))
cats=int(input('Cats:'))
dogs=int(input('Dogs:'))


if people < cats and people==25:
	print("Too many cats! The world is doomed!")

if people> cats and cats==40:
	print("Not many cats! The world is saved!")

if people < dogs and dogs==20:
	print("The world is drooled on!")

if people > dogs and cats==40:
	print("The world is dry!")

dogs +=5

if people >=dogs:
	print("People are greater than or equal to dogs.")

if people <=dogs:
	print("People are less than or equal to dogs.")

if people ==  dogs:
	print("People are dogs.")