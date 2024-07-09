from multiprocessing import Process
import os
import time

## processing
# def square_number():
#     for i in range(100):
#         i * i 
#         time.sleep(0.1)

# processes = []
# num_processes = os.cpu_count()

# # create a process
# for i in range(num_processes):
#     p = Process(target=square_number)
#     processes.append(p)

#     # start each process
# for p in processes:
#         p.start()

#         # join
# for p in processes:
#         p.join()

# print('end main')        

# #multiprocessing
# shared value
from multiprocessing import Process, Value,Array,Lock,Pool
from multiprocessing import Queue
import os

# def add_100(number,lock):
#     for i in range(100):
#         time.sleep(0.01)
#         with lock:
#          number.value += 1
#         # lock.release()

# # def suqare_number():
# #     for i in range(1000):
# #         i * i

# if __name__ == "__main__":

#     lock = Lock()
#     shared_number = Value('i', 0)
#     print('Number st the beggining is ', shared_number.value)  


#     p1 = Process(target=add_100,args=(shared_number,lock))    
#     p2 = Process(target=add_100,args=(shared_number,lock))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print('number at end is', shared_number.value)   


def add_100(numbers,lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
         numbers[i] += 1
        # lock.release()

# def suqare_number():
#     for i in range(1000):
#         i * i


# ##shared array
# if __name__ == "__main__":

#     lock = Lock()
#     shared_array = Array('d', [0.0, 100.0,200.0])
#     print('array at beginning is the beggining is ', shared_array[:])  


#     p1 = Process(target=add_100,args=(shared_array,lock))    
#     p2 = Process(target=add_100,args=(shared_array,lock))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print('array at end  is ', shared_array[:])  
  

# #  ##shared array
# def square(numbers, queue):
#    for i in numbers:
#       queue.put(i * i)

# def make_negative(numbers,queue):
#    for i in numbers:
#       queue.put(-1 * i)    
# if __name__ == "__main__":
#     numbers = range(1 ,6)
#     q = Queue()
#     p1 = Process(target=square,args=(numbers, q))
#     p2 = Process(target=make_negative, args=(numbers, q))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     while not q.empty():
#        print(q.get())


# pool processing
#  ##shared array
def cube(number):
   return number * number * number
 
if __name__ == "__main__":
    numbers = range(10)
    pool  = Pool()

    # map apply, join,close
    result = pool.map(cube, numbers)
    pool.close()
    pool.join()

    print(result)