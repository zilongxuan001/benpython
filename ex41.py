from sys import exit
from random import randint

def death():
	quips = ["You died. You kinda suck at this.",
	           "Nice job, you died ...jackass.",
			   "Such a luser.",
			   "I have a small puppy that's better at this."]
	
	print(quips[randint(0, len(quips)-1)])
	exit(1)
	
	
def central_corridor():
	print("The Gothons of Plant Percal #25 have invaded your ship and destroyed")
	print("your entire crew. You are the last surviving member and your last")
	print("mission is to get the neutron destruct bomb from the Weapons Armory,")
	print("put it in the brigde, and blow the ship up after getting into an")
	print("escape pod.")
	print("\n")
	print("You're running down the central corridor to the Weapons Armory when")
	print("a Gothon jumps out, red scaly skin, dark grimy teeth, and eveil clown costume")
	print("flowing around his hate filled body. He's blocking the door to the")
	print("Armory and about to pull a weapon to blast you.")
	
	action = input("> ")
	
	if action == "shoot!":
		print("Quick on draw you yank out your blaster and fire it at the Gothon.")
		print("His colwn costume is flowing and moving around his body, which throws")
		print("off your aim. Your laser hits his costume but misses him entirely. This")
		print("completely ruins his brand new costume his mother bought him, which")
		print("makes him fly into an insane rage and blast you repeatedly in the face untill")
		print("you are dead. Then he eats you.")
		return 'death'

	elif action == "dodge!":
		print("Link a  world class boxer you dodge, weave, slip and slide right")
		print("as the Gothon's blaster cranks a laser past your head.")
		print("In the middle of your artful dodge your foot slips and  you")
		print("bang your head on the metal wall and pass out.")
		print("You wake up shortly after only to die as the Gothon stomps on")
		print("your head and eats you.")
		return 'death'
	
	elif action == "tell a joke":
		print("Lucky for you they made you learn Gothon insults in the academy.")
		print("You tell the one Gothon joke you know:")
		print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.")
		print("The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
		print("While he's laughing you run up and shoot him square in the head")
		print("putting him down, then jumb through the Weapon Armory door.")
		return 'laser_weapon_armory'
	
	else:
		print("DOES NOT COMPUTE!")
		return 'central_corridor'
		
def laser_weapon_armory():
	print("You do a dive roll into the Weapon Armory, crouch and scan the room")
	print("for more Gothons that might be hiding. It's dead quiet, too quiet.")
	print("You stand up and run to the far side of the room and find the")
	print("neutron bomb in its container. There's a keypad lock on the box")
	print("and you need the code to get the bomb out. If you get the code")
	print("wrong 10 times then the lock closes forever and you can't")
	print("get the bomb. The code is 3 digits.")
	code = "%d%d%d" %(randint(1,9),randint(1,9),randint(1,9))
	guess = 0 
	
	while guess != code and guess <10:
		print("BZZZZEDDD!")
		guess +=1
		guess = int(input("[keypad]> "))
	
	if guess == code:
		print("The container clicks open and the seal breaks, letting gas out.")
		print("You grab the neutron bomb and run as fast as you can to the")
		print("bridge where you must place it in the right spot.")
		return 'death'
		
def the_bridge():
	print("You burst onto the Bridge with the neutron destruckt bomb")
	print("under your arm  and surpries 5 Gothons who are trying to")
	print("take control of the ship. Each of them has an evevn uglier")
	print("clown costume than the last. They haven't pulled their")
	print("weapons out yet, as they see the active bomb under your")
	print("arm and don't want to set it off.")
	
	action = input("> ")
	
	if action == 'throw the bomb':
		print("In a panic you throw the bomb at the group of Gothons")
		print("and make a leap for the door. Right as you drop it a")
		print("Gothon shoots you right in the back killing you.")
		print("As you die you see another Gothon frantically try to disarm")
		print("the bomb. You die knowing they will probably blow up when")
		print("it gose off")
		return 'death'
	
	elif action == "slowly place the bomb":
		print("You point your blaster at the bomb under your arm")
		print("and the Gothons put their hands up and start to sweat.")
		print("You inch backward to the door, open it, and then carefully")
		print("place the bomb on the floor, pointing your blaster at it.")
		print("You then jumb back through the door, punch the close butoon")
		print("and blast the lock so the Gothons can't get out.")
		print("Now that the bomb is placed you run to the escape pod to")
		print("get off this tin can.")
		return 'escape_pod'
	else:
		print("DOES NOT COMPUTE!")
		return 'the_bridge'

def escape_pod(): 
	print("You rush through the ship desperately trying to make it to")
	print("the escape pod before the whole ship explodes. It seems like")
	print("hardly and Gothons are on the ship, so your run is clear of")
	print("interference. You get to the chamber with the escape pods, and")
	print("now need to pick one to take. Some of them could be damaged")
	print("but you don't have time to look. There's 5 pods, which one")
	print("do you take?")
	
	good_nod = randint(1,5)
	guess = input("[pod #]> ")
	
	if int(guess) != good_nod:
		print("You jumb into pod %s and hit the eject button." %guess)
		print("The pod escapes out into the void of space, then")
		print("implodes as the hull ruptures, crushing your body")
		print("into jam jelly.")
		return 'death'
	else:
		print("You jumb into pod %s and hit the eject button." %guess)
		print("The pod easily slide out into space heading to")
		print("the planet below. As it files to the planet, you look")
		print("back and see your ship implode then explode like a")
		print("bright star, taking out the Gothons ship at the same")
		print("time. You won!")
		exit(0)
		
ROOMS = {
		'death':death,
		'central_corridor':central_corridor,
		'laser_weapon_armory':laser_weapon_armory,
		'the_bridge':the_bridge,
		'escape_pod':escape_pod
}

def runner(map, start):
	next = start
	
	while True:
		room = map[next]
		print("\n----------")
		next = room()

runner(ROOMS, 'central_corridor')
		


#引用网址：http://old.sebug.net/paper/books/LearnPythonTheHardWay/	


# 加分习题
# 解释一下返回至下一个房间的工作原理。
# 创建更多的房间，让游戏规模变大。
# 除了让每个函数打印自己以外，再学习一下“文档字符串(doc strings)”式的注解。看看你能不能将房间描述写成文档注解，然后修改运行它的代码，让它把文档注解打印出来。
# 一旦你用了文档注解作为房间描述，你还需要让这个函数打印出用户提示吗？试着让运行函数的代码打出用户提示来，然后将用户输入传递到各个函数。你的函数应该只是一些 if 语句组合，将结果打印出来，并且返回下一个房间。
# 这其实是一个小版本的“有限状态机(finite state machine)”，找资料阅读了解一下，虽然你可能看不懂，但还是找来看看吧。













#如何阅读难懂的语句
# （1）从前往后读
# （2）从后往前读
# （3）从中心开始，逆时针读。


# 你在上一节中发现 dict 的秘密功能了吗？你可以解释给自己吗？让我来给你解释一下，顺便和你自己的理解对比看有什么不同。这里是我们要讨论的代码：

# cities['_find'] = find_city
# city_found = cities['_find'](cities, state)
# 你要记住一个函数也可以作为一个变量，``def find_city`` 比如这一句创建了一个你可以在任何地方都能使用的变量。在这段代码里，我们首先把函数 find_city 放到叫做 cities 的字典中，并将其标记为 '_find'。 这和我们将州和市关联起来的代码做的事情一样，只不过我们在这里放了一个函数的名称。

# 好了，所以一旦我们知道 find_city 是在字典中 _find 的位置，这就意味着我们可以去调用它。第二行代码可以分解成如下步骤：

# Python 看到 city_found = 于是知道了需要创建一个变量。
# 然后它读到 cities ，然后知道了它是一个字典
# 然后看到了 ['_find'] ，于是 Python 就从索引找到了字典 cities 中对应的位置，并且获取了该位置的内容。
# ['_find'] 这个位置的内容是我们的函数 find_city ，所以 Python 就知道了这里表示一个函数，于是当它碰到 ( 就开始了函数调用。
# cities, state 这两个参数将被传递到函数 find_city 中，然后这个函数就被运行了。
# find_city 接着从 cities 中寻找 states ，并且返回它找到的内容，如果什么都没找到，就返回一个信息说它什么都没找到。
# Python find_city 接受返回的信息，最后将该信息赋值给一开始的 city_found 这个变量。
# 我再教你一个小技巧。如果你倒着阅读的话，代码可能会变得更容易理解。让我们来试一下，一样是那行：

# state 和 city 是...
# 作为参数传递给...
# 一个函数，位置在...
# '_find' 然后寻找，目的地为...
# cities 这个位置...
# 最后赋值给 city_found.
# 还有一种方法读它，这回是“由里向外”。

# 找到表达式的中心位置，此次为 ['_find'].
# 逆时针追溯，首先看到的是一个叫 cities 的字典，这样就知道了 cities 中的 _find 元素。
# 上一步得到一个函数。继续逆时针寻找，看到的是参数。
# 参数传递给函数后，函数会返回一个值。然后再逆时针寻找。
# 最后，我们到了 city_found = 的赋值位置，并且得到了最终结果。
# 数十年的编程下来，我在读代码的过程中已经用不到上面的三种方法了。我只要瞟一眼就能知道它的意思。甚至给我一整页的代码，我也可以一眼瞄出里边的 bug 和错误。这样的技能是花了超乎常人的时间和精力才锻炼得来的。在磨练的过程中，我学会了下面三种读代码的方法，它们是用户几乎所有的编程语言：

# 从前向后。
# 从后向前。
# 逆时针方向。
# 下次碰到难懂的语句时，你可以试试这三种方法。