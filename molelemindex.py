#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 3:
    eprint("USAGE: molelemindex.py infile elem")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
count = 0
for n in range(0, mol.GetAtomCount()):
    if (mol.GetAtomElem(n) == sys.argv[2]):
        str = "%d " % (n+1)
        sys.stdout.write(str)
        count = count+1
if count > 0: print ""

