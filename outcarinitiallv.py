#!/usr/bin/python

import sys
import os.path
import re
import outcar;

fn = outcar.getoutcarfilename()

fin = open(fn, "r")

while 1:
    line = fin.readline()
    if not line: 
        break
    res = re.search(r'direct lattice vectors', line)
    if res:
        lva = fin.readline().split()
        lvb= fin.readline().split()
        lvc= fin.readline().split()
        print lva[0], lva[1], lva[2], lvb[0], lvb[1], lvb[2], \
              lvc[0], lvc[1], lvc[2];
        break

fin.close();



