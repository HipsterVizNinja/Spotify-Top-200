import pandas as pd
import numpy as np
from glob import glob
import os
from datetime import timedelta


# Set settings for dataframe
#pd.set_option('display.max_rows', 1000)
pd.options.display.max_colwidth = 150
pd.set_option('display.max_columns', None)

directory = 'directory-path'
os.chdir(directory)
for filename in glob('wildcard match files.extension'):

    #Load data in dataframe
    df = pd.read_csv(filename)

    #Rename Columns
    df.rename(columns={'0': 'chart_position', '1': 'song', '2': 'performer', '3': 'streams', '4': 'spotify_url'}, inplace=True)

    #Prep the data

    #Create Song identifier
    df["song_id"] = df['song']+df['performer']

    #Extract Date from file path name
    df['chart_date'] = pd.to_datetime(df['origin'].str.extract('(\d{4}-\d{2}-\d{2})')[0])
    df['chart_date'] = df['chart_date'] + timedelta(days=6)

    #Sort dataframe for each songid ascending by date
    df.sort_values(['song_id','chart_date'], ascending=[True, True], inplace=True)
    df.reset_index(drop=True, inplace=True)

    #Extract Spotify URI from the URL
    df['spotify_uri'] = df['spotify_url'].str[-22:]

    #Find First Date for each songid
    df['first_date'] = df.groupby('song_id')["chart_date"].transform('min')

    #Extract Region
    df['region'] = df['origin'].str.split('-').str[2]


    #Time on chart
    df['time_on_chart'] = df.groupby('song_id').cumcount() + 1

    #Consecutive Days on chart
    df['consecutive_week'] = df.groupby(['song_id'])['chart_date'].diff()
    df.loc[df['consecutive_week'] == '7 days', 'is_consecutive'] = 1
    df.loc[df['consecutive_week'] != '7 days', 'is_consecutive'] = 0
    df['consecutive_weeks'] = df.groupby('song_id')["is_consecutive"].cumsum()

    #Previous Week
    df['previous_rank'] = df.groupby(['song_id'])['chart_position'].shift(1)
    df.loc[df['consecutive_week'] == '7 days', 'previous_week'] = df['previous_rank']
    df.loc[df['consecutive_week'] != '7 days', 'previous_week'] = 0

    #Peak Position
    df['peak_position'] = df.groupby(['song_id'])['chart_position'].cummin()

    #Lowest Position
    df['worst_position'] = df.groupby(['song_id'])['chart_position'].cummax()

    #Replace_null
    df['consecutive_weeks'] = df['consecutive_weeks'].replace(0, np.nan)
    df['previous_week'] = df['previous_week'].replace(0, np.nan)
    df['worst_position'] = df['worst_position'].replace(-1, np.nan)
    df['peak_position'] = df['peak_position'].replace(-1,np.nan)

    #create dynamic filename

    df.to_csv('output folder path'+filename+'.csv',index=False,columns=['chart_position','chart_date','song','performer','streams','spotify_uri','song_id','region','time_on_chart','consecutive_weeks','previous_week','peak_position','worst_position'],encoding='utf-8')
    print(filename)
