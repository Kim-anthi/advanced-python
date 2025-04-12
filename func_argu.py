def print_name(name):
  print(name)
  
print_name("Kim") #Kim is the argument


#positional and keyword argument
def foo(a, b, c, d=4):
  print(a, b, c, d)
foo(1, 2, 3) #positional arguments
foo(c=1, b=2, a=3)#keyword argument and no particular order
foo(1, b=2, c=3)#can be used both but after positional argument keyword can't be used
foo(1, 2, 3, 7) #d is 4 by default but can change as per keyword argument


#ARGS AND KWARGS
def doo(a, b, *args, **kwargs):
  print(a, b)
  for arg in args:
    print(arg)
  for key in kwargs:
    print(key, kwargs[key])
    
doo(1, 2, 3, 4, 5, six = 6, seven =7)


#no.of parameters must be met
#unpacking arguments
def coo(a, b, c):
  print(a, b, c)

my_list = [0, 1, 2] 
my_tuple = (0, 1, 2) #also works with a tuple
my_dict = {'a': 1, 'b': 2, 'c': 3} #in a dict too
coo(*my_list)
coo(*my_tuple)
coo(**my_dict)


#LOCAL vs GLOBAL VARIABLE
number = 0

def glob():
  global number
  x = number
  number = 3
  print('number inside the functio:', x)


glob()
print(number)



#############
def imm(x):
  x = 5
var = 10
imm(var)
print(var)


def imm(list):
  list.append(4)
  list[0] = 100
list = [1, 2, 3]
imm(list)
print(list)