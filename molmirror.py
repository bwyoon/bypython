#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 9:
    eprint("USAGE: molmirror.py infile outfile mposx mposy mposz normx normy normz [atomfrom atomto]")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
mpos = [ float(sys.argv[k+3]) for k in range(0,3) ]
mnor = [ float(sys.argv[k+6]) for k in range(0,3) ]
atomfrom = int(sys.argv[9])-1 if len(sys.argv) > 10 else 0
atomto   = int(sys.argv[10])-1 if len(sys.argv) > 10 else mol.GetAtomCount()-1

mir = pyBY.Mirror()
mir = pyBY.Mirror()
mir.SetMirrorPosition(mpos)
mir.SetMirrorNorm(mnor)
for n in range(atomfrom, atomto+1):
    mol.SetAtomPos(n, mir.Transform(mol.GetAtomPos(n)))

mol.WriteFile(sys.argv[2])

