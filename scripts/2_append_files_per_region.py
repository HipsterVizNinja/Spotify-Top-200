import pandas as pd
import glob

# Open an empty dataframe
df_all = pd.DataFrame()

# Find files that match wild card by region
for f in glob.glob("input path/filename or wildcard match"):

    # make sure to apply correct settings (sep, parse_dates, headers, missing_values)
    df = pd.read_csv(f, parse_dates=['chart_date'])

    # append each file to the "master" dataframe
    df_all = df_all.append(df)
    region = df_all['region']

    # once all files are appended, we need to sort and reset the index
    df_all.sort_values(['song_id', 'chart_date'], ascending=[True, True], inplace=True)
    df_all.reset_index(drop=True, inplace=True)

    # Find First Date for each songid
    df_all['chart_debut'] = df_all.groupby('song_id')["chart_date"].transform('min')

    # Time to output but only certain fields
    df_all.to_csv('output merged filename', index=False, columns=['chart_position', 'chart_date', 'song', 'performer', 'streams', 'spotify_uri', 'song_id', 'region', 'chart_debut'])

    print(f)