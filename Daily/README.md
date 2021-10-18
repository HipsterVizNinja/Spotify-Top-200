# Data Dictionary for Daily charts

  - chart_position: This is the rank of a song for the given chart date
  - chart_date: This is the date of the chart
  - song: This is the name of the song as it shows within Spotify
  - performer: This is the performer(s) of the song
  - song_id: This is a concatenation of the song & performer. Used as a unique id for each song
  - streams: This is the count of streams for the song for the date. [Click here for more info about stream count from Spotify](https://artists.spotify.com/help/article/how-we-calculate-charts)
  - spotify_uri: This is the unique Spotify URI for a particular song. A single song can have multiple URIs, such as the song from album vs song from single could have the same song_id but different URIs
  - region: The region or country
  - time_on_chart: This is the cumulative total number of days a song (by song_id) has appeared on the chart
  - consecutive_days: This is the cumulative consecutive days a song (by song_id) has appeared on the chart. If a song skips a day, this column will start counting over
  - previous_day: This is the previous rank for consecutive time. If this column is null, it is either the initial debut or a reappearance on the chart
  - peak_position: This is the cumulative highest/best ranking so far for that song
  - worst_position: This is the cumulative lowest/worst ranking so far for that song
