#Uses of asterisk 
#multiplication
result = 5 * 7
print(result)


#two forms power operation
result = 2 ** 4
print(result)

#creating a list 
list = [10] * 10
# also can create 2
list1= [0, 1] * 10
print(list)
print(list1)

#creating a string 
list = "AB" * 10

 
numbers = [1, 2, 3, 4, 5, 6]

*beginning, last = numbers
print(beginning)
print(last) #prints last number as single

#now this singles out the first and others as remain in list
beginning, *last = numbers
print(beginning)
print(last) 

#this for middle
beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last) 

#unpacking more numbers
beginning, *middle, secondlast, last = numbers
print(beginning)
print(middle)
print(secondlast)
print(last) 

#MERGING with asterik
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

#merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

new_dict = {**dict1, **dict2}
print(new_dict)