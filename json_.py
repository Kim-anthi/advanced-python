#converting from python dictionary to json
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4) #sort_keys=True
print(personJSON)

#dump it to a file
with open('person.json', 'w') as file:
  json.dump(person, file, indent=4)
  
  
#converting from json to python dictionary
person = json.loads(personJSON)
print(person)

#converting from json file to dictionary
with open('person.json', 'r') as file: #r for reading the file
  person = json.load(file)
  print(person)
  
  
  
  
class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

user = User('Max', 27)

#this for changing to dictionary so as to change to JSON
def encode_user(o):
  if isinstance(o, User):
    return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
  else:
    raise TypeError('Object of type user is not json serializiable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)