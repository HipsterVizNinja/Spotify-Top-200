from glob import glob
import os
import pandas as pd

# point to your directory containing raw files
directory = 'This is the folder where your raw files live'
os.chdir(directory)

# create the column name list
header_list = ['chart_position', 'song', 'performer', 'streams', 'spotify_url']

# run through each raw file
for filename in glob('*.csv'):
    df = pd.read_csv(filename, names=header_list)

    # get rid of junk rows
    df = df.iloc[2:]

    # add a column with a csv name
    df["origin"] = filename

    # Create Song identifier
    df["song_id"] = df['song']+df['performer']

    # grab the region
    df['region'] = df['origin'].str.split('-').str[1]
    region = df['region']

    # Extract Spotify URI from the URL
    df['spotify_uri'] = df['spotify_url'].str[-22:]

    # Extract Date from file path name
    df['chart_date'] = pd.to_datetime(df['origin'].str.extract('(\d{4}-\d{2}-\d{2})')[0])

    # Ready to output
    df.to_csv('/Users/sm029588/Desktop/Daily_Clean/'+filename, index=False)

    print(filename)
