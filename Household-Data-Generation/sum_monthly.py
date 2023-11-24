import pandas as pd

import csv
import os

hours = 24;

file_path = './sum.csv'

print(file_path)

df = pd.read_csv(file_path, sep=',')

print(df.columns)


sum_column=df['SUM'];

sum_column_groups = (sum_column.index // hours) 
sums = sum_column.groupby(sum_column_groups).sum()


sums_df = pd.DataFrame({'Date': df['Date'][0::hours].reset_index(drop=True), 'Hour': df['Hour'][0::hours].reset_index(drop=True)})

sums_df['SUMS']=sums


sums_df.to_csv('daily_consumption.csv', sep=',')

quit()