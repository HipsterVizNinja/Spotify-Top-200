from glob import glob
import os
import pandas as pd
from datetime import timedelta


directory = '/Users/sm029588/Google Drive/Spotify/Daily'  # Change to your input folder
outpath = '/Users/sm029588/Google Drive/Spotify/Daily_Clean'  # Change to your output folder
os.chdir(directory)

for filename in sorted(glob('*-weekly-*.csv')):  # What files do you want to run this code on?
    df = pd.read_csv(filename, usecols=['rank', 'uri', 'artist_names', 'track_name', 'streams'])
    df = df.rename(columns={'rank':'chart_position', 'uri':'spotify_url', 'artist_names':'performer', 'track_name':'song'})

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
    # Daily
    df['chart_date'] = pd.to_datetime(df['origin'].str.extract('(\d{4}-\d{2}-\d{2})')[0])
    # Weekly
    # df['chart_dates'] = pd.to_datetime(df['origin'].str.extract('(\d{4}-\d{2}-\d{2})')[0])
    # df['chart_date'] = df['chart_dates'] + timedelta(days=6)

    df.to_csv(outpath+'/'+filename, index=False, columns=['chart_position', 'song', 'performer', 'streams', 'spotify_url', 'origin', 'song_id', 'region', 'spotify_uri', 'chart_date'])

    print(filename)
