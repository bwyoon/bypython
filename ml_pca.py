#!/usr/bin/python3

import sys
import numpy as np

if (len(sys.argv) < 3):
    sys.stderr.write("USAGE: ml_pca.py filename ncomp\n")
    exit(1)

# number of component to keep
ncomp = int(sys.argv[2])

# file read
fin = open(sys.argv[1], "r");

arr = []
condition = True
while condition:
    v = fin.readline().split()
    if len(v) > 0:
        e = [ float(v[k]) for k in range(len(v)) ]
        arr.append(e)
    else:
        condition = False
    
fin.close()

x = np.array(arr)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_sc = sc.fit_transform(x)
# x_isc = sc.inverse_transform(x_sc)

from sklearn.decomposition import PCA
pca = PCA(n_components = ncomp)
x_pca = pca.fit_transform(x_sc)
#explained_variance = pca.explained_variance_ratio_
#print(explained_variance)
print(x_pca)


#print(x_isc)
