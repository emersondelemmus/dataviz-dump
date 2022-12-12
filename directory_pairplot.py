# Create one seaborn pairplot for each .csv file in the current directory and save it as a png file with DPI=300
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loop through all files in the current directory ending with .csv
for file in os.listdir():
    if file.endswith(".csv"):
        # Read the csv file into a pandas DataFrame
        df = pd.read_csv(file)

        # Create a scatter plot of the data
        sns.pairplot(df, diag_kind='kde', diag_kws={'color':'green'}, kind= 'reg', plot_kws={'line_kws':{'color':'red'}})

        # Save the plot as a png file
        plt.savefig(file.replace('.csv', '.png'), dpi=300)

        # Close the plot so it doesn't show up in the UI
        plt.close()