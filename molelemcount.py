#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 2:
    eprint("USAGE: molelemcount.py infile")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
elemlist = []
elemcount = {}
for n in range(0, mol.GetAtomCount()):
    elem = mol.GetAtomElem(n)
    if elem in elemcount : elemcount[elem] = elemcount[elem]+1
    else : elemlist.append(elem); elemcount[elem] = 1

for e in elemlist:
    print e, elemcount[e]

