#  Normal Decorator Syntax

def decor(func):
    def wrapper():
        print("decor toll both Start")
        result = func()
        print("decor toll both End")
        return result
    return wrapper
@decor
def greetings():
    return "wellcome to decor"

print(greetings())

# Write A decorator To get Time Required for the execution
import time
def fun_time_decor(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__}  ran in {end - start}")
        return result
    return wrapper
@fun_time_decor
def timer(num):
    return time.sleep(num)

timer(2)

# create A deccor to print the function name and their argument whenever
# the function called

def func_info(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg)for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}"for k,v in kwargs.items())
        print(f"Calling Func ->({func.__name__}) with args ({args_value}) And kwargs ({kwargs_value})")
        result = func(*args,**kwargs)
        return result
    return wrapper
@func_info
def greet(name , greet = "Good day"):
    return f"{name}  {greet}"
print(greet("Sonu" , greet = "Good Morning"))