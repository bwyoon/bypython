#!/usr/bin/python

import pyBY
import pyBY
import sys
import math

if len(sys.argv) < 7:
    sys.stderr.write("USAGE: vectordistance.py ax ay az bx by az\n")
    sys.exit(1)

a = [float(sys.argv[k+1]) for k in range(0,3)]
b = [float(sys.argv[k+4]) for k in range(0,3)]

# c = pyBY.Vector.Distance(a, b);
# c = pyBY.Vector.Distance(a, b);
c = pyBY.Vector.BinaryMap(a, b, lambda a, b: b-a)
c = pyBY.Vector.BinaryMap(a, b, lambda a, b: b-a)
print math.sqrt(pyBY.Vector.Reduce(c, lambda sum, c: sum+c*c))
print math.sqrt(pyBY.Vector.Reduce(c, lambda sum, c: sum+c*c))


