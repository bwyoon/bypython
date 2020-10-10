
import pyBY
import re
import math

class by_xyz:
    def ReadFile(self, moldata, fn):
        fin = open(fn, "r")
        line = fin.readline()
        vars = line.split()
        atomcount = int(vars[0])
        comment = fin.readline()
        moldata.SetComment(comment)
        for n in range(0, atomcount):  
            vars = fin.readline().split()
            moldata.AppendAtom(vars[0], [ float(vars[k]) for k in range(1,4) ])
        res = re.search(r'lattice=\s*"([^"]+)"', comment, re.I)
        if res:
            vars = res.group(1).split()
            lv = [ float(vars[k]) for k in range(0,len(vars)) ]
            moldata.SetLatticeVectors(lv)
            res = re.search(r'CellOrigin=\s*"([^"]+)"', comment, re.I)
            if res:
                vars = res.group(1).split()
                org = [ float(vars[k]) for k in range(0,len(vars)) ]
                moldata.SetCellOrigin(org)
            else :
                moldata.SetCellOrigin([ 0.0, 0.0, 0.0 ])
        else : 
            moldata.AutoLatticeVectors()
        fin.close()
        moldata.SetFileName(fn)
        moldata.SetFileType('xyz')
    
    def WriteFile(self, moldata, fn):
        fout = open(fn, "w")
        str = "%d\n" % moldata.GetAtomCount()
        fout.write(str)
        comment = moldata.GetComment().rstrip()
        res = re.search(r'lattice=\s*"([^"]+)"', comment, re.I)
        if not res:
            lv = moldata.GetLatticeVectors()
            str = ' Lattice="%g %g %g %g %g %g %g %g %g" ' % tuple(lv)
            comment = comment + str
        res = re.search(r'CellOrigin=\s*"([^"]+)"', comment, re.I)
        if not res:
            org = moldata.GetCellOrigin()
            str = ' CellOrigin="%g %g %g"' % tuple(org)
            comment = comment + str
        comment = re.sub(r'^\s+', r'', comment)
        comment = re.sub(r'\s{2,}', r' ', comment)
        fout.write(comment+"\n")
        for n in range(0, moldata.GetAtomCount()):
            elem = moldata.GetAtomElem(n)
            pos  = moldata.GetAtomPos(n)
            str = "%4s %20.15f %20.15f %20.15f\n" % \
                  (elem, pos[0], pos[1], pos[2])
            fout.write(str)
        fout.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
