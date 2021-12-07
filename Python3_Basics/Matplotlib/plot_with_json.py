import csv
import json
import pandas as pd
from datetime import datetime
import glob
import os



src = "C:\DEV\Python\Python3_Basics\data"
date = datetime.now()
data = []

files = glob.glob('data/*', recursive=True)
# Change the glob if you want to only look through files with specific names
for aws_files in files:
    print(files)
    #with open(files, 'w') as jsonfile:




#csv_filename = f'{str(date)}.csv'
#with open(csv_filename, "w", newline="") as f:
 #   writer = csv.writer(f)
    #writer.writerows(data)

