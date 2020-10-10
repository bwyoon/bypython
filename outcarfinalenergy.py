#!/usr/bin/python

import sys
import os.path
import re
import outcar;

fn = outcar.getoutcarfilename()

fin = open(fn, "r")

found = ""
while 1:
    line = fin.readline()
    if not line: 
        break
    res = re.search(r'entropy=', line)
    if res:
        found = line

fin.close();

print (re.sub(r'^.*entropy=\s*([^ ]+).+$', r'\1', found)).rstrip()

