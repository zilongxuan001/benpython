
filename=input('>')

txt=open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

text=open(filename,'w')
text.write('good night!')
text.close()

txt=open(filename)
print("Here's your changed file %r:" % filename)
print(txt.read())


