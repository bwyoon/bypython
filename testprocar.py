#!/usr/bin/python

import pyBYVASP
import pyBYVASP
import numpy as np

procar = pyBYVASP.PROCAR().ReadFile('PROCAR')
procar = pyBYVASP.PROCAR().ReadFile('PROCAR')

print procar.GetDataKW(spin = 0, kpoint = 0, band = 0, ion = 0, proj = 's')
print procar.GetDataKW(spin = 1, kpoint = 0, band = 20, ion = 2, proj = 'd')
print procar.data['s'][0,0,0,0]
print procar.data['d'][1,0,20,2]

