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
    res = re.search(r'^.+Iteration\s+([^(]+).+$', line)
    if res:
        iter = res.group(1);
    res = re.search(r'entropy=', line)
    if res:
        line = re.sub(r'\s{2,}', ' ', line)
        #line = re.sub(r'\n', '', line)
        line = line.rstrip()
        print iter, ":", line

fin.close();

