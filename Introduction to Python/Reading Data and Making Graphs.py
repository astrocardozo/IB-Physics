#Importing the libraries we need
import pandas as pd
print('imported pandas')
import matplotlib.pyplot as plt
print('imported matplotlib.pyplot')

#Reading data from a Google Sheet
database = pd.read_excel("https://docs.google.com/spreadsheets/d/1Z4pTRxwg1ZCAcaN5DNRuL4oLCR1MsD29gHv8toSZBKY/export")
print('finished reading')

#Checkpoint
print(database['time'][1:5])

#Now, replace the print function with each of the following and run 


#Creating a Graph

database.plot('time','position')

plt.show() # This displays the graph cleanly

#You try, create v-t and a-t plots from database below and run