def ti_xing(a,b,c):
	s=(a+b)/(2*c)
	print("The area of ti_xing is:(%d + %d)/(2*%d)" %(a,b,c))
	return s

def cycle(r,pi=3.1415926):
	s=pi*r*r
	print("The area of cycle is:%.7f *%d *%d" %(pi,r,r))
	return s 

def square(a):
	s=a*a
	print("The area of square is:%d*%d"%(a,a))
	return s

print("Let's to math these area:")

t=ti_xing(6,8,3)
c=cycle(5)
s=square(4)
print("t:%d,c:%f, s:%d"%(t,c,s))

print("There a puzzle,too")
o=square(cycle(ti_xing(t,c,s)))

print("there are a puzzle: %d"%o)
