#!/usr/bin/python

import pyBY
import pyBY
import sys

if len(sys.argv) < 7:
    sys.stderr.write("USAGE: vectordotproduct.py ax ay az bx by az\n")
    sys.exit(1)

a = [float(sys.argv[k+1]) for k in range(0,3)]
b = [float(sys.argv[k+4]) for k in range(0,3)]

#c = pyBY.Vector.DotProduct(a, b);
#c = pyBY.Vector.DotProduct(a, b);
print pyBY.Vector.BinaryReduce(a, b, lambda sum, x, y : sum+x*y, 0.0);
print pyBY.Vector.BinaryReduce(a, b, lambda sum, x, y : sum+x*y, 0.0);


