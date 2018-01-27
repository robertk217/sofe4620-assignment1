#########################################################################################################################################
# SOFE 4620 - Machine Learning and Data Mining
# 
# Instructor:  Dr. Makrehchi
# TA:  Neil Seward
#
# ASSIGNMENT #1 
#
# Date: Jan. 28, 2018
#
# Author:  Robert Kocovski (100536625)
#
#
#
# This script uses NHL api to get the season stats for player Kris Letang (id: 8471724) for seasons 0 (2002/2003) to season 19 (2017/2018)
# and saves to csv file.
# The data headers for each season vary (some years have less data and some have more).
# This script could be expanded to create csv files for other player IDs.
#########################################################################################################################################


# import libraries
import pandas as pd
import requests

HEADERS = { 
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Host': 'statsapi.web.nhl.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	}

# define function
def get_data(url, i):
    response = requests.get(url, headers=HEADERS)
    while response.status_code != 200:
        response = requests.get(url)
    # explore the response in developers tools 
    headers = response.json()['people'][0]['stats'][0]['splits'][i]['stat'].keys()
    headers = list(headers)
    data = response.json()['people'][0]['stats'][0]['splits'][i]['stat'].values()
    data = [list(data)]
    data = pd.DataFrame(data, columns=headers)
    return data
	
# define the url

url = 'https://statsapi.web.nhl.com/api/v1/people/8471724?expand=person.stats&stats=yearByYear'

#iterate through 0 to 19 seasons
for i in range(0,20):
    
# get the pandas data frame
    data = get_data(url, i)

# print rows of information with column names
    print(data.head())

# save data to csv file, removing index
    data.to_csv('player_8471724_season_stats.csv', index=False, mode = 'a')