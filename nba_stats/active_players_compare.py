
#%%
from nba_api.stats.static import players
import pandas as pd
import pickle 


#%%
active_players = players.get_active_players()