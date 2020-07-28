'''
Multitasking refers to the ability of an os to perform different tasks at the same time.
1.) Process Based: Multiple threads running on the same OS simultaneously.
    Example:Downloading,listening to song and playing a game. of various threads.
2.)Thread based:Single process consisting of separate tasks.
    Example: A game of  FIFA consists   of various threads. 

Multithreading is defined as the ability of a processor to execute multiple threads concurrently(together).
'''

# Without extending Thread class

# Without creating a class
from threading import *
def new():
    for x in range(6):
     print("Child Executing...",current_thread().getName())
t1=Thread(target=new)
# print(current_thread().getName())
t1.start()
t1.join()
print("Bye",current_thread().getName())

 
# By extending Thread class
import threading
class A(threading.Thread):
    def run(self):
        for x in range(7):
            print("Child",current_thread().getName())
a=A()
a.start()
a.join() 
print("control returned to",current_thread().getName())           

 

#Without extending Thread class
import threading
class ex(threading.Thread):
    
    def B(self):
        l=[2,1,'w',8.7,'abc']
        for x in l:
            print("Child Printing",x)
e=ex()
t1=Thread(target=e.B)
t1.start()
t1.join()
print('done')

            
#Time comparison

import time
def d2(n):
    for x in n:
        print(x%2)
def d3(n):
    for x in n:
        print(x%3)  
n=[2,4,3,6,7]         
s=time.time() 
# much time    
# d2(n)
# d3(n)
# e=time.time()
# print(e-s)
t1=Thread(target=d2,args=(n,))
t2=Thread(target=d3,args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()
#less time
e=time.time()
print(e-s)

        
        