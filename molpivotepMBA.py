#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 5:
    sys.stderr.write("USAGE: molpivotepMBA.py infile outfile sind angle\n")
    exit(1)

mol = pyBY.MolData()
mol = pyBY.MolData()
mol.ReadFile(sys.argv[1])
sind = int(sys.argv[3])-1
angle = float(sys.argv[4])

melem    = ["S", "C", "C", "C", "C", "C", "C", "C", "O", "O"]
compind  = [  0,   0,   1,   1,   2,   3,   4,   6,   7,   7]
compdist = [0.0, 2.0, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.5, 1.5]

mind = mol.FindMoleculeWithHs(sind, melem, compind, compdist)

if len(mind) < len (melem) : exit(0)

pos1 = mol.GetAtomPos(mind[0])
pos2 = mol.GetAtomPos(mind[6])
axis = pyBY.Vector.Difference(pos1, pos2)
axis = pyBY.Vector.Difference(pos1, pos2)

rot = pyBY.Rotator()
rot = pyBY.Rotator()
rot.InitMatrix()
rot.SetCenter(pos1)
rot.SetAxis(axis)
rot.Rotate(angle)

for n in range(0, len(mind)):
    mol.SetAtomPos(mind[n], rot.Transform(mol.GetAtomPos(mind[n])))

mol.WriteFile(sys.argv[2])
