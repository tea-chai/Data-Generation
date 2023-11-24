import csv
import os
import random

import pandas as pd
import numpy as np




File_Path = "/Users/user/Desktop/_CODES/pV_4KWp_E5.csv"
df = pd.read_csv(File_Path,sep = ',')

print("len",len(df.columns));

data=[]

# to expand the data from 62 to 150, we choose a random constant
for i in range(150):
    random_column = df[random.choice(df.columns[2:])]
  
    adata = [round((a/1000 * random.uniform(0.9, 1.1)), 3) for a in random_column]
    data.append(adata);



random_df=pd.DataFrame(data).T

random_df.insert(0, 'Hour', df.pop('Hour'))
random_df.insert(0, 'Date', df.pop('Date'))


random_df.to_csv('PV_Generated2.csv', sep=',')

print("ended");