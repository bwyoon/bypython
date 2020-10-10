
import math
import pyBY

class Rotator:

    def __init__ (self):
        self.center = [0.0, 0.0, 0.0]
        self.InitMatrix()

    def InitMatrix(self):
        self.mat = [ [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0] ] 

    def SetCenter(self, pos):
        self.center = [ pos[k] for k in range(0,3) ]

    def GetCenter(self):
        return [ self.center[k] for k in range(0,3) ]

    def SetMatrix(self, m):
        self.mat = [ [m[k][0], m[k][1], m[k][2]] for k in range(0,3) ]

    def GetMatrix(self):
        m = self.mat
        return [ [m[k][0], m[k][1], m[k][2]] for k in range(0,3) ]

    def MultiplyMatrix(self, m1):
        m0 = self.GetMatrix()
        m3 = [ [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0] ]
        for i in range(0,3):
            for j in range(0,3):
                for k in range(0,3):
                    m3[i][j] += m1[i][k]*m0[k][j]
        self.SetMatrix(m3)

    def SetAxis(self, axis):
        a = pyBY.Vector.UnitVector(axis)
        self.axis = [ a[k] for k in range(0,3) ]

    def GetAxis(self):
        return [ self.axis[k] for k in range(0,3) ]

    def Rotate(self, angle, radox = 0):
        if radox == 0:
            angle = angle*math.pi/180.0   
        ux = self.axis[0]
        uy = self.axis[1]
        uz = self.axis[2]
        cos_v = math.cos(angle)
        sin_v = math.sin(angle)
        rm = [ [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0] ]
        rm[0][0] = cos_v+ux*ux*(1.0-cos_v);
        rm[0][1] = ux*uy*(1.0-cos_v)-uz*sin_v;
        rm[0][2] = ux*uz*(1.0-cos_v)+uy*sin_v;
        rm[1][0] = uy*ux*(1.0-cos_v)+uz*sin_v;
        rm[1][1] = cos_v+uy*uy*(1.0-cos_v);
        rm[1][2] = uy*uz*(1.0-cos_v)-ux*sin_v;
        rm[2][0] = uz*ux*(1.0-cos_v)-uy*sin_v;
        rm[2][1] = uz*uy*(1.0-cos_v)+ux*sin_v;
        rm[2][2] = cos_v+uz*uz*(1.0-cos_v);
        self.MultiplyMatrix(rm)

    def RotateX(self, angle, radox = 0):
        self.SetAxis([1.0, 0.0, 0.0])
        Rotate(angle, radox)
        
    def RotateY(self, angle, radox = 0):
        self.SetAxis([0.0, 1.0, 0.0])
        Rotate(angle, radox)

    def RotateZ(self, angle, radox = 0):
        self.SetAxis([0.0, 0.0, 1.0])
        Rotate(angle, radox)
        
    def Transform(self, pos):
        pos1 = [ pos[k]-self.center[k] for k in range(0,3) ]
        pos2 = [0.0, 0.0, 0.0]
        for k in range(0,3):
            for l in range(0,3):
                pos2[k] = pos2[k]+self.mat[k][l]*pos1[l]
        return [ pos2[k]+self.center[k] for k in range(0,3) ]

