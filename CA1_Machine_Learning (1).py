#!/usr/bin/env python
# coding: utf-8

# # CA1 Machine Learning

# In[ ]:





# In[ ]:





# ## Add Python Libraries

# In[12]:


import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np


# ## Data Preparation

# ### Load The Dataset

# In[ ]:





# In[ ]:





# In[13]:


## Create a Function to prepaer a new Dataframe from the original


# In[14]:


def prepare_players(file_name): # file_name is a parameter given to the function

    # read in csv
    df = pd.read_csv(file_name)


     # create duplicate dataframe with required columns only
    df = df[
        ["short_name", 
         "club_name", 
          "club_position", 
          "age",
          "value_eur", 
          "overall", 
         "potential", 
         "skill_moves", 
         "international_reputation", 
         "work_rate", 
         "pace", 
         "shooting", 
         "passing", 
         "dribbling", 
         "physic", 
         "attacking_crossing", 
         "attacking_finishing", 
         "attacking_volleys", 
         "skill_ball_control", 
         "movement_acceleration", 
         "movement_sprint_speed", 
         "movement_agility", 
         "power_shot_power", 
         "mentality_penalties", 
         "mentality_positioning", 
         "mentality_vision", 
         "mentality_composure"
         ] 
    ].copy()

    # rename columns
    df = df.rename(columns={
        "short_name": "Name",
        "club_name": "Club_Team",
        "club_position": "Position",
        "age": "Age",
        "value_eur": "Value(€)",
        "overall": "Overall",
        "potential": "Potential",
        "skill_moves": "Skill_Moves",
        "international_reputation": "Reputation",
        "work_rate": "Work_Rate",
        "pace": "Pace",
        "shooting": "Shooting",
        "passing": "Passing",
        "dribbling": "Dribbling",
        "physic": "Physic",
        "attacking_crossing": "Crossing",
        "attacking_finishing": "Finishing",
        "attacking_volleys": "Volleys",
        "skill_ball_control": "Ball_Control",
        "movement_acceleration": "Acceleration",
        "movement_sprint_speed": "Sprint_Speed",
        "movement_agility": "Agility",
        "power_shot_power": "Shot_Power",
        "mentality_penalties": "Mentality_Pens",
        "mentality_positioning": "Mentality_Position",
        "mentality_vision": "Mentality_Vision",
        "mentality_composure": "Composure",
        } 
    )



    # Filter club position to show only Forward Players
    df = df[df["Position"].isin(["CAM","ST", "LW", "RW", "RS"] ) ]





    return df

    print(df.columns.tolist())


# In[15]:


df_Forwards = prepare_players("FC26.csv") 


# In[ ]:




