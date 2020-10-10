#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 4:
    sys.stderr.write("USAGE: molremovepMBA.py infile outfile sind1 [sind2 ..]\n")
    exit(1)

mol = pyBY.MolData()
mol = pyBY.MolData()
mol.ReadFile(sys.argv[1])
count = len(sys.argv)-3;
sind = []
for n in range(0, count):
    sind.append(int(sys.argv[n+3])-1)

melem    = ["S", "C", "C", "C", "C", "C", "C", "C", "O", "O"]
compind  = [  0,   0,   1,   1,   2,   3,   4,   6,   7,   7]
compdist = [0.0, 2.0, 1.7, 1.7, 1.7, 1.7, 1.7, 1.7, 1.5, 1.5]

atomcount = mol.GetAtomCount()
ox = [ 1 for k in range(0, atomcount) ]
for n in range(0, count):
    mind = mol.FindMoleculeWithHs(sind[n], melem, compind, compdist)
    if len(mind) >= len(melem):
        for m in range(0, len(mind)): ox[mind[m]] = 0;

mol2 = pyBY.MolData()
mol2 = pyBY.MolData()
for n in range(0, atomcount):
    if ox[n] == 1:
        x = mol.GetAtom(n)
        mol2.AppendAtom(x['elem'], x['pos'])

mol2.SetComment(mol.GetComment())
mol2.SetLatticeVectors(mol.GetLatticeVectors())
mol2.SetCellOrigin(mol.GetCellOrigin())
mol2.WriteFile(sys.argv[2])
