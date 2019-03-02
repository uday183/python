def test_arg(fun_arg, *arg):
	fun_arg = fun_arg
	print ('definf arg:',fun_arg)
	for args in arg:
		print ('*args are :', args)

#test_arg('uday','bangalore','hoodi')

def test_key_args(**kwargs):
	for key,value in kwargs.items():
		print (key, value)

#test_key_args(name='uday',age=28,location='bangalore')

def test_args_kwargs(arg1,arg2,arg3):
	print (arg1,arg2,arg3)

#test_args_kwargs('uday',1,2)
kwargs = {"arg1": "uday", "arg2":28,'arg3':'bangalore'}
# kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)

