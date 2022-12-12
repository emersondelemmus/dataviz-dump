# Create one scatter plot for each .csv file in the current directory and save it as a png file
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# Loop through all files in the current directory ending with .csv
for file in os.listdir():
    if file.endswith(".csv"):
        # Read the csv file into a pandas DataFrame
        df = pd.read_csv(file)

        # Create a scatter plot of the data
        plt.scatter(df["Date"], df["Temp"])

        # Save the plot as a png file
        plt.savefig(file.replace('.csv', '.png'))

        # Close the plot so it doesn't show up in the UI
        plt.close()