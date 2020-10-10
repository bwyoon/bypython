#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 2:
    eprint("USAGE: molatomcount.py infile")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
print mol.GetAtomCount()

