def test_generator():
	for i in range(10):
		yield i

#You use them by iterating over them, either with a for loop or by passing them to any function.
for each in test_generator():
	#print (each)
	pass

#why we need  to use Generator
#for free memory when you are accesing larger values
#they generate values on fly

#with use of generator's 

def test_fib_on_gen(n):
	a = b = 1
	for each in range(n):
		#values on fly no memory
		yield a
		a, b = b, a+b

for each in test_fib_on_gen(10):
	#print (each)
	pass

#without use of generator's

def test_with_out_gen_fib(n):
	a = b = 1
	result =[]
	for each in range(n):
		#adding in memory
		result.append(a)
		a, b = b, a+b
	return result

#print (test_with_out_gen_fib(10))


