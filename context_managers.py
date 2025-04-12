#open a writtable file 
with open('notes.txt', 'w') as file:
  file.write('some todoo...')
  
  
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
  f = open(filename, 'w')
  try:
    yield f
  finally:
    f.close()
    
with open_managed_file('notes.txt') as f:
  f.write('some todoooo...')