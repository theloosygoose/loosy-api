#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import requests
import numpy as np
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import teams


# In[42]:


nba_teams = teams.get_teams()
nba_teams_df = pd.DataFrame(nba_teams, columns=['id', 'full_name', 'abbreviation', 'nickname', 'city', 'state', 'year_founded'])
nba_teams_id = nba_teams_df['id']


# In[43]:
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType

#Parsing to get pbp data
#Calling the teams function to get games ids that the team has played
temp_02 = []
for i in nba_teams_id:
    temp = leaguegamefinder.LeagueGameFinder(team_id_nullable = [i], season_nullable=Season.default, season_type_nullable=SeasonType.regular)
    temp_01 = temp.get_normalized_dict()
    temp_02 += temp_01['LeagueGameFinderResults']
#    temp_03 += temp_02
    
print(len(temp_02))
# %%
