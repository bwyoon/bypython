#!/usr/bin/python

import pyBY
import pyBY

rot = pyBY.Rotator()
rot = pyBY.Rotator()
rot.SetCenter([0.0, 0.0, 0.0])
rot.SetAxis([0.0, 0.0, 1.0])
rot.Rotate(30.0)
rot.Rotate(30.0)
pos1 = [1.0, 0.0, 0.0]
pos2 = rot.Transform(pos1)

print pos1
print pos2
