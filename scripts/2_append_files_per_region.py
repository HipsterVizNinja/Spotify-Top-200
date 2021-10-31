from glob import glob
import os
import pandas as pd


# Open an empty dataframe
df_all = pd.DataFrame()

# Find files that match wild card by region
directory = '/Users/sm029588/Google Drive/Spotify/Daily_Clean'
outpath = '/Users/sm029588/Google Drive/Spotify/Daily_Ready'
region = 'at'
time = 'daily'
os.chdir(directory)
for f in glob('*'+region+'-'+time+'*.csv'):

    # make sure to apply correct settings (sep, parse_dates, headers, missing_values)
    df = pd.read_csv(f, parse_dates=['chart_date'])

    # append each file to the "master" dataframe
    df_all = df_all.append(df)

    # once all files are appended, we need to sort and reset the index
    df_all.sort_values(['song_id', 'chart_date'], ascending=[True, True], inplace=True)
    df_all.reset_index(drop=True, inplace=True)

    # Find First Date for each songid
    df_all['chart_debut'] = df_all.groupby('song_id')["chart_date"].transform('min')

    # Time to output but only certain fields
    df_all.to_csv(outpath+'/'+time+'_'+region+'_merged.csv', index=False, columns=['chart_position', 'chart_date', 'song', 'performer', 'streams', 'spotify_uri', 'song_id', 'region', 'chart_debut'])

    print(f)