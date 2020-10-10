#!/usr/bin/python

import pyBY
import pyBY
import sys

if len(sys.argv) < 5:
    sys.stderr.write("USAGE: vectormultiply ax ay az c\n")
    sys.exit(1)

a = [float(sys.argv[k+1]) for k in range(0,3)]

#c = pyBY.Vector.Multiply(a, float(sys.argv[4]));
#c = pyBY.Vector.Multiply(a, float(sys.argv[4]));
c = pyBY.Vector.Map(a, float(sys.argv[4]), lambda a, c: a*c);
c = pyBY.Vector.Map(a, float(sys.argv[4]), lambda a, c: a*c);

print c[0], c[1], c[2]


