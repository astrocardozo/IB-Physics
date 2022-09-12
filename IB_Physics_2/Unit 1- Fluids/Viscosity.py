import numpy as np  
import matplotlib.pyplot as plt
from matplotlib import cm 
import pandas as pd
import seaborn as sb
from vpython import *

# tgraph = graph(ytitle="Absolute Pressure [Pa]",xtitle="Depth [m]",fast=False)
# f1 = gcurve(color=color.blue)

 

# F = 1.22E5
# A = 0.1
# dA = 0.01
# P0 = 0
# Alist = []
# Plist = []


# while A<10:
#     rate(50)
#     P = P0 + F/A
#     A = A + dA
#     Alist.append(A)
#     Plist.append(P)
#     f1.plot(A,P)

tgraph2 = graph(ytitle="Absolute Pressure [Pa]",xtitle="Depth [m]",fast=False)
f2 = gcurve(color=color.blue)

P2 = 1.01E5
R = 1
eta = 250E-3
P1 = 1.02E5
l = 1
r = 0
dr = 0.1
Q0 = 1000


while r<10:
    rate(50)
    Q = ((R**2-r**2)*(P1-P2))/(4*eta*l)
    r = r + dr
    f2.plot(r,Q