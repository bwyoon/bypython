#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 6:
    eprint("USAGE: moldup.py infile outfile atom1 atom2 dist")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
n1 = int(sys.argv[3])-1
n2 = int(sys.argv[4])-1
dist = float(sys.argv[5])
dd = (dist-mol.CalcDistance(n1, n2))*0.5
dir = mol.CalcUnitDirection(n1, n2)

pos1 = mol.GetAtomPos(n1)
pos2 = mol.GetAtomPos(n2)

mol.SetAtomPos(n1, [ pos1[k]-dd*dir[k] for k in range(0,3) ])
mol.SetAtomPos(n2, [ pos2[k]+dd*dir[k] for k in range(0,3) ])

mol.WriteFile(sys.argv[2])

