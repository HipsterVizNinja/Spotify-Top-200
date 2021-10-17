from glob import glob
import os
import pandas as pd

directory = 'path to directory'
os.chdir(directory)
for filename in glob('*.csv'):
    df = pd.read_csv(filename)

    df = df.iloc[1:]

    df.to_csv('path to save directory'+filename+'extension', index = False, header=False)

    print(filename)
