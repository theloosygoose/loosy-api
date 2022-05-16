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


# In[42]:


nba_teams = teams.get_teams()
nba_teams_df = pd.DataFrame(nba_teams, columns=['id', 'full_name', 'abbreviation', 'nickname', 'city', 'state', 'year_founded'])
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
