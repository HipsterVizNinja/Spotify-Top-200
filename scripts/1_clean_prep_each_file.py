from glob import glob
import os
import pandas as pd


directory = 'input directory'
outpath = 'output path'
os.chdir(directory)
header_list = ['chart_position', 'song', 'performer', 'streams', 'spotify_url']
for filename in glob('filename or wildcard match'):
    df = pd.read_csv(filename, names=header_list)

    #get rid of junk rows
    df = df.iloc[2:]

    #add a column with a csv name
    df["origin"] = filename

    #Create Song identifier
    df["song_id"] = df['song']+df['performer']

    #grab the region
    df['region'] = df['origin'].str.split('-').str[1]
    region = df['region']

    #Extract Spotify URI from the URL
    df['spotify_uri'] = df['spotify_url'].str[-22:]

    #Extract Date from file path name
    df['chart_date'] = pd.to_datetime(df['origin'].str.extract('(\d{4}-\d{2}-\d{2})')[0])


    df.to_csv(outpath+filename, index=False)

    print(filename)
