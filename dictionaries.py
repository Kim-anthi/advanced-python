#unordered, mutable, key value pairs where each key value
# maps its values to it's associated value
dict1 = {"name": "Kim", "age": 20, "city": "Nairobi"}
print(dict1)

#using the dict function the key values do not need to be in quotes
dict2 = dict(name="Akah", age= 14, city = "Nc")
print(dict2)

#accessing values in dictionary
value = dict2["age"]
print(value)

#add/change items after it's creation
dict2["email"] = "kim@gmail.com"
print(dict1)
#so doing this again overwrites the last one
dict2["email"] = "yeikim@gmail.com"
print(dict1)


#deleting items
del dict2["age"]
print(dict2)

dict2.pop("name")
print(dict2)

dict2.popitem() #now this happens to remove the last item
print(dict2)

#checking items in the dictionary
if "city" in dict2:
  print("yes")
else:
  print("nooo")
 #using try and except method 
try:
 print(dict2["city"])
except:
  print("errror")
  
#looping through a dictionary
  
for value in dict1.values(): #this for
#values for keys replace value with key in the method too
  print(value)
  
#can also be printed both
for key, value in dict1.items():
  print(key, value)


#copying a dictionary  -----> this if altered won't be effucient
dict1_copy = dict1 
dict1_copy = dict1.copy() #---> prints original as copy

dict1_copy["email"] = "@ayagmail.com"
print(dict1_copy)
print(dict1)


#update two dictionaries
diction = {"name":"brr", "age": 21, "email": "brr@gmail.com"}
diction2 = dict(name="dre", age=20, city="Acapulco")

diction.update(diction2)
print(diction)

#possible key types
dictionary = {3: 9, 6: 36, 9: 81}
print(dictionary)

value = dictionary[3] #accessed using key instead of index
print(value)