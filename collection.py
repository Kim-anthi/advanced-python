#Counter --> container that stores elements as dictionary keys
#and counts as dictionary values
from collections import Counter 

a = "aaaaabbbcccc"
my_counter = Counter(a)
print(my_counter)
#change to list
print(list(my_counter.elements()))
#most common items
print(my_counter.most_common(1)) #1 for most common 2 for most common

b = "ddddeeeeefffff"
my_counter1 = Counter(b)
print(my_counter1.items()) #keys, values


#Namedtuple
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
#for accessing points
print(pt.x, pt.y)

from collections import namedtuple
Fruit = namedtuple('Fruit', 'mango,banana')
tunda = Fruit("ripe", "yellow")
print(tunda)


#Ordered dictionaries
from collections import OrderedDict
ordered_dict = {}
ordered_dict['e'] = 5
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict)



#Default dict
from collections import defaultdict
d =defaultdict(int) #list, float all here
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

print(d)
print(d['a']) #accessing



#deque 
from collections import deque
f = deque()
f.append(1)
f.append(2)

#add elements to desired side
f.appendleft(3)

print(f)

#remove elements
f.pop()  #f.popleft(), clear
f.extend([4, 5, 6])#f.extendleft
print(f)
f.rotate()  #f.extendleft
print(f)  
