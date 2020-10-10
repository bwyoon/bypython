#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY
import math

if len(sys.argv) < 5:
    eprint("USAGE: molangle.py infile atom1 atom0 atom2")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
angle  = mol.CalcAngle(int(sys.argv[2])-1, int(sys.argv[3])-1, int(sys.argv[4])-1)
print angle*180.0/math.pi

