#!/usr/bin/python

def function(a, b, c):
    return c(a, b)


print function(1,2, lambda x, y : x+y)
print function(1,2, lambda x, y : x*y)
print function(1,2, lambda x, y : x/y)
print function(1,2, lambda x, y : x%y)

def func(a, b):
    return a*b

print function(1,2, func)
