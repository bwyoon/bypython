#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 4:
    eprint("USAGE: molbl.py infile atom1 dcutoff")
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
mol = pyBY.MolData().ReadFile(sys.argv[1])
atom = int(sys.argv[2])-1
dcutoff = float(sys.argv[3])

x = mol.GetAtom(atom)
print("%5d %4s %10.5f %10.5f %10.5f : %10.5f" % (atom+1, x['elem'], \
      x['pos'][0], x['pos'][1], x['pos'][2], 0.0))

for n in range(0, mol.GetAtomCount()):
    if n != atom:
        d = mol.CalcDistance(atom, n)
        if d < dcutoff:
            x = mol.GetAtom(n)
            print("%5d %4s %10.5f %10.5f %10.5f : %10.5f" % (n+1,
                  x['elem'], x['pos'][0], x['pos'][1], x['pos'][2], d))

