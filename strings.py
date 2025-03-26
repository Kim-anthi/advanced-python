#used for text representation
string = 'I\'m Kimanthi' #slash for the apostrophe to work
print(string)

#triple quotes for multiple lines
string1 = """hello 
world"""
print(string1)

#backslash to continue another line but not create new line
string0 = """hello \
world"""
print(string0)

#getting items in a string
mystring = "Hello there"
char = mystring[1]
print(mystring)

#access substring with slicing
mystring = "Hello there"
substring = mystring[1:3]
print(substring)

#adding strings
greeting = "Hello"
name = "Kim"
sentence = greeting + " " + name
print(sentence)

#iterating 
name = "cup"
for i in name:
  print(i)

#check if item is in string
greeting = "jambo"
if 'p' in greeting:
  print("yyee")
else:
  print("noo")
  
#removing wide space 
greeting = "  jambo  "
greeting = greeting.strip()
print(greeting)

#convert characters to uppercase,,,lower change method
ate = "food is good"
print(ate.upper())

#start with and end with
print(ate.endswith("s"))

#find index
print(ate.find('is'))

#count of items in string
print(ate.count('s'))

#replacing 
print(ate.replace('good', 'awesome'))

#converting to list 
sent = 'how was your morning' #looks for space 
sent = sent.split()
print(sent)

#if there is no space
brr = 'how,was,your,morning'
brrlist = brr.split(",")
print(brrlist)
newbrr = ' '.join(brrlist)
print(newbrr)

#from list to string
mystring1 = ['b'] * 6
print(mystring1)

mystring1 = ''.join(mystring1)
print(mystring1)


#formating string
#with %
#%s --> for string, %d --> decimal, %f --> float
var = "Jerry"
str = "the variable is %s" % var 
print(str)

#format method
var = 3.142
str = "the variable is {}".format(var)
print(str)
