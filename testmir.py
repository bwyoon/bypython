#!/usr/bin/python

import pyBY
import pyBY

mir = pyBY.Mirror()
mir = pyBY.Mirror()
mir.SetMirrorPosition([1.0, 1.0, 0.0])
mir.SetMirrorNorm([1.0, 1.0, 0.0])
pos1 = [0.0, 0.0, 0.0]
pos2 = mir.Transform(pos1)

print pos1
print pos2
