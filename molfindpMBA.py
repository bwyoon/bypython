#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 4:
    sys.stderr.write("USAGE: molfindpMBA.py infile outfile sind\n")
    exit(1)

mol = pyBY.MolData()
mol = pyBY.MolData()
mol.ReadFile(sys.argv[1])
sind = int(sys.argv[3])-1

melem    = ["S", "C", "C", "C", "C", "C", "C", "C", "O", "O"]
compind  = [  0,   0,   1,   1,   2,   3,   4,   6,   7,   7]
compdist = [0.0, 2.0, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.5, 1.5]

mind = mol.FindMoleculeWithHs(sind, melem, compind, compdist)

if len(mind) < len (melem) : exit(0)

mol2 = pyBY.MolData()
mol2 = pyBY.MolData()

for n in range(0, len(mind)):
    x = mol.GetAtom(mind[n])
    mol2.AppendAtom(x['elem'], x['pos'])

mol2.SetComment(mol.GetComment())
mol2.SetCellOrigin(mol.GetCellOrigin())
mol2.SetLatticeVectors(mol.GetLatticeVectors())
mol2.WriteFile(sys.argv[2])
