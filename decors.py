#function decoraters
#--> takes another function as argument extending it without modifying it

# def start_end_decorater(func):
#   def wrapper():
#     print('start')
#     func()
#     print('end')
#   return wrapper


# @start_end_decorater
# def print_name():
#   print('Alex')
  
# # print_name = start_end_decorater(print_name)
# print_name()


import functools
def start_end_decorater(func):
  
  functools.wraps(func)
  def wrapper(*args, **kwargs):
    print('start')
    result = func(*args, **kwargs)
    print('end')
    return(result)
  return wrapper


@start_end_decorater
def add5(x):
  return x + 5
  
# print_name = start_end_decorater(print_name)

print(help(add5))
print(add5.__name__)
result = add5(10)
print(result)


  
  
  
def repeat(num_times): #outer function
    def decorator_repeat(func):#decorater unction
        @functools.wraps(func)
        def wrapper(*args, **kwargs):#wrapper 
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet('Alex')


class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(num):
    print("Hello!")

say_hello(5)
say_hello(5)