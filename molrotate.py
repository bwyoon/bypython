#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 10:
    eprint("USAGE: molrotate.py infile outfile cposx cposy cposz axisx axisy axisz  angle [atomfrom atomto]")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
cpos = [ float(sys.argv[k+3]) for k in range(0,3) ]
axis = [ float(sys.argv[k+6]) for k in range(0,3) ]
angle = float(sys.argv[9])
atomfrom = int(sys.argv[10])-1 if len(sys.argv) > 11 else 0
atomto   = int(sys.argv[11])-1 if len(sys.argv) > 11 else mol.GetAtomCount()-1

rot = pyBY.Rotator()
rot = pyBY.Rotator()
rot.InitMatrix()
rot.SetCenter(cpos)
rot.SetAxis(axis)
rot.Rotate(angle)
for n in range(atomfrom, atomto+1):
    mol.SetAtomPos(n, rot.Transform(mol.GetAtomPos(n)))

mol.WriteFile(sys.argv[2])

