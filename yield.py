# Syn ==> write a function to generate even num from given range

def even_generator(num):
    for n in range(2,num+1,2):
        # return n # after riturn loop will be stop
        yield n
    
print(type(even_generator(10))) # 2
# we need to handle this yield function using for loop
# Yield return generator eterator object
for  even in even_generator(10):
    print(even)

