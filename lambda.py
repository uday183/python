#lambda --> map, filter, reduce

#sample lambda

f = lambda x: x*x
print (f(1))

l=[]
for each in range(10):
	l.append(each*2)
print (l)

#to reduce above code we can use map function in one line

print (list(map(lambda x: x*2, [1,2,3,4,5,6,7,8,9])))

def multiply(x):
	return (x*x)
def add(x):
	return (x+x)
func = [add,multiply]

for each in range(5):
	value = list(map(lambda x: x(each) , func))
	print (value)


#filter function
range_list = range(-5, 5)
print (list(filter(lambda x: x<0, range_list)))


#reduce function from functool
#if you wanted to compute the product of a list of integers.
#it for performing some computation on a list and returning the result

product = 1 
lis = [1,2,3,4]
for each in lis:
	product = product * each
print (product)

#above one we can write with reduce 
from functools import reduce
product = reduce((lambda x, y : x*y),[1,2,3,4])
print (product)

