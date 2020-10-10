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
    res = re.search(r'E-fermi', line)
    if res:
        ef = line

fin.close();

print re.sub(r'^.*E-fermi\s*:\s*([^ ]+).*$', r'\1', ef).rstrip()

