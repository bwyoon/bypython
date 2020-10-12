
import pyBY
#import pyBYMolDataFile
from pyBYMolDataFile import *
import re
import math

class MolData:
       
    def __init__(self):
        self.Initialize()

    def Initialize(self):
        self.atomcount  = 0
        self.keyvalue = {}
        self.keyvalue['filename'] = ''
        self.keyvalue['filetype'] = ''
        self.keyvalue['comment']  = ''
        self.keyvalue['extraexists'] = 0
        self.elem = []
        self.pos  = []

    def SetKeyValue(self, key, value):
        self.keyvalue[key] = value

    def GetKeyValue(self, key):
        return self.keyvalue[key]

    def SetFileName(self, fn):
        self.keyvalue['filename'] = fn;

    def KeyValueExists(self, key):
        if key in self.keyvalue: return True
        else: return False

    def GetFileName(self):
        return self.keyvalue['filename']

    def SetFileType(self, fn):
        self.keyvalue['filetype'] = fn;

    def GetFileType(self):
        return self.keyvalue['filetype']

    def SetComment(self, comment):
        self.keyvalue['comment'] = comment
        self.keyvalue['comment'] = self.keyvalue['comment'].rstrip()

    def GetComment(self):
        return self.keyvalue['comment']

    def SetAtomCount(self, atomcount):
        self.atomcount = atomcount

    def GetAtomCount(self):
        return self.atomcount

    def SetAtom(self, n, elem, pos):
        self.elem[n] = elem.rstrip()
        self.pos[n]  = [ pos[k] for k in range(3) ]

    def GetAtom(self, n):
        return self.elem[n], [ self.pos[n][k] for k in range(3) ]

    def SetAtomElem(self, n, elem):
        self.elem[n] = elem.rstrip()

    def GetAtomElem(self, n):
        return self.elem[n]

    def SetAtomElemList(self, elems):
        count = self.GetAtomCount()
        for n in range(count):
            self.elem[n] = elems[n]

    def GetAtomElemList(self):
        return self.elem

    def SetAtomPos(self, n, pos):
        self.pos[n] = [ pos[k] for k in range(3) ]

    def GetAtomPos(self, n):
        return [ self.pos[n][k] for k in range(3) ]

    def SetAtomPosList(self, poss):
        count = self.GetAtomCount()
        for n in range(count):
            self.pos[n] = [ poss[n][k] for k in range(3) ]

    def GetAtomPosList(self):
        return self.pos

    def AppendAtom(self, elem, pos):
        self.elem.append(elem.rstrip())
        self.pos.append( [ pos[k] for k in range(3) ] )
        self.atomcount = self.atomcount+1

    def DeleteAtomAt(self, n):
        del self.elem[n]
        del self.pos[n]
        self.atomcount = self.atomcount-1

    def SetCellOrigin(self, org):
        self.cellorigin = [ org[k] for k in range(3) ]

    def GetCellOrigin(self):
        return [ self.cellorigin[k] for k in range(3) ]

    def SetLatticeVectors(self, lv):
        self.lv = [ [ float(lv[k*3+l]) for l in range(3) ] for k in range(3) ]
        self.CalcInverseLatticeVectors()

    def GetLatticeVectors(self):
        return [ self.lv[k][l] for k in range(3) for l in range(3) ]

    def CalcInverseLatticeVectors(self):
        lv = [ [ self.lv[k][l] for l in range(3) ] for k in range(3) ]
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
        return [ self.ilv[k][l] for k in range(3) for l in range(3) ]

    def AutoLatticeVectors(self, margin = 5.0):
        min = [ +1.0E+300 for k in range(3) ]
        max = [ -1.0E+300 for k in range(3) ]
        mag = margin
        for m in range(3):
            for n in range(0,self.GetAtomCount()):
                if self.pos[n][m] < min[m] : min[m] = self.pos[n][m]
                if self.pos[n][m] > max[m] : max[m] = self.pos[n][m]
            min[m] = min[m]-mag
            max[m] = max[m]+mag
            if min[m] < 0.0 : 
                min[m] = math.floor(min[m])
            else :
                min[m] = math.ceil(min[m])
            if max[m] < 0.0 :
                max[m] = math.floor(max[m])
            else :
                max[m] = math.ceil(max[m])
        self.SetCellOrigin(min)
        self.SetLatticeVectors( [ max[0]-min[0], 0.0, 0.0,\
                                 0.0, max[1]-min[1], 0.0,\
                                 0.0, 0.0, max[2]-min[2] ] )
        self.CalcInverseLatticeVectors()

    def Scaled2Unscaled(self, pos):
        spos = [ pos[k] for k in range(3) ]
        upos = [ self.cellorigin[k] for k in range(3) ]
        for n in range(3):
            for m in range(3):
                upos[n] = upos[n] + self.lv[m][n]*spos[m]
        return upos

    def Unscaled2Scaled(self, pos):
        upos = [ pos[k]-self.cellorigin[k] for k in range(3) ] 
        spos = [ 0.0 for k in range(3) ]
        for n in range(3):
            for m in range(3):
                spos[n] = spos[n] + self.ilv[n][m]*upos[m]
        return spos

    def CalcDistance(self, n1, n2):
        spos1 = self.Unscaled2Scaled(self.GetAtomPos(n1))
        spos2 = self.Unscaled2Scaled(self.GetAtomPos(n2))
        for m in range(3):
            if (spos2[m]-spos1[m]) >= 0.5 : spos2[m] = spos2[m]-1.0
            if (spos2[m]-spos1[m]) < -0.5 : spos2[m] = spos2[m]+1.0
        upos1 = self.Scaled2Unscaled(spos1)
        upos2 = self.Scaled2Unscaled(spos2)
        return pyBY.Vector.Distance(upos1, upos2)

    def CalcUnitDirection(self, n1, n2):
        spos1 = self.Unscaled2Scaled(self.GetAtomPos(n1))
        spos2 = self.Unscaled2Scaled(self.GetAtomPos(n2))
        for m in range(3):
            if (spos2[m]-spos1[m]) >= 0.5 : spos2[m] = spos2[m]-1.0
            if (spos2[m]-spos1[m]) < -0.5 : spos2[m] = spos2[m]+1.0
        upos1 = self.Scaled2Unscaled(spos1)
        upos2 = self.Scaled2Unscaled(spos2)
        return pyBY.Vector.UnitVector(BY.Vector.Difference(upos1, upos2))

    def CalcAngle(self, n1, n0, n2):
        dir1 = self.CalcUnitDirection(n0, n1)
        dir2 = self.CalcUnitDirection(n0, n2)
        return math.acos(BY.Vector.DotProduct(dir1, dir2))

    def FindMolecule(self, startind, melem, compind, compdist):
        mind = []
        atomcount = self.GetAtomCount()
        if startind >= atomcount: 
            return mind
        for n in range(startind, atomcount):
            if self.GetAtomElem(n) == melem[0]: 
                mind.append(n)
                break
        if len(mind) == 0:
            return mind
        ox = [0]*atomcount
        for n in range(1, len(melem)):
            for m in range(0, atomcount):
                if (ox[m] == 0) and (self.GetAtomElem(m) == melem[n]):
                    d = self.CalcDistance(m, mind[compind[n]])
                    if d < compdist[n]: 
                        mind.append(m)
                        ox[m] = 1 
                        break
            if ox[m] == 0: 
                break
        if len(mind) == len(melem):
            return mind
        else:
            return []
        
    def FindMoleculeWithHs(self, startind, melem, compind, compdist):
        mind = []
        atomcount = self.GetAtomCount()
        if startind >= atomcount:
            return mind
        for n in range(startind, atomcount):
            if self.GetAtomElem(n) == melem[0]: 
                mind.append(n)
                break
        if len(mind) == 0: 
            return mind
        ox = [0]*atomcount
        for n in range(1, len(melem)):
            for m in range(0, atomcount):
                if (ox[m] == 0) and (self.GetAtomElem(m) == melem[n]):
                    d = self.CalcDistance(m, mind[compind[n]])
                    if d < compdist[n]:
                        mind.append(m)
                        ox[m] = 1
                        break
            if ox[m] == 0: break
        if len(mind) < len(melem):
            return []
        count = len(mind)
        for m in range(0, atomcount):
            if (ox[m] == 0) and (self.GetAtomElem(m) == "H"):
                for n in range(0, count):
                    d = self.CalcDistance(m, mind[n])
                    if (d < 1.3): 
                        mind.append(m)
                        ox[m] = 1
                        break
        return mind
        
    def SetVDOrigin(self, org):
        self.vdorigin = [ org[k] for k in range(3) ]

    def GetVDOrigin(self):
        return [ self.vdorigin[k] for k in range(3) ]

    def SetVDGridCount(self, count):
        self.vdgridcount = [ count[k] for k in range(3) ]
        nnn = count[0]*count[1]*count[2]
        self.vd = [ 0.0 for k in range(0, nnn) ]

    def GetVDGridCount(self):
        return [ self.vdgridcount[k] for k in range(3) ]

    def SetVolumetricData(self, ix, iy, iz, v):
        self.vd[ix*self.vdgridcount[1]*self.vdgridcount[2] \
                +iy*self.vdgridcount[2]+iz] = v

    def GetVolumetricData(self, ix, iy, iz):
        return self.vd[ix*self.vdgridcount[1]*self.vdgridcount[2] \
                +iy*self.vdgridcount[2]+iz] 


    def ReadFile(self, fn, ftype = ""):
        if ftype == "":
            if fn == 'POSCAR':
                by_poscar().ReadFile(self, fn)
            elif fn == 'CONTCAR':
                by_poscar().ReadFile(self, fn)
            elif fn == 'CHGCAR':
                by_chgcar().ReadFile(self, fn)
            else:
                res = re.search(r".([a-zA-Z0-9]+)$", fn, re.I)
                if res:
                    ext = res.group(1).lower()
                    getattr(globals()["by_"+ext](), 'ReadFile')(self, fn)
        else:
            ext = ftype.lower()
            getattr(globals()["by_"+ext](), 'ReadFile')(self, fn)
        return self

    def WriteFile(self, fn, ftype = ""):
        if ftype == "":
            if fn == 'POSCAR':
                by_poscar().WriteFile(self, fn)
            elif fn == 'CONTCAR':
                by_poscar().WriteFile(self, fn)
            elif fn == 'CHGCAR':
                by_chgcar().WriteFile(self, fn)
            else:
                res = re.search(r".([a-zA-Z0-9]+)$", fn, re.I)
                if res:
                    ext = res.group(1).lower()
                    getattr(globals()["by_"+ext](), 'WriteFile')(self, fn)
        else:
            ext = ftype.lower()
            getattr(globals()["by_"+ext](), 'WriteFile')(self, fn)



