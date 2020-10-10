#!/usr/bin/python

import pyBY
import pyBY

gconv = pyBY.GConvolution()
gconv = pyBY.GConvolution()
gconv.SetRange(-5, 5)
gconv.SetGridWidth(0.1)
gconv.SetSigma(0.5)
gconv.InitData()

gconv.AddDataPoint(0.0, 1.0)

for n in range(0,gconv.GetGridCount()):
    val = gconv.GetConvolutionDataPoint(n)
    print val
