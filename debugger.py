'''
pdb implements an interactive debugging environments for python programs.It includes features to let you pause your program, lok at the 
values of variables, and watch executions step- by-step, so you can understand what your program actually does and find bugs in the logic.
'''
import  pdb
def seq(n):
    for i in range(n):
        pdb.set_trace()   
        print(i)
    return
seq(5)  

'''
Debugger command:
c:continue
q:quit
h:help
list
p:print
p locals()
p globals()

'''      l


