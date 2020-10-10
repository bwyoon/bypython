#!/usr/bin/python

import sys
import os.path
import re
import outcar;

fn = outcar.getoutcarfilename()

cmd = 'outcarhomo.py '+fn;
homo = os.popen(cmd).read().rstrip()

fin = open(fn, "r")

while 1:
    line = fin.readline()
    if not line: 
        break
    pattern = r"^\s*"+homo;
    res = re.search(pattern, line)
    if res:
         heline = line
fin.close();

he = heline.split()
print he[1]

