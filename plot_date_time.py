
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
from numpy import genfromtxt


# Read the csv file into a Numpy Array
csv_data = pd.read_csv("Plant_3_Cure_Bay_B3030-Bay_1 _Internal Temp_2019.csv", parse_dates=['DATE'])

csv_data['DATE'] = pd.to_datetime(csv_data['DATE'])

csv_data.plot(x='DATE', y='TEMP')