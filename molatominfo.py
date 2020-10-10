#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 3:
    eprint("USAGE: molatominfo.py infile atom")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
count = len(sys.argv)-2
for n in range(0, count):
    x  = mol.GetAtom(int(sys.argv[n+2])-1)
    print x['elem'], x['pos'][0],  x['pos'][1], x['pos'][2]

