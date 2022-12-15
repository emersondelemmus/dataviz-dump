# Create one line plot
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
from numpy import genfromtxt

# Read the csv file into a Numpy Array
csv_data = genfromtxt("Plant_3_Cure_Bay_B3030-Bay_1 _Internal Temp_2019.csv", delimiter=',')

# Create a line plot of the data
plt.plot(csv_data, color = 'orange')



# Fonts
font1 = {'family': 'serif',
         'color':'black',
         'size':12}
font2 = {'family': 'serif',
         'color':'black',
         'size':11}

# Add labels to axis
plt.title("Plant_3_Cure_Bay_B3030-Bay_1 _Internal Temp_2020-2021", fontdict=font1)
plt.xlabel("Occurrence", fontdict= font2)
plt.ylabel("Temperature", fontdict= font2)


plt.show()