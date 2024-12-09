# *args ==> To take multiple Argument from function

def args_func_1(*args):
    return sum(args)

print(args_func_1(1,3,5,7))
# we can iterate args 
def args_func_2(*args):
    x = 0
    for i in args:
        x=i+x
    return x
print(f"Total Is ==> ",{args_func_2(1,3,5,7)})

# **Kargs Use for Key Value type parameter passing
def kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
        
kwargs( name= "Saktiman" , power = "Laser" , enimy = "Jaykal")