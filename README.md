# Spotify Top 200

## This repo is where you will find historical daily and weekly charts for the Spotify Top 200.

Contained in this main branch is the python code I use to clean and prep the daily and weekly charts. The unique charts themselves are pulled from [Spotify Charts](https://charts.spotify.com) in daily or weekly batches - on chart per day/week per region. There's a bit a cleaning that needs to happen in order to get it ready.

Additionally, Spotify uses a two-character abbreviation for each region. You can use the region_lookup.csv file to get the region friendly names.

The Daily and Weekly folders contain the region-specific merged chart data. The data dictionary for each can be found in the README files within the folder  
