#!/usr/bin/python

import sys
import os.path
import re
import outcar;

fn = outcar.getoutcarfilename()

cmd = 'outcarhomo.py '+fn;
homo = int(os.popen(cmd).read().rstrip())
print "HOMO", homo

cmd = 'outcarbandcount.py '+fn;
nband = int(os.popen(cmd).read().rstrip())

fin = open(fn, "r")

lines = []
n = 0
while 1:
    line = fin.readline()
    if not line: 
        break
    res = re.search(r'band No.\s*band energies', line)
    if res:
        res = re.search(r'band No.\s*band energies', fin.readline())
        if res: n = 0
        while 1:
            line = fin.readline();
            res = re.search(r'------------', line)
            if res: break
            lines.append(line)  
            n = n+1
fin.close();

for n in range (0, nband):
    lines[n] = re.sub(r'\s{2,}', r' ', lines[n])
    lines[n] = re.sub(r'^\s+', r'', lines[n])
    if len(lines[n]) >= 3:
        print lines[n].rstrip()

