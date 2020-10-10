#!/usr/bin/python

import sys
import os.path
import re
import outcar;

fn = outcar.getoutcarfilename()

cmd = 'outcarhomo.py '+fn;
lumo = str(int(os.popen(cmd).read().rstrip())+1)

fin = open(fn, "r")

while 1:
    line = fin.readline()
    if not line: 
        break
    pattern = r"^\s*"+lumo;
    res = re.search(pattern, line)
    if res:
         leline = line
fin.close();

le = leline.split()
print le[1]

