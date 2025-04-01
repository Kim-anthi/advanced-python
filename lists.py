#Lists; ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

#allows duplicate items 
mylist2 = [5, True, "apple", "apple"]
print(mylist2)

#accessing items in a list
item = mylist2[1]
print(item)

#also can be accessed by negative where -1 is the last item 
# while -2 is the second last and goes on like that
item = mylist2[-4]
print(item)

#iterating in a list can be done in a for loop
for i in mylist2:
  print(i)
  
#checking items is in a list using if
if "apple" in mylist:
  print("yes")
else:
  print("No")
  
#checking number of elements in a list
print(len(mylist2))

#adding items in alist (appending)
mylist2.append("lemon")
print(mylist2)

#inserting items in a list
mylist2.insert(1, "blueberry")
print(mylist2)

#remove items which returns last item and removes it
item = mylist2.pop()
print(item)
print(mylist2)

#also removing an item completely
item = mylist2.remove(5)
print(mylist2)

#remove all items with the clear method
item = mylist2.clear()
print(mylist2)

#reversing the list
item = mylist.reverse()
print(mylist)

#sorting the list
list = [5, 2, 4, -1, 0, -8]
print(list)

item = list.sort()
print(list)

#we can also print a sorted list 
# but also leaving the original list
new_list = sorted(list)
print(list)
print(new_list)

#creating a list with same items
lyst = [5]  * 4
print(lyst)

#also add two lists together
lyst2 = [1, 2, 3, 4]

listnew = lyst + lyst2
print(listnew)

#slicing list 
liist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = liist[2:7] #indexes of which items to slice
#failing to specify the start and stop index means 
# it starts till end index and vice versa
print(a)

#so with two colons we can make it select the indexes we want
#with the desired index spacing
#basically with step of specified index
liist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = liist[::3] 
print(a)

#also specifying a negative reverses the list
liist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = liist[::-1] 
print(a)

#copying a list
list_original = ["banana", "oranges", "pears"]

list_copy = list_original.copy()
list_copy = list_original[:] #also makes original copy by slicing

list_copy.append("lemon") #making a change in the copied list 
#changes the original even so do it we need the copy method
print(list_original)
print(list_copy)

#list comprehension- making new list from existing list
a = [1, 2, 3, 4, 5, 6] 
b = [i*i for i in a]  #simply squaring a list

print(a)
print(b)

