#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 4:
    eprint("USAGE: molbl.py infile atom1 atom2")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
bl  = mol.CalcDistance(int(sys.argv[2])-1, int(sys.argv[3])-1)
print bl

