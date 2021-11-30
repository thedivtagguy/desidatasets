# Spotify Streaming Data
`Categories > Entertainment`


Data of Spotify streams from Aman's account between 2019 and 2020

## Download

Install the `desidata` package using CRAN and then call the `download_data()` function:
```r
library(desidata)
download_data(name = "dd-spotify-streams-2021-30-11")
```

## Data Dictionary 

| Column Name | Column Type | Column Description |
| ----------- | ----------- | --------------- |
| Unnamed: 0 | id column (empty) | numeric |
| id | Song's ID on Spotify | string |
| artistName | Name of the artist | string |
| trackName | Name of the song | string |
| time | Time played at | datetime |
| date | Date played at | date |
| duration | Length of song | numeric |
| msPlayed | Duration of time played in milliseconds | numeric |
| percent_song | Percentage of song played. might be more than 100 if song is replayed before finishing | numeric |
| endTime | Time finished playing | datetime |


# Source
This dataset is sourced from Spotify

# License
CC BY

## Cite This Dataset
Spotify (2021-30-11). 'Spotify Streaming Data', https://github.com/thedivtagguy/desidatasets/tree/master/datasets/categories/entertainment/dd-spotify-streams-2021-30-11. Retrieved from Spotify Developer API 



`desidata for R`