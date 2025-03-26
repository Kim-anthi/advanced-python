#unordered and mutable and doesnt allow duplicate elements
myset ={1, 2, 3, 1, 2}
print(myset)

#using set method in a list
set0 = set([1, 2, 3, 4,]) 
print(set0)

#empty set use set method
set1 = set()
  
#change / add elements
set1.add(4)
set1.add(5)
set1.add(6)

#removing item both work the same
set1.remove(4)
set1.discard(5)

#clearing the set
# set1.clear()
print(set0.pop())
print(set1)

#iterating with for loop
for i in myset:
  print(i)
  
#checking items in set
if 1 in myset:
  print("Yees")
else:
  print("Noo")
  
#union and intersection 
#union combines two sets without duplication
odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

u = odd.union(even)
print(u)

#intersection takes same numbers in the sets
i = odd.intersection(prime)
print(i)

#difference in sets
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 10, 11, 12}

diff = a.difference(b) #symetric_difference also cool
print(diff)

#modifying items not in from b get joined
a.update(b)
print(a)

#numbers in both sets
a.intersection_update(b)
print(a)

#difference update
a.difference_update(b) #symetric_difference_difference
print(a)

#subset --->all elements in first set are all in second
#superset --->set that carries sub set
SetA= {1, 2, 3, 4, 5}
SetB= {1, 2, 3}
SetC= {7, 8, 9}

print(SetB.issubset(SetA))
print(SetA.issuperset(SetB))
print(SetA.isdisjoint(SetC))

#copying sets
setD = {1, 2, 3, 4, 5}
setE = setD.copy()

setE.add(7)
print(setD)
print(setE)

#frozen set ---> immutable version of normal set
c = frozenset([1, 2, 3, 4])
print(c)