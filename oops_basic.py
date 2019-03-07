#class of python

class Test:
	def __init__(self,name):
		self.name = name

#obj = Test('uday')
#print (obj.name)

#########################################

class Test:
	def __init__(self,name):
		self.name = name
	def set_name(self,name):
		self.name = name
		return ('name changed')
	def get_name(self):
		return self.name
#obj = Test('uday')
#print(obj.name)
#print (obj.set_name('kumar'))
#print (obj.get_name())

######################################
class Person:
	def __init__(self,name):
		self.name = name
	def is_joined(self):
		return False

class College(Person):
	# calling the super-class function __init__  
    # using the super() function 
	def __init__(self,name):
		super().__init__(name)

	def is_joined(self):
		return True

#p_obj = Person('kumar')

#print (p_obj.is_joined())
#print(p_obj.name)

#c_obj = College('uday')

#print(c_obj.is_joined())
#print (c_obj.name)

##########################################
#if not find function in child it will look in parent classes

class Test:
	def __init__(self,name):
		self.name = name

	def is_check(self):
		print ("Test class calling ........")

class Test1(Test):
	def __init__(self,name):
		self.name = name
	def is_check(self):
		print ("Test1 class calling.........")

class Test2(Test1):
	def __init__(self,name):
		self.name = name


#obj = Test2('uday')
#print (obj.is_check())


###############################################
#calling parent class method in child class

class Test:
	def __init__(self,name):
		self.name = name

	def is_check(self):
		print ("Test class calling ........")

class Test1(Test):
	def __init__(self,name):
		self.name = name
	def is_check(self):
		print ("Test1 class calling.........")

class Test2(Test1):
	def __init__(self,name):
		self.name = name
	def is_check(self):
		#it calls Test1 function
		super().is_check()

#obj = Test2('uday')
#print (obj.is_check()) 

##########################################################
#the way mro works

class A:
	def __init__(self):
		self.name = 'uday'

class B(A):
	def __init__(self):
		self.name = 'uday'

class C(B):
	def __init__(self):
		self.name = 'uday'

#print (C.mro())
#left to right
#[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

#dimond problem
class A:
	def __init__(self):
		self.name = 'uday'

class B(A):
	def __init__(self):
		self.name = 'uday'

class C(A):
	def __init__(self):
		self.name = 'uday'

class D(B,C):
	def __init__(self):
		self.name = 'uday'

#print (D.mro())
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#imp
#if two child having same grand parent languages it will add the end
# the rule is Left -to - Right - to - Grand Parent

############################################################
#encapsulation

class Hide:
	__amount = 100
	def __init__(self):
		self.name = 'uday'

obj = Hide()
#print (obj.name)
#print (obj.__amount) #it will raise attribute error
#print (obj._Hide__amount)#it will give amount so nothing is private in python 


###############################################################
#methods of classes

#instance method

class A:
	def __init__(self):
		self.name = 'uday'
obj =A()
print(obj.name)

#class method

class B:
	@classmethod
	def myfunc(cls):
		print ("this is class method")

print (B.myfunc())


#staticmethod

class C:
	@staticmethod
	def myFunction():
		print ("this is staticmethod")
print (C.myFunction())

###############################################












































































































































































