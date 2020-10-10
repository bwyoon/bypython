#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 2:
    eprint("USAGE: mollv.py molfile")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
lv = mol.GetLatticeVectors();
print lv[0], lv[1], lv[2]
print lv[3], lv[4], lv[5]
print lv[6], lv[7], lv[8]

