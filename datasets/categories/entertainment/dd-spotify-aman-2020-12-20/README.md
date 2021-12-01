# Spotify Streaming Data
`Categories > Entertainment`
Spotify streaming data for Aman B, between 22019 and 20320
## Download
Install the `desidata` package using CRAN and then call the `download_data()` function:
```r
library(desidata)
download_data(name = "dd-spotify-aman-2020-12-20")
```
## Data Dictionary 
| Column Name | Column Type | Column Description |
| ----------- | ----------- | --------------- |
| Unnamed: 0 | ID | numeric |
| id | ID of song on Spotify | string |
| artistName | Name of Artist | string |
| trackName | Name of Song | string |
| time | time listened at | datetime |
| date | date listened at | date |
| duration | duration of song | numeric |
| msPlayed | duration played for in millisecond | numeric |
| percent_song | percentage of song listened to | numeric |

# Source
This dataset is sourced from Spotify
# License
CC BY
## Cite This Dataset
Spotify (2020-12-20). 'Spotify Streaming Data', https://github.com/thedivtagguy/desidatasets/tree/master/datasets/categories/entertainment/dd-spotify-aman-2020-12-20. Retrieved from Spotify Developer API 

`desidata for R`