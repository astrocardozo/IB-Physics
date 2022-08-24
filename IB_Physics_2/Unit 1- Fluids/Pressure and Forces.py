import numpy as np  
import matplotlib.pyplot as plt
from matplotlib import cm 
import pandas as pd
import seaborn as sb

def Pressure(F,A):
    P = F/A
    return P   

F = 1.22E5
A = np.linspace(0,100,25)
y = Pressure(F,A)

plt.scatter(A,y)
plt.xlabel('Cross Sectional Area (m^2)')
plt.ylabel('Pressure (Pa)')
plt.title('Pressure vs Cross Sectional Area')
plt.show()

# Linearized function 

F = 1.22E5
A = np.linspace(0,100,10)
y = Pressure(F,A)

plt.scatter(1/A,y)
plt.xlabel('1/Cross Sectional Area (m^-2)')
plt.ylabel('Pressure (Pa)')
plt.title('Linearized Pressure vs Cross Sectional Area')
plt.show()

def fluid_P(rho,g,h):
    P = rho*g*h
    return P


h = np.linspace(0,100,10) #displacement is negative 
rho = 1E3
g = 9.81
y = fluid_P(rho,g,h)

plt.scatter(h,y)
plt.xlabel('Depth (m)')
plt.ylabel('Pressure (Pa)')
plt.title('Pressure vs Depth in Water')
plt.show()

rho = 1E3
g = 9.81
h = 0
dh = 5     #set up the delta h incraments
P1 = 1.01E5
P = 0
PList = []  #create an empty list for pressure
hList= []   #create an empty list for depth

while h < 100:         #loop through h = 0 to h = -100
    dP = P1 + rho*g*dh
    P = P + dP
    h = h + dh
    PList.append(P)     #Adding each new value of P to the list 
    hList.append(h)     #Adding each new value of h to the list 
    
plt.scatter(hList,PList)
plt.xlabel('Depth (m)')
plt.ylabel('Pressure (Pa)')
plt.title('Pressure vs Depth in Water')
plt.show()

def Pressure(P1,rho,g,h):
    P = P1 + rho*g*h
    return P

h = np.linspace(0,100,100)
x = np.linspace(0,100,100)
x,h = np.meshgrid(x,h)
P1 = 1.01E5
rho = 1E3
g = 9.81
z = Pressure(P1,rho,g,h)
ax = sb.heatmap(z)
plt.xlabel('Range (m)')
plt.ylabel('Depth (m) ')
plt.title('Pressure vs Depth of Water')
plt.show()

x = np.linspace(0,100,100)
x,h = np.meshgrid(x,hList)
rho2 = 1.35E3
z = Pressure(P1,rho2,g,h)
ax = sb.heatmap(z)
plt.xlabel('Range (m)')
plt.ylabel('Depth (m) ')
plt.title('Pressure vs Depth of Mercury')
plt.show()