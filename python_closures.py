#if we want to access variables inside scope its easy
#but if a variable is out side scope it will not access inside scope
#for this we can use closures

def outer_function():
	x= 'uday'
	def inner_function():
		name =x
		print (name)
	return inner_function
print (outer_function())


#A closure unlike a plain function allows the function to access those captured variables through 
#the closures copies of their values or references
#even when the function is invoked outside their scope

def outer_function():
	x= 'uday'
	def inner_function():
		print (x)
	return inner_function

obj = outer_function()
print (obj())


#if use global it will not work
def outer_function():
	x= 'uday'
	def inner_function():
		global x
		print (x)
	return inner_function

obj = outer_function()
print (obj())


#if use x out side function it will work
x= 'uday'
def outer_function():
	def inner_function():
		global x
		print (x)
	return inner_function

obj = outer_function()
print (obj())