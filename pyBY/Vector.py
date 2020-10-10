import math

def Add(a, b):
    return [ a[k]+b[k] for k in range(0,3) ] 

def Subtract(a, b):
    return [ a[k]-b[k] for k in range(0,3) ]

def Difference(a, b):
    return [ b[k]-a[k] for k in range(0,3) ]

def Multiply(a, b):
    return [ a[k]*b for k in range(0,3) ]

def Divide(a, b):
    return [ a[k]/b for k in range(0,3) ]

def DotProduct(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def Norm(a):
    return math.sqrt(DotProduct(a,a))

def Distance(a, b):
    return Norm(Difference(a, b))

def CrossProduct(a, b):
    return [ a[1]*b[2]-b[1]*a[2], a[2]*b[0]-b[2]*a[0], a[0]*b[1]-b[0]*a[1] ]

def UnitVector(a):
    b = Norm(a)
    return [ a[k]/b for k in range(0,3) ]

def Map(a, c, op):
    return [ op(a[k], c) for k in range(0,3) ]

def BinaryMap(a, b, op):
    return [ op(a[k], b[k]) for k in range(0,3) ]

def BinaryReduce(a, b, op, initval = 0):
    c = initval
    for k in range(0,3):
        c = op(c, a[k], b[k])
    return c 

def Reduce(a, op, initval = 0):
    c = initval
    for k in range(0,3):
        c = op(c, a[k])
    return c 




