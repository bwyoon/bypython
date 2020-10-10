#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 6:
    eprint("USAGE: moldup.py infile outfile dx dy dz [atomfrom atomto]")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
dpos = [ float(sys.argv[k+3]) for k in range(0,3) ]
atomfrom = int(sys.argv[6])-1 if len(sys.argv) > 7 else 0
atomto   = int(sys.argv[7])-1 if len(sys.argv) > 7 else mol.GetAtomCount()-1

for n in range(atomfrom, atomto+1):
    pos = mol.GetAtomPos(n)
    mol.SetAtomPos(n, [ pos[k]+dpos[k] for k in range(0,3) ])

mol.WriteFile(sys.argv[2])

