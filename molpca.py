#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import numpy as np

if len(sys.argv) < 2:
    print('USAGE: {} infile'.format(sys.argv[0]))
    exit(1)

mol = pyBY.MolData().ReadFile(sys.argv[1])
pos = mol.GetAtomPosList()
covmat = np.cov(np.array(pos).T)
v, eig = np.linalg.eig(covmat)
print(v)
print(eig)

