
import re
import numpy as np

class PROCAR:

    def __init__(self): pass

    def ReadFile(self, fn):
        fin = open(fn, 'r')
        # nkpoints, nbands, nions
        while 1:
            res = re.search(r"^\s*# of k-points:\s*([^ ]+)\s*# of bands:\s*([^ ]+)\s* # of ions:\s*([^ ]+)", fin.readline())
            if res:
                self.nkpoints = int(res.group(1))
                self.nbands   = int(res.group(2))
                self.nions    = int(res.group(3))
                break
        # print self.nkpoints, self.nbands, self.nions
        # array set up
        self.energy = np.empty((2, self.nkpoints, self.nbands))
        self.occ    = np.empty((2, self.nkpoints, self.nbands))
        self.data = {}
        self.data['s']   = np.empty((2, self.nkpoints, self.nbands, self.nions))
        self.data['p']   = np.empty((2, self.nkpoints, self.nbands, self.nions))
        self.data['d']   = np.empty((2, self.nkpoints, self.nbands, self.nions))
        self.data['tot'] = np.empty((2, self.nkpoints, self.nbands, self.nions))
        for k in range(0, self.nkpoints): # loop for kpoints
            for spin in range(0, 2):
                while 1:
                    res = re.search(r"^\s*k-point\s*([0-9]+).+$", \
                                    fin.readline())
                    if res: break
                for b in range(0, self.nbands): # loop for bands
                    while 1:
                        res = re.search(r"\s*band\s*([^ ]+)\s*# energy\s*([^ ]+)\s*# occ\.\s*([^ ]+)", fin.readline())
                        if res:
                             self.energy[spin, k, b] = float(res.group(2))
                             self.occ[spin, k, b] = float(res.group(2))
                             break 
                    while 1:
                        res = re.search(r"\s*ion\s+", fin.readline())
                        if res: break
                    for i in range(0, self.nions): # loop for ions
                        vars = fin.readline().rstrip().split()
                        self.data['s'][spin, k, b, i]   = float(vars[1])
                        self.data['p'][spin, k, b, i]   = float(vars[2])
                        self.data['d'][spin, k, b, i]   = float(vars[3])
                        self.data['tot'][spin, k, b, i] = float(vars[4])
                self.spinox = True if self.occ[0,0,0] < 1.1 else False
                if not self.spinox: break               
        fin.close()
        return self                     
       
    def GetDataKW(self, **kw):
        return self.data[kw['proj']][kw['spin'], kw['kpoint'], \
                         kw['band'], kw['ion']]

    def GetData(self, spin, k, b, ion, proj):
        return self.data[proj][spin, k, b, ion]

