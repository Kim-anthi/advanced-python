#functions that return an object that can be iterated
#which is done lazily---> memory efficient

def generator():
  yield 1
  yield 2
  yield 3
  yield 4
  
#this iterates in all
g = generator()
for i in g:
  print(i)
  
#returns the first yield value and then pauses
g = generator()
value = next(g)
print(value)

#resumes and prints the next value
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)


#can also be used in other built in functions that take iterables
#adds all the values
g = generator()
print(sum(g))


def countdown(num):
  print('Starting')
  while num > 0:
    yield num
    num -= 1
    
cd = countdown(4)
value = next(cd)

print(value)

print(next(cd))
print(next(cd))
print(next(cd))

#this uses alot of memory instead use generatore
def firstn(n):
  nums = []
  num = 0
  while num < n:
    nums.append(num)
    num += 1
  return nums
print(firstn(10))
print(sum(firstn(10)))

#using a generator
def firstgenerator(n):
  num = 0
  while num < n:
    yield num
    num += 2

# print(firstgenerator(10))
print(sum(firstgenerator(10)))



#fibonacci sequence
def fibonacci(limit):
  #0 1 1 2 3 5 8 13 ....
  a, b = 1, 3 # numbers to start with
  while a < limit:
    yield a
    a, b = b, a + b
fib = fibonacci(30)
for i in fib:
  print(i)
  
  
mygenerator = ( i for i in range(10) if i % 2 == 0)
# for i in mygenerator:
print(list(mygenerator)) #converting to list