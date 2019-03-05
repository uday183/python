
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
def make_deco(f):
    def iner_func():
        print('calling deco')
        f()
    return iner_func
@make_deco
def ordi():
   print ('calling ordinary')
