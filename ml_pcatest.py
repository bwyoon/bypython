#!/usr/bin/python3

import sys
import numpy as np

if (len(sys.argv) < 2):
    sys.stderr.write("USAGE: ml_pcatest.py filename\n")
    exit(1)


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

from sklearn.decomposition import PCA
pca = PCA(n_components = None)
x_pca = pca.fit_transform(x_sc)
explained_variance = pca.explained_variance_ratio_
print(explained_variance)

