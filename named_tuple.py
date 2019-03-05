def func():
	name = 'uday'
	place = 'bangalore'
	return name,place

print (func())
#insted of returning in tuple we have namedtuple
#if a function return more than one variable better to use namedtuple to get easy access

from collections import namedtuple
def funcs():
	nam = namedtuple('nam','name place')
	return nam(name='uday',place ='bangalore')

obj = funcs()
print (obj.name)
print (obj.place)
