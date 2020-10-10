#!/usr/bin/python

import pyBY
import pyBY

mol = pyBY.MolData()
mol = pyBY.MolData()

mol.ReadFile("test.xyz")
#for n in range(0,10):
#    mol.AppendAtom("Au", [ float(n), float(n), float(n) ])
#mol.DeleteAtomAt(5)

for n in range(0,mol.GetAtomCount()):
    x = mol.GetAtom(n)
    print x

#mol.SetLatticeVectors([20.0, 0.0, 0.0, 0.0, 20.0, 0.0, 0.0, 0.0, 20.0 ])
lv = mol.GetLatticeVectors()
print lv
ilv = mol.GetInverseLatticeVectors()
print ilv
mol.WriteFile("test03.xyz")
