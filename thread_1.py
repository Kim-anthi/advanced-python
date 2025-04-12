# In multithreading, all threads share the same memory space.
# but use Locks to avoid race conditions.

from threading import Thread
import os
import time

def square_numbers():
  for i in range(100):
    i= i
    
if __name__ == '__main__':
   threads = []
   num_threads = 10 


#create process
for i in range(num_threads):
  t = Thread(target=square_numbers)
  threads.append(t)
  
#start
for t in threads:
  t.start()
  
#join
for t in threads:
  t.join()

print('end main')

#----> race condition happens when two 
# or more threads try to modify same varian=ble at same time

from threading import Thread, Lock,current_thread
import time 

database_value = 0
lock = Lock()

def increase():
  global database_value
  global lock
  
  with lock:
    local_copy = database_value
    
    local_copy += 1
    time.sleep(0.1) #race condition, locked so no switching
    
    database_value = local_copy
  

if __name__ == '__main__':
  
  print('start value', database_value)
  
  thread1 = Thread(target=increase)
  thread2 = Thread(target=increase)
  
  thread1.start()
  thread2.start()
  
  thread1.join()
  thread2.join()
  
  print('end value', database_value)
  
  print('end main')




#queue--> linear data structure that follows FIFO
from queue import Queue

if __name__ == '__main__':
  q = Queue()
  
  q.put(1)
  q.put(2)
  q.put(3)
  
  first = q.get()
  print(first) #prints and removes the first leaving the others
  
  q.task_done() #shows task is done and not continue
  q.join() #blocks main thread and wait for all queues be processed
  
from threading import Thread, Lock,current_thread  
from queue import Queue
 
def worker(q, lock):
  while True:
    value = q.get() # blocks and wait until items are available
    
    #processing happens here
    with lock:
      print(f'in  {current_thread().name} got {value}')
    q.task_done()
  
if __name__ == '__main__':
  q = Queue()
  lock = Lock()
  num_threads = 10
  
  for i in range(num_threads):
    thread = Thread(target=worker, args=(q, lock))
    thread.daemon = True  #background thread that dies after main 
    #thread dies making the function dies and while loop no longer invoked
    thread.start()
  
  for i in range(1, 21):
    q.put(i)
    
  q.join()#unblocks
  
  print('end main')
  