add10 = lambda x: x + 10
print(add10(5))


def add10_func(x):
  return x + 10

mult = lambda x,y: x * y
print(mult(2,7))

#sergeant
points = [(1, 2), (15, 2), (5, -1), (10, 3)]

# def sort_by_y(x):
#   return x[1]
points_sorted = sorted(points, key=lambda x: x[1])
print(points)
print(points_sorted)


#map function
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)

#filter function
a = [1,2,3,4,5,6]
b = filter(lambda x: x%2 == 0, a)
print(list(b))

c = [x for x in a if x%2 ==0]
print(c)


#reduce unction
from functools import reduce
a = [1,2,3,4,5,6] 
product = reduce(lambda x, y: x * y, a)
print(product)

