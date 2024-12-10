# write a function to generate  even num and we want to multiply each 
# even num by 10

def even_generator(num):
    for even in range(2,num+1,2):
        # return even # we can not return this inside loop because after return loop will be stop
        yield even
for even in even_generator(20):
    print(even*10) # we need to handle with for loop
# yeild return generator object
