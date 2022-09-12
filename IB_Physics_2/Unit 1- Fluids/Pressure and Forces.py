import numpy as np  
import matplotlib.pyplot as plt
from matplotlib import cm 
import pandas as pd
import seaborn as sb
from vpython import *

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

def V(r,P1,P2,eta,l):
    V = ((R**2-r**2)*(P1-P2))/(4*eta*l)
    return V

P2 = 1.01E5
r = np.linspace(0,1,35)
R = 1
eta = 250E-3
eta2 = 500E-3
P1 = 1.02E5
l = 1

V = np.array(V(r,P1,P2,eta,l))

plt.scatter(r,V)

plt.title('Fluid Speed vs Radius of Pipe')
plt.ylabel('Fluid Speed (m/s)')
plt.xlabel('Radius (m)')
plt.show()

def Q(r,P1,P2,eta,l):
    Q = ((np.pi)*(r**2)*(P1-P2))/(8*eta*l)
    return Q

P2 = 1.01E5
r = np.linspace(0,1,35)
eta = 250E-3
P1 = 1.02E5
l = 1

Q = np.array(Q(r,P1,P2,eta,l))
plt.scatter(r,Q)
plt.title('Volume Flow Rate vs Radius of Pipe')
plt.ylabel('Volume Flow Rate (m^3/s)')
plt.xlabel('Radius (m)')
plt.show()


scene = canvas()
scene.background = color.gray(0.8)
scene.forward = vec(2,-2,-2)

P1 = 1.01E5
eta = 250E-3
P2 = 1.02E5
l = 1
x = 0
xmax = 2.5
dx = 0.5
rmax = 0.8
dR = 0.1
dtheta = pi/8
Vscale = 1E-3

tube = extrusion(path=[vec(0,0,0), vec(2,0,0)], shape=shapes.circle(radius=1, thickness=0.2),pos=vec(1,0,0), axis=vec(2,0,0), color=color.white, end_face_color=color.white, opacity = 0.5)
water = cylinder(radius=0.8, thickness=0.2, pos=vec(0,0,0), axis=vec(2,0,0), color=color.blue, end_face_color=color.blue, opacity = 0.7)

arrow_list = []

while x < xmax:
    rate(100)
    theta = 0
    while theta < 2*pi:
        R = 0
        while R < rmax:
            a = arrow(pos=vector(x,R*sin(theta),R*cos(theta)),color=color.orange, radius = 1E-2, axis= vector(V,0,0))
            V = vector(((R**2-rmax**2)*(P1-P2))/(4*eta*l),0,0)
            a.axis = V*Vscale
            arrow_list.append(a)
            R = R+dR
        theta = theta + dtheta
    x=x+dx