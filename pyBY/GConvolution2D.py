
import math

class GConvolution2D:

    def SetXRange(self, min, max):
        self.xmin = min
        self.xmax = max

    def SetYRange(self, min, max):
        self.ymin = min
        self.ymax = max

    def SetXGridWidth(self, w):
        self.xgridwidth = w

    def SetYGridWidth(self, w):
        self.ygridwidth = w

    def SetSigma(self, sig):
        self.sigma = sig

    def InitData(self):
        self.xgridcount = math.floor((self.xmax-self.xmin)/self.xgridwidth) 
        self.ygridcount = math.floor((self.xmax-self.xmin)/self.ygridwidth) 
        self.data = [ [0.0 for l in range(0,self.ygridcount)] for k in range(0,self.xgridcount) ]

    def GetXGridCount(self):
        return self.xgridcount

    def GetYGridCount(self):
        return self.ygridcount

    def AddDataPoint(self, x, y, z):
        dx = self.xgridwidth
        dy = self.ygridwidth
        nxmax = self.xgridcount
        nymax = self.ygridcount
        xmin = self.xmin
        ymin = self.ymin
        sig  = self.sigma
        vx = (x-xmin)/dx
        vy = (y-ymin)/dy
        nx0 = int(math.floor(vx+0.5))
        ny0 = int(math.floor(vy+0.5))
        dnx = int(math.floor(sig/dx*5.0+0.5))
        dny = int(math.floor(sig/dy*5.0+0.5))
        for nx in range(nx0-dnx, nx0+dnx+1):
            x1 = xmin+dx*float(nx)
            x2 = (x1-x)*(x1-x)
            if (nx >= 0) and (nx < nxmax):
                for ny in range(ny0-dny, ny0+dny+1):
                    if (ny >= 0) and (ny < nymax):
                        y1 = ymin+dy*float(ny)
                        y2 = (y1-y)*(y1-y)
                        z1 = (x2+y2)/2.0/sig/sig
                        z1 = math.exp(-z1)/sig/sig/(2.0*math.pi)
                        self.data[nx][ny] = self.data[nx][ny]+z*z1 

    def GetConvolutionDataPoint(self, nx, ny):
        return [self.xmin+float(nx)*self.xgridwidth, \
                self.ymin+float(ny)*self.ygridwidth, \
                self.data[nx][ny]]

