#!/usr/bin/python
# Bokwon Yoon

lines_up = open('up.ACF.dat', 'r').readlines()
lines_dn = open('dn.ACF.dat', 'r').readlines()

natoms = len(lines_up)-6
for n in range(natoms):
    v_up = lines_up[n+2].split()
    v_dn = lines_dn[n+2].split()
    #print(v_up)
    #print(v_dn)
    print( '%d %f' %(n+1, float(v_up[4])-float(v_dn[4])) )
    #print( '{} {}'.format(n+1, float(v_up[4])-float(v_dn[4])) )




