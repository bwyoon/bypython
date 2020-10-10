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
    res = re.search(r'NBANDS', line)
    #res = re.search(r'NBANDS=\s*([^ ]+)', line)
    if res:
        print re.sub(r'^.*NBANDS=\s*([^ ]+).*$', r'\1', line).rstrip()
        break

fin.close();

