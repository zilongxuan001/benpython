from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
#file_again = raw_input("> ")

txt_again = open(file_again)

print(txt_again.read())

#去掉第11行，运行ex15.py,会出现NameError:name 'file_again' is not defined.
