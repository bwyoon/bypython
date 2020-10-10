#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 2:
    eprint("USAGE: molcm.py infile [atomfrom atomto]")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
atomfrom = int(sysargv[2])-1 if len(sys.argv) >= 4 else 0
atomto   = int(sysargv[3])-1 if len(sys.argv) >= 4 else mol.GetAtomCount()-1

cm = [ 0.0 for k in range(0, 3) ]
for n in range(atomfrom, atomto+1):
    pos = mol.GetAtomPos(n)
    cm  = [ cm[k]+pos[k] for k in range(0,3) ]
cm = [ cm[k]/float(atomto-atomfrom+1) for k in range(0,3) ]

print cm[0], cm[1], cm[2]

