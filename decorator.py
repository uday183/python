
#function inside function
def f():
    def g():
        print ("this is inside function 'g' ")
    print ("this is out side function 'f' ")
    g()

f()

#function as a parameter
def g():
    print ("function 'g'")
def f(func):
    print ("function 'f'")
    func()
f(g)

def deco(f):
    def inner_deco(v1,v2):
        print ('inner deco:',v1-v2)
    return inner_deco

@deco
def test_deco(v1,v2):
    print ('test_deco:',v1+v2)


test_deco(2,3)


#function as no parameter
def deco(f):
	def inner_deco():
		print ('decorator is calling...')
	return inner_deco


@deco
def test_deco():
	print ('test_deco is calling...')

test_deco()
#output: decorator is calling...


#realtime examples


def deco(fun):
	def inner_deco(list_values):
		return [fun(v) for v in list_values]
	return inner_deco

@deco
def strings(value):
	return ''.join([word.capitalize() for word in value.split('_')])

print (strings(['uday_kumar_punna']))






















