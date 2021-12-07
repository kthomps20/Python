import csv
import os
import pandas as pd
from matplotlib import pyplot as plt


def read_pandas():
    df = pd.read_csv(r'C:\Iosix\Perl_scripts\5735\5735_1H261451_converted.csv', low_memory=False)
    print(df.columns)
    x_axis = df.loc[:, 'Vehicle Speed (kph)']
    y_axis = df.loc[:, 'Engine Speed (rpm)']
    z_axis = df.loc[:, 'Time (s)']

    plt.xlabel('Engine Speed')
    plt.ylabel('Vehicle Speed')
    plt.plot(z_axis, x_axis, color='red', linestyle='--')

    plt.plot(z_axis, y_axis, color='green', linestyle='--')

    plot = plt.show()
    return plot


def save_fig():
    ord_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
    power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
    years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

    plt.close('all')

    plt.figure(figsize=(7, 3))
    plt.plot(years, power_generated)
    plt.savefig('power_generated.png')

    plot = plt.show()
    return plot

plt.show()
save_fig()
