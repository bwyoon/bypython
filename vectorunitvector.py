#!/usr/bin/python

import pyBY
import pyBY
import sys
import math

if len(sys.argv) < 4:
    sys.stderr.write("USAGE: vectorunitvector ax ay az\n")
    sys.exit(1)

a = [float(sys.argv[k+1]) for k in range(0,3)]

# pyBY.Vector.UnitVector(a);
# pyBY.Vector.UnitVector(a);
n = math.sqrt(pyBY.Vector.Reduce(a, lambda sum, a: sum+a*a))
n = math.sqrt(pyBY.Vector.Reduce(a, lambda sum, a: sum+a*a))
c = pyBY.Vector.Map(a, n, lambda a, n : a/n)
c = pyBY.Vector.Map(a, n, lambda a, n : a/n)

print c[0], c[1], c[2]


