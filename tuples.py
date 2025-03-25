#tuple is similar to list only that once created can't be changed
mytuple = ("Max", 28, "Nairobi") #can also work without paranthesis
print(mytuple)

#if wanting to have only one element inside the tuple it must 
# end with a comma otherwise it is recognized oanother way
mytuple = ("Max",)
print(mytuple)

#creating a tuple from iterable i.e list uses tuple inbuilt func
mytuple = tuple(["Kim", 20, "3rd Year"])
print(mytuple)

#accessing items
item = mytuple[-2] #same as list negative starts from the very end
print(item)

#Iterating items in a tuple using for loop
for i in mytuple:
  print(i)
  
#checking itmes in tuple using if statement
if "Kim" in mytuple:
  print("yess")
else:
  print("noo")
  

my_tuple = ('a', 'b', 'c', 'd', 'e', 'b', 'c')

#checking length of tuple
print(len(my_tuple))

#counting elements in a tuple
print(my_tuple.count('a')) 

#checkin index of specific elements
print(my_tuple.index('c')) 

#convert tuple list and vice versa
my_list = list(my_tuple)
print(my_list)

#back to tuple 
my_tuple2 = tuple(my_list)
print(my_tuple2)

#slicing in tuple
a = (1, 2, 3, 4, 5, 6, 7, 8,)
b = a[2:7] #last index not included in this case 6
#if no stop index it goes all the way to end and vice versa
print(b)

#with a step of an index
a = (1, 2, 3, 4, 5, 6, 7, 8,)
b = a[::3]
print(b)

#reversing
a = (1, 2, 3, 4, 5, 6, 7, 8,)
b = a[::-1]
print(b)

#unpacking from a tuple
tuple = "cups", "chelsea", 16

trophies, team, number = tuple
print(trophies)
print(team)
print(number)

#unpacking using star
tuple2 = 0, 1, 2, 3, 4, 5

i1, *i2, i3 = tuple2
print(i1)
print(i3)
print(i2)

#comparing a tuple to a list using bytes  this happens to be the same
import sys
my_list2 = [0, 1, 2, "hello", True]
my_tuple3 = [0, 1, 2, "hello", True]
print(sys.getsizeof(my_list2), "bytes")
print(sys.getsizeof(my_tuple3), "bytes")

#comparing using the time method basically execution time
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5,]", number=1000000))
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5,]", number=1000000))