import pandas as pd
import numpy as np
from glob import glob
import os
from datetime import timedelta

# Set settings for dataframe
pd.set_option('display.max_rows', 1000)
pd.options.display.max_colwidth = 150
pd.set_option('display.max_columns', None)

directory = '/Users/sm029588/Google Drive/Spotify/Daily_Ready'
outpath = '/Users/sm029588/OneDrive - Cerner Corporation/PycharmProjects/Spotify-Top-200/Daily'

os.chdir(directory)
for f in sorted(glob('*.csv')):

    # Load data in dataframe
    df = pd.read_csv(f, parse_dates=['chart_date', 'chart_debut'])
    # df['chart_position'] = pd.to_numeric(df['chart_position'])

    # drop null SongIDs
    df.dropna(subset=['song_id'], inplace = True)

    # create region variable
    region = df['region']

    # Time on chart
    df['time_on_chart'] = df.groupby('song_id').cumcount() + 1

    # Consecutive Days on chart
    # Daily
    df['consecutive_day'] = df.groupby(['song_id'])['chart_date'].diff()
    df.loc[df['consecutive_day'] == '1 days', 'is_consecutive'] = 1
    df.loc[df['consecutive_day'] != '1 days', 'is_consecutive'] = 0
    df['consecutive_days'] = df.groupby('song_id')["is_consecutive"].cumsum()
    # Weekly
    # df['consecutive_week'] = df.groupby(['song_id'])['chart_date'].diff()
    # df.loc[df['consecutive_week'] == '7 days', 'is_consecutive'] = 1
    # df.loc[df['consecutive_week'] != '7 days', 'is_consecutive'] = 0
    # df['consecutive_weeks'] = df.groupby('song_id')["is_consecutive"].cumsum()

    # Previous Week
    df['previous_rank'] = df.groupby(['song_id'])['chart_position'].shift(1)
    # Daily
    df.loc[df['consecutive_day'] == '1 days', 'previous_day'] = df['previous_rank']
    df.loc[df['consecutive_day'] != '1 days', 'previous_day'] = 0
    #Weekly
    # df.loc[df['consecutive_week'] == '7 days', 'previous_week'] = df['previous_rank']
    # df.loc[df['consecutive_week'] != '7 days', 'previous_week'] = 0

    # Peak Position
    df['peak_position'] = df.groupby(['song_id'])['chart_position'].cummin()

    # Lowest Position
    df['worst_position'] = df.groupby(['song_id'])['chart_position'].cummax()

    # Replace_null
    # Daily
    df['consecutive_days'] = df['consecutive_days'].replace(0, np.nan)
    df['previous_day'] = df['previous_day'].replace(0, np.nan)
    # Weekly
    # df['consecutive_weeks'] = df['consecutive_weeks'].replace(0, np.nan)
    # df['previous_week'] = df['previous_week'].replace(0, np.nan)

    # Create Chart URL
    # Daily
    chart_dt = chart_date_st_start = df['chart_date'].dt.strftime('%Y-%m-%d')
    df['chart_url'] = 'https://www.spotifycharts.com/regional/'+region+'/daily/'+chart_dt
    # Weekly
    # chart_date_st_start = (df['chart_date'] - timedelta(days=6)).dt.strftime('%Y-%m-%d')
    # chart_date_st_end = (df['chart_date'] + timedelta(days=1)).dt.strftime('%Y-%m-%d')
    # df['chart_url'] = 'https://www.spotifycharts.com/regional/'+region+'/weekly/'+chart_date_st_start+'--'+chart_date_st_end

    # create dynamic filename
    #Daily
    df.to_csv(outpath  +'/'+ f, index=False, columns=['chart_position', 'chart_date', 'song', 'performer', 'streams', 'spotify_uri', 'song_id', 'region', 'time_on_chart', 'consecutive_days', 'previous_day', 'peak_position', 'worst_position', 'chart_url'])
    #Weekly
    # df.to_csv(outpath  +'/'+ f, index=False, columns=['chart_position', 'chart_date', 'song', 'performer', 'streams', 'spotify_uri', 'song_id', 'region', 'time_on_chart', 'consecutive_weeks', 'previous_week', 'peak_position', 'worst_position', 'chart_url'])
    print(f)
