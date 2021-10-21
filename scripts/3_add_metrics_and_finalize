import pandas as pd
import numpy as np
from glob import glob
import os
from datetime import timedelta


# Set settings for dataframe
#pd.set_option('display.max_rows', 1000)
pd.options.display.max_colwidth = 150
pd.set_option('display.max_columns', None)

directory = '/Users/sm029588/OneDrive - Cerner Corporation/Spotify/Weekly Merged'
os.chdir(directory)
for f in glob('/Users/sm029588/Desktop/Daily_Ready/daily_global_merged.csv'):

    #Load data in dataframe
    df = pd.read_csv(f, parse_dates=['chart_date', 'chart_debut'])

    #Time on chart
    df['time_on_chart'] = df.groupby('song_id').cumcount() + 1

    #Consecutive Days on chart
    df['consecutive_day'] = df.groupby(['song_id'])['chart_date'].diff()
    df.loc[df['consecutive_day'] == '1 day', 'is_consecutive'] = 1
    df.loc[df['consecutive_day'] != '1 day', 'is_consecutive'] = 0
    df['consecutive_days'] = df.groupby('song_id')["is_consecutive"].cumsum()

    #Previous Week
    df['previous_rank'] = df.groupby(['song_id'])['chart_position'].shift(1)
    df.loc[df['consecutive_day'] == '1 day', 'previous_day'] = df['previous_rank']
    df.loc[df['consecutive_day'] != '1 day', 'previous_day'] = 0

    #Peak Position
    df['peak_position'] = df.groupby(['song_id'])['chart_position'].cummin()

    #Lowest Position
    df['worst_position'] = df.groupby(['song_id'])['chart_position'].cummax()

    #Replace_null
    df['consecutive_days'] = df['consecutive_days'].replace(0, np.nan)
    df['previous_day'] = df['previous_day'].replace(0, np.nan)

    #create dynamic filename

    #df.to_csv('/Users/sm029588/Documents/GitHub/Spotify-Top-200/Daily/global_merged.csv',index=False,columns=['chart_position','chart_date','song','performer','streams','spotify_uri','song_id','region','time_on_chart','consecutive_weeks','previous_week','peak_position','worst_position'],encoding='utf-8')
    print(df)
