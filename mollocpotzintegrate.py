#!/usr/bin/python
#########################################
#     original author : Bokwon Yoon     #
#########################################

import sys
import pyBY
import pyBY

if len(sys.argv) < 3:
    sys.stderr.write("USAGE: mollocpotzintegrate LOCPOT outfile [Ef]\n")
    exit(1)

ef = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0

mol = pyBY.MolData().ReadFile(sys.argv[1], "chgcar")
lv  = mol.GetLatticeVectors()
gn  = mol.GetVDGridCount()
org = mol.GetVDOrigin()
gw  = [ lv[k*3+k]/float(gn[k]) for k in range(3)  ] 

za = [ float(k)*gw[2] for k in range(gn[2]) ]
va = [ 0.0 for k in range(gn[2]) ]

for iz in range(gn[2]):
    for ix in range(gn[0]):
        for iy in range(gn[1]):
            va[iz] += mol.GetVolumetricData(ix, iy, iz)
    va[iz] = va[iz]/(float(gn[0])*float(gn[1]))-ef

vmax, zmax = -1.0e-300, -1.0e-300
fout = open(sys.argv[2], "w")
fout.write("z          W\n");
for iz in range(gn[2]):
    fout.write("%10.5f %10.5f\n" % (za[iz], va[iz]))
    if vmax < va[iz]: vmax = va[iz]; zmax = za[iz];
fout.close()

print("maximum %.5f eV at z = %.5f" % (vmax, zmax))

