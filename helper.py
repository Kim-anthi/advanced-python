# import logging
# logger = logging.getLogger(__name__)
# logger.info('hello from helper')

def my_func(x):
  return x * 2

result = map(my_func, [1, 2, 3])
print(list(result))