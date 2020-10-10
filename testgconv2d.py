#!/usr/bin/python

import pyBY
import pyBY

gconv = pyBY.GConvolution2D()
gconv = pyBY.GConvolution2D()
gconv.SetXRange(-5, 5)
gconv.SetYRange(-5, 5)
gconv.SetXGridWidth(0.1)
gconv.SetYGridWidth(0.1)
gconv.SetSigma(0.5)
gconv.InitData()

gconv.AddDataPoint(0.0, 0.0, 1.0)

ny = int(gconv.GetYGridCount()/2)
for nx in range(0,gconv.GetXGridCount()):
    val = gconv.GetConvolutionDataPoint(nx, ny)
    print val
