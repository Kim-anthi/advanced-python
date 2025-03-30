# x = 5
# if x < 0:
#   raise Exception('x should be positive')

# x = -5
# assert(x >= 0), 'x is not positive'

try:
  a = 5 / 0
except:
  print("error happened")
  
  
try:
  a = 5 / 1
  b = a + '10'
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print("everything is fine")
finally:
  print("cleaning up...")
  
  #own error classes
class ValueTooHighError(Exception):
    pass
  
def test_value(x):
    if x > 100:
      raise ValueTooHighError("value too high")

try:
  test_value(200) 
except ValueTooHighError as e:
  print(e)