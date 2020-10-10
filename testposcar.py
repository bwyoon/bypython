#!/usr/bin/python

import pyBY
import pyBY

mol = pyBY.MolData()
mol = pyBY.MolData()

mol.ReadFile("POSCAR")
#for n in range(0,10):
#    mol.AppendAtom("Au", [ float(n), float(n), float(n) ])
#mol.DeleteAtomAt(5)

print mol.GetAtomCount()
for n in range(0, 10):
    x = mol.GetAtom(n)
    print x

#mol.SetLatticeVectors([20.0, 0.0, 0.0, 0.0, 20.0, 0.0, 0.0, 0.0, 20.0 ])
lv = mol.GetLatticeVectors()
print lv
ilv = mol.GetInverseLatticeVectors()
print ilv
mol.SetKeyValue('poscardirect', 0)
mol.WriteFile("copy.POSCAR")
