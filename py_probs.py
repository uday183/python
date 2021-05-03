#thread:
#In computing, a process is an instance of a computer program that is being executed. Any process has 3 basic components:
#An executable program.
#The associated data needed by the program (variables, work space, buffers, etc.)
#The execution context of the program (State of process)


#A thread is an entity within a process that can be scheduled for execution. 
#Also, it is the smallest unit of processing that can be performed in an OS (Operating System).

#In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code.

#Multiple threads can exist within one process .Multithreading is defined as the ability of a processor to execute multiple threads concurrently.

import threading
import os


def task1():
    print("Task 1 assigned to thread: {}".format(threading.currentThread().name))
    print("Id: {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to thread: {}".format(threading.currentThread().name))
    print("Id: {}".format(os.getpid()))

t1 = threading.Thread(target=task1,name='t1')
t2 = threading.Thread(target=task2,name='t2')

# t1.start()
# t2.start()

# t1.join()
# t2.join()

def square(n):
    print('Square',n*n)

def qube(n):
    print('Qube',n*n*n)

t1 = threading.Thread(target=square,args=(10,))
t2 = threading.Thread(target=qube,args=(10,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


#race condition
x = 0 
lock = threading.Lock()

def thread_task():
    global x
    lock.acquire()
    for _ in range(10000):
        x+=1
    lock.release()

def main_task():
    global x
    x = 0
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)
    
#    t1.start()
#    t2.start()

#   t1.join()
#   t2.join()

#for i in range(10):
#    main_task()
#    print("Iteration {0}: x = {1}".format(i,x))



##########################################################################
test_list = [(6, 9, 17, 18), (15, 34, 56), (6, 7), (6, 9), (15, 34)] 
k = 2

temp = {}
for each in test_list:
    t = each[:k]
    temp.setdefault(t,[]).append(each)
#print(temp)
result = [i for i in test_list if len(i)>k or len(temp[i])==1]
# print(result)

##########################################################################

#Total equal pairs in List
lis = [2, 4, 5, 2, 5, 4, 2, 4, 5, 7, 7, 8, 3]
uniq = set(lis)
count = 0

for i in uniq:
    count+=lis.count(i)//2
#print(count)

##########################################################################
#Python program to randomly create N Lists of K size

test_list = [6, 9, 1, 8, 4, 7]
K = 3
N =  4

from random import shuffle

def random_list(test_list,K):
    shuffle(test_list)
    while True:
        yield  test_list[:K]

new = []
for each in range(0, N):
    new.append(next(random_list(test_list,K)))

#print(new)

##########################################################################

#Print all words occurring in a sentence exactly K times
s = "banana is in yellow and sun flower is also in yellow"
k = 2

def word_occurring(s,k):
    l_s = s.split(' ')
    for i in l_s:
        if l_s.count(i) == k:
            print(i)
            l_s.remove(i)
    return ''

#print(word_occurring(s,k))
##########################################################################
#Python program to convert a list into a list of lists using a step value

lis = [5, 6, 3, 2, 7, 1, 9, 10, 8]
k = 3

def slice(lis,k):
    new = []
    for i in range(0,k):
        new.append(lis[i::k])
    return new

#print(slice(lis,k))
#print([lis[i::k] for i in range(0,k)])
##########################################################################
#sort 1010101
def list_sort():
    lis = [1,0,1,0,1,0,1,1,0]
    first = 0
    last = len(lis)-1
    while first < last:
        if lis[first] > 0:
            lis[first],lis[last] = lis[last],lis[first]
            last-=1
        else:
            first+=1
    return lis
#print(list_sort())
#another way

lis = [1,0,1,0,1,0,1,1,0]
count=0
for each in range(len(lis)):
    if lis[each]!=1:
        lis[count] = lis[each]
        count+=1
while count < len(lis):
    lis[count] = 1
    count+=1
#print(lis)
##########################################################################
#find index position of a list
lst = [1, 2, 1, 3, 4, 5, 4, 5]

d = {}

for each in range(len(lst)):
    if lst[each] in d.keys() :
        d[lst[each]].append(each)
    else:
        d[lst[each]] = [each]
#print(d)

#second method
d={} 
count=0
for each in lst:
    if each in d.keys():
        d[each].append(count)
    else:
        d[each] = [count]
    count+=1
#print(d)

#third type
d={}
for idx,each in enumerate(lst):
    if each in d.keys():
        d[each].append(idx)
    else:
        d[each] = [idx]
#print(d)
##########################################################################
#classmethods and staticmethod best example

class Date:
    def __init__(self,day=0,month=0,year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def chk_date(cls,date_string):
        day,month,year = map(int,date_string.split('-'))
        date1 = cls(day,month,year)
        return date1

    @staticmethod
    def valid_date(date_string):
        day,month,year = map(int,date_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date2 = Date()
is_date = Date.valid_date('11-09-2012')
#print(date2.chk_date('11-09-2012'))
#print(is_date)

##########################################################################
#bubble sort
arr = [3,6,9,5,2]

n= len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] =  arr[j+1],arr[j]
#print(arr)

#second index position sorting
data = [['akash', 5], ['rishav', 3], ['gaurav', 15], ['ram', 6]]

n= len(data)
for i in range(n):
    for j in range(n-i-1):
        if data[j][1] > data[j+1][1]:
            data[j],data[j+1] = data[j+1],data[j]
#print(data)

#another way

arr = [3,6,9,5,2]
n = 5

for i in range(n):
    min = i
    for j in range(i+1,n):
        if arr[min] > arr[j]:
            min = j
    arr[i],arr[min] = arr[min],arr[i]
#print(arr,'***')

##########################################################################
#Decorator

def is_even_chk(fun):
    def wrap(*args,**kwargs):
        if args[0]%2==0:
            return fun(*args,**kwargs)
        else:
            return ('Its Odd Number')
    return wrap

@is_even_chk
def number(value):
    print('Its Even number go Head')
    return

#print(number(4))
##########################################################################
#recurence
lst = [1,2,3,4,5]

def recur(lst):
    if not lst:
        return 0
    else:
        return lst[0]+recur(lst[1:])
#print(recur(lst))

lst = [1, [2, [3, 4], 5], 6, [7, 8]]

def recurs(lst):
    tot =0
    for each in lst:
        if not isinstance(each,list):
            tot+=each
        else:
            tot+=recurs(each)
    return tot

#print(recurs(lst))

##########################################################################
#merge sort

arr = [54,26,93,17,77,31,44,55,20]
def merge(arr):
    
    if len(arr) >1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge(left)
        merge(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    return arr
#print(merge(arr))
##########################################################################
#N-Largest numbers
N=3
def n_largest_number(N):
    lis = [1,22,4,33,66,88,100]
    result = []
    for i in range(N):
        maxx = 0
        for j in range(len(lis)):
            if lis[j] > maxx:
                maxx = lis[j]
        result.append(maxx)
        lis.remove(maxx)
    return result

#print(n_largest_number(N))
#find second highest number in a list

l = [2,4,5,8,7,9]

f1 = l[0]
f2 = None

l1 = l[0]
l2 = None

for i in l[1:]:
    if i > f1:
        f2 = f1
        f1 = i
    elif f2 == None or i > f2:
        f2 = i
    if i < l1:
        l2 = l1
        l1 = i
    elif l2 ==None or i < l2:
        l2 = i

#print(l1,l2)
#print(f1,f2)
##########################################################################
#Filter consecutive elements Tuples
ll = [(3, 4, 5, 6), (5, 6, 7, 2), (1, 2, 3), (6, 4, 6, 3)]

def check(ll):
    for each in range(len(ll)-1):
        if ll[each+1]!= ll[each]+1:
            return False
    return True

#print([i for i in ll if check(i)])

##########################################################################
#binary_search
def binary_search(data,elem):
    first = 0
    last  = len(data)-1
    while first <= last:
        mid = (first+last)//2
        if data[mid] == elem:
            return mid
        elif data[mid] > elem:
            last = mid -1
        else:
            first = mid+1
    return False

data = [1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71]
elem = 700

#print(binary_search(data, elem))

##########################################################################

ll = [('p', 'q'), ('p', 'r'), ('p', 's'), ('m', 't')]

#O/P: {'m': ['m', 't'], 'p': ['p', 'q', 'r', 's']}
d={}
for each in ll:
    try:
        d[each[0]].extend(each[1:])
    except:
        d[each[0]] = list(each)

#print(d)

##########################################################################
#missing number in a list
lis = [1,2,4,5,6]
n = len(lis)

formula = (n+1)*(n+2)/2
sums = sum(lis)
result = formula-sums
#print(result) 
##########################################################################
#is_prime number
num =3

def is_prime_number(num):
    if num > 1:
        for i in range(2, num//2):
            if num%i  == 0:
                print('its not a prime number')
                break
        else:
            print('its a prime number')
    else:
        print('its not a prime number')

#print(is_prime_number(num))
##########################################################################
#sum of int
b = 365
l=[]
while (b > 0):
    dig = b%10
    l.append(dig)
    b = b//10
#print(sum(l))
##########################################################################

##########################################################################
#remove duplicates

lis = [1,1,2,3,4,5,6,2,3]
#print([i for idx,i in enumerate(lis) if not i in lis[:idx] ])
##########################################################################

s='abbcdabcdbbaa'
def longest_uniq_string_count(s):
    result = []
    dummy = []
    for idx, value in enumerate(s):
        if value in result:
            index = result.index(value)
            result = result[index:]
        else:
            result.append(value)
        if len(result) > len(dummy):
            dummy = result
    return len(dummy)
#print(longest_uniq_string_count(s))

##########################################################################
#reverse a string
s = 'uday'
def reverse_string(s):
    new = ''
    last = len(s)-1
    while last > 0:
        new += s[last]
        last -=1
    new+=s[last]
    return new
#print(reverse_string())
n = ''
for i in s:
    n = i+n
#print(n)

sen = "GeeksforGeeks is good to learn" 
#print(' '.join(word[::-1] for word in sen.split(' ')))
#print("".join(sen[i] for i in range(len(sen)-1,-1,-1)) )
##########################################################################
main ='ababababcdbcdbdfdfdfd'
sub = 'aba'

def sub_string_count(main,sub):
    count = 0
    for i in range(len(main)):
        sub1 = main[i:i+len(sub)]
        if sub == sub1:
            count+=1
    return count
#print(sub_string_count(main,sub))

##########################################################################
#defination with examples

#polymorphism

#Duck typing about Polymorphism
#as long as classes contains same methods create comman interface for both class 
#it check calls at runtime
#Without polymorphism, a type check may be required before performing an action on an object to determine the
#correct method to call. The following counter example performs the same task as the previous code


#Python uses the C3 linearization algorithm to determine the order in which to resolve class attributes, including
#methods. This is known as the Method Resolution Order (MRO) 

#Python's MRO algorithm is
# 1. depth first (left to right)
# 2. No circular relationship allowed
# 3. a shared parent blocked by child


class Test:
    def get(self):
        return 'red'

class Best:
    def get(self):
        return 'white'

t =Test()
b = Best()
def common_interface(obj):
    return obj.get()
#print(common_interface(b))


##########################################################################
#adding two instance of class
class Test:
    def __init__(self,value):
        self.value = value
    def __add__(self,obj):
        return self.value+obj.value

a = Test(2)
b = Test(3)

#print(a+b)
##########################################################################
#Monkey Patching
#we can assign functions or method to a already established class like assing functions to a class while run time

class Test:
    def __init__(self):
        self.value = 30

def test(self):
    return self.value

t =Test()

Test.test = test

#print(t.test())
##########################################################################

#multiple inheritance

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C.__init__')

#c = C()
#print(c)

##########################################################################
#Calling a Method on a Parent Class

class A:
    def get(self):
        print('A is calling')

class B(A):
    def test(self):
        super(B,self).get()
        print('B is calling')

obj = B()
#print(obj.test())

##########################################################################
#Override class methods in Python
#Overriding is a very important part of OOP since it makes inheritance utilize its full power. 
#By using method overriding a class may "copy" another class, avoiding duplicated code, 
#and at the same time enhance or customize part of it. Method overriding is thus a part of the inheritance mechanism.

class Test:
    def __init__(self):
        self.value = 4
    def get_value(self):
        return self.value

class Pest(Test):
    def get_value(self):
        return self.value +1

obj = Pest()
#print (obj.get_value())

##########################################################################
#Single Inheritance
x=0
class Test:
    def __init__(self):
        global x
        x +=1
        #print ('class Test')

class West(Test):
    def __init__(self):
        super().__init__()
        global x
        x +=2
        #print ('class west')

#obj= West()
#print(obj())

##########################################################################
#Operator Overloading

#Operator Overloading means giving extended meaning beyond their predefined operational meaning.
#For example operator + is used to add two integers as well as join two strings and merge two lists.
#It is achievable because + operator is overloaded by int class and str class. 
#You might have noticed that the same built-in operator or function shows different behavior for objects of different classes,
# this is called Operator Overloading.

#Example class:


class OperatorOverLoading(object):
    def __init__(self,a):
        self.a = a
    def __add__(self,o):
        return self.a+o.a
obj1 = OperatorOverLoading(1)
obj2 = OperatorOverLoading(1)
obj3 = OperatorOverLoading('uday')
obj4 = OperatorOverLoading('kumar')
#print (obj3+obj4)

##########################################################################

#Polymorphism
#To use common interface for multiple form (data types)
#Suppose, we need to color a shape, there are multiple shape option (rectangle, square, circle). 
#However we could use same method to color any shape. This concept is called Polymorphism.

#Polymorphism of class
class WaterBottile:
    def get_color(self):
        return "RED"
class Laptop:
    def get_color(self):
        return "BLUE"

#common interface for both class

def common_interface(thing):
    return thing.get_color()

wb = WaterBottile()
lp = Laptop()

#print (common_interface(lp))

#Polymorphism of function
def sums(*args):
    return sum(args)

#print (sums(1,2,3))

##########################################################################

#Encapsulation
#we can restrict access to methods and variables. 
#This prevent data from direct modification which is called encapsulation.
#In Python, we denote private attribute using underscore as prefix i.e single " _ " or double "__".

class Student:
    def __init__(self):
        self.__pass_Marks = 35
    def printPassMarks(self):
        return self.__pass_Marks
    def set_marks(self,marks):
        self.__pass_Marks = marks

obj = Student()
#print (obj.printPassMarks())

#print(obj.__pass_Marks)
obj.__pass_Marks = 100
#print(obj.__pass_Marks)
#it will not change the number
#print (obj.printPassMarks())

#now number will change
#obj.set_marks(100)
#print (obj.printPassMarks())

##########################################################################

#Inheritance
#Inheritance is a way of creating new class for using details of 
#existing class without modifying it.

class Teach:
    def __init__(self,name=None):
        self.name = 'uday'
    def printTeachName(self):
        return self.name

class Stud(Teach):
    def __init__(self,age):
        self.age = age
        super().__init__()
    def printStudName(self):
        #it takes Teach name becoz of we called super().
        return self.name

#obj = Stud(90)
# print (obj.age)
# print (obj.printStudName())

##########################################################################
#lambda:---
#anonymous function means that a function is without a name. 
#This function can have any number of arguments but only one expression, which is evaluated and returned.
#One is free to use lambda functions wherever function objects are required.
#Lambda definition does not include a return statement,
#it always contains an expression which is returned.

def fun(x):
    return x*x

a=lambda x: x*x

# print (fun(2))
# print (a(2))

#Lambda functions are mainly used in combination with the functions filter(), map() and reduce()
# Syntax of map:  
#map(function_object, iterable1, iterable2,...) #multiple iterables

(list(map(lambda x: x*x,[1,2,3,4])))
(list(map(lambda x,y :x+y, [1,2,3],[4,5,6] )))

#Syntax of filter:
#filter(function_object, iterable) #one iterable onle unlike map

(list(filter(lambda x: x%2==0,[1,2,3,4,5])))

#reduce:
#The function reduce(func, seq) continually applies the function func() to the sequence seq.
#It returns a single value. 
from functools import reduce

(reduce(lambda x,y:x+y,[1,2,3,4]))
#----------------------------------
f = lambda a,b: a if (a>b) else b
#print(reduce(f,[1,2,3,4]))
##########################################################################

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.head = Node(1)
second = Node(2)
thrid = Node(3)

ll.head.next = second
second.next = thrid

#print(ll.printList())

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,new_value):
        new_data = Node(new_value)
        new_data.next = self.head
        self.head = new_data
    
    def append(self,new_value):
        new_data = Node(new_value)
        if self.head is None:
            self.head = new_data
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_data
    
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next



    def insertatnth(self, nth, value):
        self.current  = self.head
        count = 0
        while self.current:
            count += 1
            if count == nth:
                break;

            self.current= self.current.next
        obj = Node(value)
        obj.next = self.current.next
        self.current.next = obj



ll= LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.append(4)
ll.append(5)
ll.insertatnth(2,66)
#print(ll.printList())


##############################################################################################################################

d = [{'name':'uday'},{'name':'uday'}]

#{key['exam_series_id'] : ind for ind, key in enumerate(final)}
n = []
for idx,value in d:
    if value[idx] in [i['name'] for i in n]:
        pass
    else:
        n.append(key)
#print(n)


##############################################################################################################################