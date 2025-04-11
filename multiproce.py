from multiprocessing import Process
import os


def square_numbers():
  for i in range(100):
    i= i
    

if __name__ == '__main__':
  processes = []
  num_process = os.cpu_count() #no of CPU's on machine

  #create process
  for i in range(num_process):
    process = Process(target=square_numbers)
    processes.append(process)
  
  #start
  for process in processes:
    process.start()
    
  #join
  for process in processes:
    process.join()

  print('end main')




