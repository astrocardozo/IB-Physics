#Read in our Data
import pandas as pd
import matplotlib.pyplot as plt
from vpython import *

#Import database
database = pd.read_excel("https://docs.google.com/spreadsheets/d/1Z4pTRxwg1ZCAcaN5DNRuL4oLCR1MsD29gHv8toSZBKY/export")

#Plot position data as a function of time and save the figure
database.plot.scatter('time','position')
plt.xlabel('Time[s]')
plt.ylabel('Position[m]')
plt.title("Position vs Time")
plt.savefig("Position_Time_Plot.jpg",dpi=800)

#Plot velocity data as a function of time and save the figure
database.plot.scatter('time','velocity')
plt.xlabel('Time[s]')
plt.ylabel('Velocity[$m/s$]')
plt.title("Velocity vs Time")
plt.savefig("Velocity_Time_Plot.jpg",dpi=800)

#Plot velocity data as a function of time and save the figure
database.plot.scatter('time','acceleration')
plt.xlabel('Time[s]')
plt.ylabel('Acceleration[$m/s^2$]')
plt.title("Acceleration vs Time")
plt.savefig("Acceleration_Time_Plot.jpg",dpi=800)


#Defining a function
def vmodel(vi,a,t):
  v = vi + a * t
  return v

#Here we call the vmodel function
print( vmodel(vi=0,a=0,t=0) )

def xmodel(??):
    x = ??
    return ??

print(xmodel())

#Generating data from our function
database['velocity model'] = vmodel(vi=0.4,a=-1,t=database['time'])

#Fitting our Model to the Data. Carry out the following
plt.figure()
plt.scatter(database['time'],database['velocity'])
plt.plot(database['time'],database['velocity model'])

#Show the plots we just made
plt.show()
