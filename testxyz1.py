#!/usr/bin/python

import xyzfile as xyz

natom, comment, data = xyz.ReadFile('test.xyz')
print(natom)
print(comment)
print(data)
