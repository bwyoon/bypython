
import pyBY
import re
import math

class by_poscar:
    def ReadFile(self, moldata, fn):
        fin = open(fn, "r")
        # comment
        comment = fin.readline()
        moldata.SetComment(comment)
        # scale factor
        vars = fin.readline().split()
        sf = float(vars[0].rstrip())
        moldata.SetKeyValue("scalefactor", vars[0].rstrip())
        # lattice vectors
        lv = []
        vars = fin.readline().split()
        for k in range(0,3): lv.append(float(vars[k])*sf)
        vars = fin.readline().split()
        for k in range(0,3): lv.append(float(vars[k])*sf)
        vars = fin.readline().split()
        for k in range(0,3): lv.append(float(vars[k])*sf)
        moldata.SetLatticeVectors(lv)
        moldata.SetCellOrigin([0.0, 0.0, 0.0])
        # elements and element counts
        elem = fin.readline().split()
        vars = fin.readline().split()
        elemcount = [ int(vars[k]) for k in range(0, len(vars)) ]
        # selective and/or cartesian/direct
        line = fin.readline()
        res = re.search(r'^\s*s', line, re.I)
        if res:
            moldata.SetKeyValue('poscarselective', 1)
            line = fin.readline()
        else:
            moldata.SetKeyValue('poscarselective', 0)
        res1 = re.search(r'^\s*c', line, re.I)
        res2 = re.search(r'^\s*k', line, re.I)
        if res1 or res2: moldata.SetKeyValue('poscardirect', 0)
        else:            moldata.SetKeyValue('poscardirect', 1)
        # atom data
        moldata.SetKeyValue('extraox', 1)
        moldata.extra = []
        for n in range(0, len(elem)):
            for m in range(0, elemcount[n]):
                vars = fin.readline().split()  
                p = [float(vars[0]), float(vars[1]), float(vars[2])]
                if moldata.GetKeyValue('poscardirect') == 1:
                    p = moldata.Scaled2Unscaled(p)
                moldata.AppendAtom(elem[n], [p[0], p[1], p[2]])
                if moldata.GetKeyValue('poscarselective') == 1:
                    extra = vars[3]+'   '+vars[4]+'   '+vars[5]
                else:
                    extra = 'T   T   T'
                moldata.extra.append(extra)
        fin.close()
        moldata.SetFileName(fn)
        moldata.SetFileType('poscar')
    
    def WriteFile(self, moldata, fn):
        fout = open(fn, "w")
        # comment
        fout.write(moldata.GetComment()+"\n")
        # scale factor
        sf = 1.0
        if moldata.KeyValueExists('scalefactor'): 
            sf = float(moldata.GetKeyValue('scalefactor'))
        str = "%20.15f" % sf
        fout.write(str+"\n")
        # lattice vectors
        lv = moldata.GetLatticeVectors()
        fout.write("%20.15f %20.15f %20.15f\n" % (lv[0], lv[1], lv[2]))
        fout.write("%20.15f %20.15f %20.15f\n" % (lv[3], lv[4], lv[5]))
        fout.write("%20.15f %20.15f %20.15f\n" % (lv[6], lv[7], lv[8]))
        # elements and element count 
        elemcount = {}
        elemlist = []
        for n in range(0, moldata.GetAtomCount()):
            elem = moldata.GetAtomElem(n)
            if elem in elemcount: 
                elemcount[elem] = elemcount[elem]+1
            else:
                elemlist.append(elem)
                elemcount[elem] = 1
        for n in range(0,len(elemlist)):
            fout.write("%5s" % elemlist[n])
        fout.write("\n")
        for n in range(0,len(elemlist)):
            fout.write("%5d" % elemcount[elemlist[n]])
        fout.write("\n")
        # selective
        fout.write("Selective\n")
        # cartesian or direct
        if moldata.KeyValueExists('poscardirect'):
            if moldata.GetKeyValue('poscardirect') == 1: cox = 0
            else: cox = 1
        else: cox = 1
        if cox == 1: fout.write("Cartesian\n")
        else: fout.write("Direct\n")
        # atom data
        for n in range(0, moldata.GetAtomCount()):
            p = moldata.GetAtomPos(n);
            extra = 'T   T   T'
            if moldata.KeyValueExists('poscarselective'):
                if moldata.GetKeyValue('poscarselective') == 1:
                    extra = moldata.extra[n]
            if cox == 0: p = moldata.Unscaled2Scaled(p)
            fout.write("%21.16f %21.16f %21.16f   %s\n" % (p[0],p[1],p[2],extra))
        fout.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
