import pandas as pd

import csv
import os

minutes = 60;

file_name = "/SumProfiles.Electricity.csv"
dir_name = "/Users/user/Desktop/_last/LoadGeneratorData/"

dirs = sorted(os.listdir(dir_name))

isFirst = True;
for i in dirs:
    File_Path = dir_name + i + file_name
    print(File_Path)

    df = pd.read_csv(File_Path,sep = ';')

    df[['date', 'time']] = df['Time'].str.split(expand=True)

    df[['hour', 'minutes']] = df['time'].str.split(':',expand=True)

    if(isFirst):
        sums_df = pd.DataFrame({'Date': df['date'][0::minutes].reset_index(drop=True), 'Hour': df['hour'][0::minutes].reset_index(drop=True)})
        isFirst=False;

    sum_column=df['Sum [kWh]'];

    sum_column_groups = (sum_column.index // minutes) 
    sums = sum_column.groupby(sum_column_groups).sum()

    sums_df[i]=sums;


sums_df.to_csv('sum.csv', sep=';')
