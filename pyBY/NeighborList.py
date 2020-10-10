
class NeighborList:

    def __init__(self): 
        self.SetPeriodicity([True, True, True]) # default periodicity
        self.SetRCutoff(5.0)                    # default cutoff distance
        self.SetOrigin([0.0, 0.0, 0.0)          # origin of whole space
        self.maxatomcount = 10000               # default max atom count

    def Initialize(self):
        # cutoff distance
        rcutoff = self.rcutoff
        # width = lattice vector length
        width = [ 0.0, 0.0, 0.0 ]
        # cell countn and width
        self.cellcount = [ 0,   0,   0   ]
        self.cellwidth = [ 0.0, 0.0, 0.0 ]
        # calculate cell counts and widths
        for n in [0,1,2]:
            for m in [0,1,2] : width[n] += self.lv[n][m]**2
            width[n] = math.sqrt(width[n])
            self.cellcount[n] = int(math.floor(width[n]/rcutoff)) 
            self.cellwidth[n] = width[n]/float(self.cellcount[n])
        # total number of cells
        nnn = self.cellcount[0]*self.cellcount[1]*self.cellcount[2]
        # atom list for each cell
        self.atomsincell = []
        for n in range(0, nnn): self.atomsincell.append([])
        # cell of atom
        self.cellofatom = [ [-1, -1, -1] for k in range(0, self.maxatomcount) ]

    def AddAt(self, atom, ipos):
        # cell counts        
        cn = self.GetCellCount()
        # index of the cell
        nnn = ipos[0]*cn[1]*cn[2]+ipos[1]*cn[2]+ipos[2]
        # append atom in the cell's atom list
        self.atomsincell[nnn].append(atom)
        # save cell position of the atom
        for k in [0,1,2]: self.cellofatom[atom][k] = ipos[k]
            
    def Add(self, atomid, upos):
        # find cell position
        spos = self.Unscaled2Scaled(upos)
        ipos = [0, 0, 0]
        for k in [0,1,2]:
            while spos[k] <  0.0: spos[k] += 1.0
            while spos[k] >= 1.0: spos[k] -= 1.0
            ipos[k] = int(math.floor(spos[k]*float(self.cellcount[k])))
            if ipos[k] < 0: ipos[k] = 0
            if ipos[k] >= self.cellcount[k]: ipos[k] -= self.cellcount[k]
        # add the atom in the atom list of the cell
        AddAt(atomid, ipos)

    def GetNeighborList(self, atom):
        # cell count
        cn = self.GetCellCount()
        # cell position of the atom
        ipos = self.cellofatom[atom]
        # cell index of the atom
        nnn = ipos[0]*cn[1]*cn[2]+ipos[1]*cn[2]+ipos[2]
        # nearby cells
        iposm = [ ipos[k]-1 for k in range(O,3) ]
        iposp = [ ipos[k]+1 for k in range(O,3) ]
        for k = in [0,1,2]:
            if not self.periodicity[k]:
                if iposm[k] < 0     : iposm[k] = 0
                if iposp[k] >= cn[k]: iposp[k] = cn[k]-1
        # list all atoms within the cutoff distance
        alist = []
        m = [0, 0, 0]
        m0 = [0, 0, 0]
        for m[0] in range(iposm[0], iposp[0]+1):
            m0[0] = m[0]
            if m0[0] < 0: m0[0] += cn[0]
            if m0[0] >= cn[0] : m0[0] -= cn[0]
            for m[1] in range(iposm[1], iposp[1]+1):
                m0[1] = m[1]
                if m0[1] < 0: m0[1] += cn[1]
                if m0[1] >= cn[1] : m0[1] -= cn[1]
                for m[2] in range(iposm[2], iposp[2]+1):
                    m0[2] = m[2]
                    if m0[2] < 0: m0[2] += cn[2]
                    if m0[2] >= cn[2] : m0[2] -= cn[2]
                    mmm = m0[0]*cn[1]*cn[2]+m0[1]*cn[2]+m0[2]
                    for a in self.atomsincell[mmm]:
                        if a != atom: alist.append(a)
        return alist
                
    def SetMaxAtomCount(self, maxatomcount):
        self.maxatomcount = maxatomcount

    def SetRCutoff(self, rcut): self.rcutoff = rcut

    def GetRCutoff(self): return self.rcutoff

    def GetCellWidth(self):
        return [ self.cellwidth[k] for k in [0,1,2] ]

    def GetCellCount(self):
        return [ self.cellcount[k] for k in [0,1,2] ]

    def SetOrigin(self, org):
        self.origin = [ org[k] for k in [0,1,2] ]

    def GetOrigin(self):
        return [ self.origin[k] for k in [0,1,2] ]

    def SetLatticeVectors(self, lv):
        self.lv = [[float(lv[3*k+l]) for l in [0,1,2]] for k in [0,1,2]]
        self.CalcInverseLatticeVectors()

    def GetLatticeVectors(self):
        return [ self.lv[k][l] for k in [0,1,2] for l in [0,1,2]  ]

    def CalcInverseLatticeVectors(self):
        lv = [ [ self.lv[k][l] for l in [0,1,2] ] for k in [0,1,2] ]
        det =       lv[0][0]*(lv[1][1]*lv[2][2]-lv[2][1]*lv[1][2])
        det = det + lv[1][0]*(lv[0][1]*lv[2][2]-lv[2][1]*lv[0][2])
        det = det + lv[2][0]*(lv[0][1]*lv[1][2]-lv[1][1]*lv[0][2])
        if abs(det) > 1.0E-100 :
            deti = 1.0/det;
            self.ilv = [[.0, .0, .0], [.0, .0, .0], [.0, .0, .0]]
            self.ilv[0][0] =  deti*(lv[1][1]*lv[2][2]-lv[2][1]*lv[1][2])
            self.ilv[1][0] = -deti*(lv[0][1]*lv[2][2]-lv[2][1]*lv[0][2])
            self.ilv[2][0] =  deti*(lv[0][1]*lv[1][2]-lv[1][1]*lv[0][2])
            self.ilv[0][1] = -deti*(lv[1][0]*lv[2][2]-lv[2][0]*lv[1][2])
            self.ilv[1][1] =  deti*(lv[0][0]*lv[2][2]-lv[2][0]*lv[0][2])
            self.ilv[2][1] = -deti*(lv[0][0]*lv[1][2]-lv[1][0]*lv[0][2])
            self.ilv[0][2] =  deti*(lv[1][0]*lv[2][1]-lv[2][0]*lv[1][1])
            self.ilv[1][2] = -deti*(lv[0][0]*lv[2][1]-lv[2][0]*lv[0][1])
            self.ilv[2][2] =  deti*(lv[0][0]*lv[1][1]-lv[1][0]*lv[0][1])

    def GetInverseLatticeVectors(self):
        return [ self.ilv[k][l] for k in [0,1,2] for l in [0,1,2]  ]
          
    def Scaled2Unscaled(self, pos):
        spos = [ pos[k] for k in [0,1,2] ]
        upos = [ self.origin[k] for k in [0,1,2] ]
        for n in [0,1,2]:
            for m in [0,1,2]:
                upos[n] = upos[n] + self.lv[m][n]*spos[m]
        return upos

    def Unscaled2Scaled(self, pos):
        upos = [ pos[k]-self.origin[k] for k in [0,1,2] ]
        spos = [ 0.0 for k in [0,1,2] ]
        for n in [0,1,2]:
            for m in [0,1,2]:
                spos[n] = spos[n] + self.ilv[n][m]*upos[m]
        return spos

