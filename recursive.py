# find a factorial of given num using recursive function
# by normal loop

def factorial_normal (num):
    x=1
    for n in range(1,(num+1)) :
        x=x*n
    return x

print(factorial_normal(5))

# by using reccursion
def recursion(num):
    if (num == 0) :
        return 1
    else:
        return num * recursion(num-1)

print(recursion(5))