
import pyBY

class Mirror:
    def __init__(self):
        self.SetMirrorPosition([0.0, 0.0, 0.0])

    def SetMirrorPosition(self, pos):
        self.mpos = [ pos[k] for k in range(0,3) ]

    def GetMirrorPosition(self):
        return [ self.mpos[k] for k in range(0,3) ]

    def SetMirrorNorm(self, nor):
        nor1 = pyBY.Vector.UnitVector(nor)
        self.mnorm = [ nor1[k] for k in range(0,3) ]

    def GetMirrorNorm(self):
        return [ self.mnorm[k] for k in range(0,3) ]

    def Transform(self, pos):
        pos1 = [ pos[k]-self.mpos[k] for k in range(0,3) ]
        dotp = pyBY.Vector.DotProduct(pos1, self.mnorm)
        dpos = pyBY.Vector.Multiply(self.mnorm, -2.0*dotp)
        return pyBY.Vector.Add(pos, dpos)
