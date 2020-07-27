t=10      # global var
def temp():
   global t # global var
   t=30     # global var
print(t)    # global var

print(t)    # global var
temp()      # global var
print(t)    #local var
    
    
 