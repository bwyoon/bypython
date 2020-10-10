#!/usr/bin/python

import pyBY
import pyBY
import sys
import math

if len(sys.argv) < 4:
    sys.stderr.write("USAGE: vectornorm ax ay az\n")
    sys.exit(1)

a = [float(sys.argv[k+1]) for k in range(0,3)]

#c = pyBY.Vector.Norm(a);
#c = pyBY.Vector.Norm(a);
print  math.sqrt(pyBY.Vector.Reduce(a, lambda sum, a: sum+a*a));
print  math.sqrt(pyBY.Vector.Reduce(a, lambda sum, a: sum+a*a));

