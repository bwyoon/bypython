#!/usr/bin/python

import pyBY
import pyBY
import sys

if len(sys.argv) < 7:
    sys.stderr.write("USAGE: vectordifference.py ax ay az bx by az\n")
    sys.exit(1)

a = [float(sys.argv[k+1]) for k in range(0,3)]
b = [float(sys.argv[k+4]) for k in range(0,3)]

#c = pyBY.Vector.Difference(a, b);
#c = pyBY.Vector.Difference(a, b);
c = pyBY.Vector.BinaryMap(a, b, lambda x, y : y-x);
c = pyBY.Vector.BinaryMap(a, b, lambda x, y : y-x);

print c[0], c[1], c[2]


