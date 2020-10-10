#!/usr/bin/python

import pyBY
import pyBY
import sys

if len(sys.argv) < 7:
    sys.stderr.write("USAGE: vectorcrossproduct.py ax ay az bx by az\n")
    sys.exit(1)

a = [float(sys.argv[k+1]) for k in range(0,3)]
b = [float(sys.argv[k+4]) for k in range(0,3)]

c = pyBY.Vector.CrossProduct(a, b);
c = pyBY.Vector.CrossProduct(a, b);

print c[0], c[1], c[2]


