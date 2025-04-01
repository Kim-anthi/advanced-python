#generate random pseudo numbers for various distributions
import random 

a = random.random()
print(a)

#with range --> brings float number
a = random.uniform(1,8)
print(a)

#range but with whole numbers
#randit includes the last number 
a = random.randrange(1,8) #rand range doesnt include last number
print(a)

#normalvariate
a = random.normalvariate(1, 2)#1 --> mean 2--> std deviation
print(a)

#picking 1 random from a list
mylist = list("ABCDEFG")
b = random.choice(mylist)
print(b)

#picking desired random from a list 
#also picks unique no repetition
mylist = list("ABCDEFG")
b = random.sample(mylist, 3)
print(b)

#picking and allowing repetition
mylist = list("ABCDEFG")
b = random.choices(mylist, k=3)
print(b)

#random shuffle 
mylist = list("ABCDEFG")
random.shuffle(mylist)
print(mylist)


import secrets
d = secrets.randbelow(10)
print(d)

#can have random binary values as specified
import secrets
e = secrets.randbits(4)
print(e)

# an array
import numpy as np
f = np.random.rand(3) #here define how it should be
print(f)

f = np.random.randint(0, 10, 7) #7 is the size
print(f)

f = np.random.randint(0, 10, (3, 3)) #3, 3 is the change to tuple
print(f)

#shuffling in the array
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)