
from sys import argv

script, from_file, to_file=argv

indata=open(from_file).read 

output=open(to_file,'w')

output.write(indata())

output.close


print(open(from_file).read())
print(open(to_file).read())

#print(open(to_file).read()),无法在运行中显示出来。但是print(open(from_file).read())可以在运行中显示出来。



