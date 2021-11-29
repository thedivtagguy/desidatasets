# Spotify Streaming
`Categories > Entertainment`

Streaming history for Aman Bhargava between 2019 and 2021

## Download

Install the `desidata` package using CRAN and then call the `download_data()` function:
```r
library(desidata)
download_data(name = "dd-spotify-streaming-2021-29-11")
```

## Data Dictionary 

| Column Name | Column Type | Column Description |
| ----------- | ----------- | --------------- |
| id | numeric | Spotify ID for the song |
| artistName | character | Name of the artist who wrote the song |
| trackName | character | Name of the song |
| date | date | Date played |
| time | time | Time played at |
| msPlayed | numeric | Time played for in milliseconds |
| percent_song | numeric | Percentage of the song played. Might be more than 100 if song is replayed before finished. |
| endTime | datetime | Time finished playing |


# Source
This dataset is sourced from Spotify

# License
CC0

## Cite This Dataset
Spotify (2021-29-11). 'Spotify Streaming', https://github.com/thedivtagguy/desidatasets/tree/master/datasets/categories/entertainment/dd-spotify-streaming-2021-29-11. Retrieved from spotify.com 



`desidata for R`