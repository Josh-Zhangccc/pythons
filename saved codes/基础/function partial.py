from functools import partial
 

def anyfunc(a,b,c):
    return a**(b**c)

square=partial(anyfunc,b=2,c=1)

print(square(3)) 