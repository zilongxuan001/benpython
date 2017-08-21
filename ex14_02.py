
from sys import argv

script, user, time =argv

prompt='>'

L='leaflet'
H='house'

print('Welcome,  %s! The %s of the game.This year is %s.'%(user,script,time))
print('There is the west of %s. Do you want to know it?'%H)
House=input(prompt)
print('''
You are standing in an open field west of a white %s, with a boarded 
front door. 
There is a small mailbox here. 
'''%H)
print('\n')

print('Oh, there is a box. Do you want to open it?')
Box=input(prompt)
print('Opening the small mailbox reveals a %s.'%L)
print('\n')

print('Do you want to take the %s?'%L)
Leafleat=input(prompt)
print('Taken. ')
print('\n')

print('Do you want to go north?')
north=input(prompt)
print('''North of House.
You are facing the north side of a white %s.
There is no door here,and all the windows are boarded up. 
To the north a narrow path winds 
through the trees. '''%H)
print('\n')

print('The end. Goodbye.')


#West of House

#open the box

#take leaflet

#go north

