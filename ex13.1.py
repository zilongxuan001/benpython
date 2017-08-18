from sys import argv

scirpt, first,second=argv


print('The script is:',scirpt)
print('The first people name: ',first)
age=input('How old are you,%r? '%first)
color=input("What is your skin's color,%r? "%first)
print("So, the first people name: %r, age: %r, color: %r." %(first, age,color))


print('The second variable is: ',second)
age2=input('How old are you, %r?'%second)
color2=input("What is your skin's color, %r?"%second)
print("So, the second people name: %r, age: %r, color: %r." %(second, age2,color2))


