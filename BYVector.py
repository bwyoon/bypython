import math

def Add(a, b):
    return [ a[k]+b[k] for k in range(0,3) ] 

def Subtract(a, b):
    return [ a[k]-b[k] for k in range(0,3) ]

def Difference(a, b):
    return [ b[k]-a[k] for k in range(0,3) ]

def DotProduct(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2];

def CrossProduct(a, b):
    return [ a[1]*b[2]-b[1]*a[2], a[2]*b[0]-b[2]*a[0], a[0]*b[1]-b[0]*a[1] ]

def Multiply(a, b):
    return [ a[k]*b for k in range(0,3) ]

def Divide(a, b):
    return [ a[k]/b for k in range(0,3) ]

def Norm(a):
    return math.sqrt(DotProduct(a,a))

def UnitVector(a):
    b = Norm(a)
    return [ a[k]/b for k in range(0,3) ]

def Distance(a, b):
    return Norm(Difference(a, b))



