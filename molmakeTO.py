#!/usr/bin/python
#####################################
##   original author: Bokwon Yoon   #
#####################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 5:
    eprint("USAGE: molmakeTO.py N lparam elem xyzfile")
    exit(1)

N = int(sys.arv[1]);
lp = float(sys.argv[2]);
elem = sys.argv[3];

mol = pyBY.MolData();
mol = pyBY.MolData();
rot = pyBY.Rotator();
rot = pyBY.Rotator();
rot.SetCenter([0.0, 0.0, 0.0]);
rot.SetAxis(


