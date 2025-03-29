#product 
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b) 
print(list(prod))

#using repeat
a = [1,2]
b = [3]
prod = product(a,b, repeat=2) 
print(list(prod))


#permutations ---> return all possible orderings
from itertools import permutations
c= [4,5,6]
perm =permutations(c) #length also specified
print(list(perm))


#combinations --> make all possible commbination with specified length
from itertools import combinations, combinations_with_replacement
c= [1,2,3,4]
comb = combinations(c,2)
print(list(comb))

#this allows repetition
comb_wr = combinations_with_replacement(c,2)
print(list(comb_wr))



#accumulate --> iterate for returning acumulate function
from itertools import accumulate
d = [1,2,3,4]
acc = accumulate(d)
print(d)
print(list(acc))

#multiplying
import operator
acc = accumulate(d, func=operator.mul)
print(list(acc))

#max--> return max for each
e = [1,2,5,4,6,7]
acc = accumulate(e, func=max)
print(list(acc))


#groupby --> makes iterator that returns keys and groups from iterables
from itertools import groupby

def smaller_than_3(x):
  return x < 3

f = [1,2,3,4]
group = groupby(a, key=smaller_than_3)
for key, value in group:
  print(key, list(value))

persons = [{"name": "HJ", 'age': 21, }, {"name": "hhhj", 'age': 20, },
           {"name": "ghjk", 'age': 23, }, {"name": "hbnbb", 'age': 19, }]

persons_group = groupby(persons, key=lambda x: x['name'])
for key, value in persons_group:
  print(key, list(value))
  
  

#infinite iterators
from itertools import count, cycle, repeat

for i in count(10):
  print(i)
  if i == 15:
    break

g = [1,2,3]
for i in cycle(g):
  print(g)
  if i == 3: 
    break
  
h = [6,7,8]
for i in repeat(1, 3): #1 times for repeat and 3 the break point
  print(h)
 