import csv
import pandas as pd
import glob
import os

path = 'C:\DEV\Python\Python3_Basics\data'
filenames = glob.glob(path + "/*.csv")

df = []

for files in filenames:
    appended_file = df.append(pd.read_csv(files))
    
