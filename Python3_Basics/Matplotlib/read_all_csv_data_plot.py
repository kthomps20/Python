import os
import csv
import pandas as pd
from matplotlib import pyplot as plt


def open_csv(path):
    data = []
    with open(path) as filename:
        data = csv.readline(filename)
        print(data)
    return data

print(open_csv(r'C:\Iosix\Perl_scripts\5735\5735_1H261451_converted.csv'))
open_csv(r'C:\Iosix\Perl_scripts\5735\5735_1H261451_converted.csv')