# youtube_data_analysis

### YOUTUBE DATA ANALYSIS USING PYTHON (data source: youtube API)

An analysis systems to analyze youtube data on a topic and the currently available  data/videos.
This is to analyze youtube data (videos, tags, video durations) using a search key word for example "python", channel analysis e.g. using channel ID or name. 

Youtube Search : Python
https://developers.google.com/youtube/v3/docs/search/list



##Data/vidoes' analysis

Tag Vs number videos
Tag with most videos, least videos etc
Tag vs Avg duration of videos
Tag with most video time, least video time etc
Tag Classification
tags vs no. of comments, view count, likes count etc
store the data in some Db or file (choose right one for the task).
Write queries or script for the analysis


Search a Keyword: Python
Number of videos: at least 300 (make sure the sample size is enough get a good
confidence level)
Implementation:

use Apis to fetch data (examples are given below)
Cleanup data


1. Install Anaconda
2. Open jupyter notebook. 
3. Set up postgres database server. Create database: dbname e.g youtubedb

### DATA VARIABLES

1.API_KEY
2. search_keyword
3. max_result
4. file_directory

# Database Connection (using Postgres):
Please enter the database Connection parameters. 
user, password,host,port,dbname i.e pg_conn


# EXECUTE: 
 run  using jupyter notebook: youtube_data_analysis_aviyel.ipynb  in  the src folder. Using the RUN: button on the jupyter notebook top menu.
