# Shallow copy -- one level deep, only refernces of netsed child objects
#Deep copy -- full independent copy
original = 5
copy = original # this doesnt copy just creates a new variable with same number
copy = 6
print(original)
print(copy)

#--> hence the difference in outputs

#--> for immutable objects
#SHALLOW COPYING
import copy  
original = [1, 2, 3, 4]
# copy = copy.copy(original)  --> function same
# copy = original.copy
# cpy = list(original)
cpy = original[:]
cpy[1] = -10
print(original)
print(cpy)


#another shallow copy which happens only on one list 
# and affects the original
import copy  
original = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
copy = copy.copy(original) 
copy[0][1] = -10
print(original)
print(copy)


#deep copy --> doesn't affect original
import copy  
original = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
copy = copy.deepcopy(original) 
copy[0][1] = -10
print(original)
print(copy)

import copy  
class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      
p1 = Person('Kim', 20)
p2 = copy.copy(p1)

p2.age = 25
print(p2.age)
print(p1.age)


#shallow while the age is in second level so copy mad not right 
# and on adding deep it is normal
import copy  
class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
class Company:
  def __init__(self, boss, employee):
     self.boss = boss
     self.employee = employee

      
p1 = Person('Kim', 50)
p2 = Person('Me', 25)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)