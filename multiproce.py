# In multiprocessing, processes don't share memory.
# To share data, use special shared memory objects like Array or Value.
from multiprocessing import Process, Value, Array, Lock
import os
import time
from multiprocessing import Queue #first in first out


# def square_numbers():
#   for i in range(100):
#     i= i
    

# if __name__ == '__main__':
  # processes = []
  # num_process = os.cpu_count() #no of CPU's on machine

  # #create process
  # for i in range(num_process):
  #   process = Process(target=square_numbers)
  #   processes.append(process)
  
  # #start
  # for process in processes:
  #   process.start()
    
  # #join
  # for process in processes:
  #   process.join()

  # print('end main')
  
  
  #VALUE ---> single value
  #race condition below happens because more than one process
  #tries to access the object at same time prevented by lock
  #lock makes sure that only one process runs at time 
  #passed as argument too

# def add_100(number, lock):
#   for i in range(100):
#     time.sleep(0.01)
#     with lock:
#       number.value += 1
  
  
# if __name__ == '__main__':
#   lock = Lock()
#   shared_number = Value('i', 0) #give datatype as string
#   print('Number at beggining is', shared_number.value)
    
#   process1 = Process(target= add_100, args=(shared_number, lock))
#   process2 = Process(target= add_100, args=(shared_number, lock))
  
#   process1.start()
#   process2.start()
  
#   process1.join()
#   process2.join()
  
#   print('number at end is', shared_number.value)





#----> for ARRAY
# def add_100(numbers, lock):
#   for i in range(100):
#     time.sleep(0.01)
#     for i in range(len(numbers)):
#       with lock:
#         numbers[i] +=1
  
  
# if __name__ == '__main__':
#   lock = Lock()
#   shared_array = Array('d', [0.0, 100.0, 200.0]) #give datatype as string
#   print('Array at beggining is', shared_array[:])
    
#   process1 = Process(target= add_100, args=(shared_array, lock))
#   process2 = Process(target= add_100, args=(shared_array, lock))
  
#   process1.start()
#   process2.start()
  
#   process1.join()
#   process2.join()
  
#   print('Array at end is', shared_array[:])
  
  
  
  #QUEUE to exchange data between multiple processes
  
def square(numbers, queue):
   for i in numbers:
     queue.put(i*i)
  
def make_negative(numbers, queue):
    for i in numbers:
      queue.put(-1*i)
  
  
if __name__ == '__main__':
  numbers = range(1, 6)
  q = Queue()
  
  proc1 = Process(target=square, args=(numbers, q))
  proc2= Process(target=make_negative, args=(numbers, q))
  
  proc1.start()
  proc2.start()
  
  proc1.join()
  proc2.join()
  
  while not q.empty():
    print(q.get())
    
    
#PROCESS POOL ---> controls pool of worker process
# to which chops can be submitted and manages available 
# processes and splits to smaller chunks that can be processed 
#parallel by different processes

from multiprocessing import Pool

def cube(number):
  return number * number * number


if __name__ == '__main__':
  numbers = range(10)
  pool = Pool()
  
  #map, apply, join, close
  result = pool.map(cube, numbers)
  #pool.apply(cube, numbers[0]) --> executes only one function
  
  pool.close()
  pool.join()
  print(result)
