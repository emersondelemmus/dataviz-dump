# Create one line plot for each .csv file in the current directory and save it as a png file
import os
import matplotlib.pyplot as plt
from numpy import genfromtxt
from pathlib import Path

input_dir = Path.cwd() / "Plant 3"
print(input_dir)
file_list = list(input_dir.rglob('*.csv'))
print(file_list)

# Loop through all files in the current directory ending with .csv
#for file in os.listdir():
for path in list(input_dir.rglob('*.csv')):

    # Read the csv file into a pandas DataFrame
    csv_data = genfromtxt(fname=file, delimiter=',')

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
    plt.title(file, fontdict=font1)
    plt.xlabel("Occurrence", fontdict= font2)
    plt.ylabel("Temperature", fontdict= font2)


    # Save the plot as a png file
    plt.savefig(file.replace('.csv', '.png'), dpi=600)

    # Close the plot so it doesn't show up in the UI
    plt.close()