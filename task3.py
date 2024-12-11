#3 what are python decorators?
def decorator (func):
    def wrapp():
        print("Before function call")
        func()
        print("After function call")
    return wrapp
@decorator
def say_hello():
    print("hello")
say_hello()
print("****************")
#4 What is difference between deep copy and shalloaw copy?
import copy
origin=[[1,2,33,7,55,64]]
sha= copy.copy(origin)
dep=copy.deepcopy(origin)
sha[0][2]=28
dep[0][0]=102
print(sha)
print(dep)
print("****************")
#5 Explain python's memory management and use of del
x = 5.5
print(x)  # Output: 10
del x   # after print(x)  # This will raise a NameError because `x` no longer exists.
numlist= [11,23,83,44,95]
del numlist[2]  # Removes the element at index 1
print(numlist)  # Output: [11,23,44,95]
del numlist[1:3]  # Removes a slice (elements at index 1 and 2)
print(numlist)  # Output: [11,95]
perinfo = {'name': 'Amita', 'age': 33,'degree':'BCS'}
print(perinfo)
del perinfo['age']  # Removes the 'age' key
print(perinfo)  # Output: {'name': 'Amita','degree':'BCS'}
#6 What is difference between 'is' and '==' in python?
print("****************")
a=[22,56]
b=[22,56]
print(a==b)# True if values are same
print(a is b)# false if different memory location
b=a
print(a is b)# True if same memory location
#7 How does python handle mutable and immutable objects?
print("****************")
# Mutable objects
li=[11,4,9,16]
li[0]=1
print(li)# output[1,4,9,16] 
# immutable
tu=(11,22,33)
# tu[0]=44 #raise an error
print("****************")
#8 What are python datatypes?
# Numeric
x=11
y=3.89
z=11+2j
# Sequence
li=[22,33,55,88.2]
print(type(li))
tup=(1,4,9,16)
print(type(tup))
ra= range(0, 10,2)  # Generates numbers from 1 to 9, stepping by 2
print(list(ra))  # Output: [0,2,4,6,8]
print(type(ra))
tx='amita'
print(type(tx))
#mapping
dict={'Name':'amita','Degree':'Bcs','Age':33}
print(type(dict))
se={1,5,8,3,4,6,7}
print(se)# set is ordered collection of unique elements
print(type(se))
st=[5,8,9,1,2,1]
fro= frozenset(st)#forzenset is ordered collection of unique elements and immutable
print(type(fro))
print(fro)  # Output: frozenset({1,2,5,8,9})
bol = 5 > 3
print(bol)  # Output: True
print(type(bol))
print("****************")
#9 What is difference between @staticmethod,@classmethod,and instance method?
class Example:
    def instance_method(self):
        return "Instance method called",self

    @classmethod
    def class_method(cls):
        return "Class method called", cls

    @staticmethod
    def static_method():
        return "Static method called"
obj = Example()  # Create an instance and calling by instance method
print(obj.instance_method())
print(Example.class_method())# calling by class method
result = Example.static_method()# calling by static method
print(result)
print("****************")
#10 What are python's comprehension techniques?
# list comprehension
squares = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]
print(squares)
# dictionary comprehension
squares_dict = {x: x **2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(squares_dict)
# set comprehension
squares_set = {x ** 2 for x in range(5)}  # {0, 1, 4, 9, 16}
print(squares_set)
print("****************")
#11 How would you handle exceptions in python?
try:
    x = int("not_a_number")
except ValueError as e:
    print(f"Error: {e}")#Error: invalid literal for int() with base 10: 'not_a_number'
finally:
    print("This block always executes.")
print("****************")
#12 Explain Python's 'with' statement.
with open ("outp.py","r")as file:
    content=file.read()
    print(content)
print("****************")
#13 How does Python implement inheritence?
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")
chi=Child()
chi.greet()
print("****************")
#14 What are Pythons itertors and geneators?
numbers = [11, 32, 63]
iterator = iter(numbers)# Create an iterator from the list
print(next(iterator))  # Output: 1# Access elements using next()
print(next(iterator))  # Output: 2
def generator():
    for i in range(3):
        yield i

gen = generator()
print(next(gen))  # 0
print(next(gen))  # 1
print("****************")
#15 What is difference between copy()and deepcopy()?
lio=[[22,88,99,77]]
co=copy.copy(lio)
depco=copy.deepcopy(lio)
lio[0][2]=110# modify also co list
depco[0][1]=66# doesnot modify original list
print(lio)
print(co)
print(depco)

