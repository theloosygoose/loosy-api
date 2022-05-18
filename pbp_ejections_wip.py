#!/usr/bin/env python
# coding: utf-8

# In[41]:
import pandas as pd
import requests
import numpy as np
import time
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType
from nba_api.stats.endpoints import playbyplay

custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}
# In[42]:
nba_teams = teams.get_teams()
nba_teams_df = pd.DataFrame(nba_teams)
nba_teams_id = nba_teams_df['id']

# In[43]:
#Parsing to get pbp data
#Calling the teams function to get games ids that the team has played
temp_03 = []
for i in nba_teams_id:
    temp = leaguegamefinder.LeagueGameFinder(team_id_nullable = [i], season_nullable=Season.default, season_type_nullable=SeasonType.regular) 
    temp_01 = temp.get_normalized_dict()
    temp_02 = temp_01['LeagueGameFinderResults']

    for i in range(len(temp_02)):
        temp_03.append(temp_02[i]['GAME_ID'])
    #temp_03 += temp_02[['GAME_ID']]
    #time.sleep(0.600)
    
print(temp_03)
# In[44]
#get all pbp and filter ejections only
df = pd.DataFrame()
df_temp01 = pd.DataFrame()

def pbp_download(game1, game2):
    for i in temp_03[game1:game2]:
        df.append(playbyplay.PlayByPlay(i).get_data_frames()[0])
        #df_temp01 = df_temp01.query('EVENTMSGTYPE == 11')

pbp_download(0,200)
#pbp_download(200,400)
#pbp_download(400,600)
#pbp_download(600,800)
print(df_temp01)
# %%
df_temp01.to_csv("main.csv")

# %%
