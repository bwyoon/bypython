#!/usr/bin/python

def function(a, b, c = 0):
    print a+b+c


function(1,2)
function(1,2,3)


def LessThan(cutoffval, *vals):
    arr = []
    for val in vals:
        if val < cutoffval:
            arr.append(val)
    print arr
    

LessThan(3, 1, 2, 3, 4, 5)

