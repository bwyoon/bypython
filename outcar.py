#!/usr/bin/python

import sys
import os.path
import re

def getoutcarfilename():
    if (len(sys.argv) == 1): 
        if (os.path.isfile("converged.OUTCAR")) :
            return "converged.OUTCAR"
        elif (os.path.isfile("optimized.OUTCAR")) :
            return "optimized.OUTCAR"
        else:
            return "OUTCAR"
    else:
        return sys.argv[1];

