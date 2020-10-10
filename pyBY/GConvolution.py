
import math

class GConvolution:

    def SetRange(self, min, max):
        self.min = min
        self.max = max

    def SetGridWidth(self, w):
        self.gridwidth = w

    def SetSigma(self, sig):
        self.sigma = sig

    def InitData(self):
        self.gridcount = math.floor((self.max-self.min)/self.gridwidth) 
        self.data = [ 0.0 for k in range(0,self.gridcount) ]

    def GetGridCount(self):
        return self.gridcount

    def AddDataPoint(self, x, y):
        dx = self.gridwidth
        nmax = self.gridcount
        xmin = self.min
        sig  = self.sigma
        v = (x-xmin)/dx
        n0 = int(math.floor(v+0.5))
        dn = int(math.floor(sig/dx*5.0+0.5))
        for n in range(n0-dn, n0+dn+1):
            if (n >= 0) and (n < nmax):
                x1 = xmin+dx*float(n)
                y1 = (x1-x)*(x1-x)/2.0/sig/sig
                y1 = math.exp(-y1)/sig/math.sqrt(2.0*math.pi)
                self.data[n] = self.data[n]+y*y1 

    def GetConvolutionDataPoint(self, n):
        return [self.min+float(n)*self.gridwidth, self.data[n]]

