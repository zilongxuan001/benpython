from sys import argv

script,filename=argv

test=open(filename)

print("Here is  your %r of files:%r."%(script,filename))
print(test.read())

print("Do you want to read  the %r of %r file again?"%(script,filename))
file_agin=input('>>')

test_again=open(filename)
print(test_again.read())
