#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import json


# In[2]:


#provide the path of csv file
path = "../Resources/Programming_Language_data.csv"


# In[3]:


#read csv_file
language_df = pd.read_csv(path)
language_df.head(10)


# In[4]:


#filterout data between year 1940-2023
filtered_df = language_df[(language_df['appeared'] >= 1940) & (language_df['appeared'] <= 2023)]
filtered_df


# In[5]:


#create newdataframe with only targeted data columns
df = filtered_df[['title','appeared','rank','numberOfUsers','numberOfJobs','githubBigQuery.repos']]
df.head()


# In[6]:


#rename columns 
new_df = df.rename(columns ={'title':'Programming_Language','appeared':'Year','rank':'Rank','numberOfUsers':'Number_Of_Users','numberOfJobs':'Number_Of_Jobs','githubBigQuery.repos':'GitHubBigQuery_Repos'})
new_df.head()


# In[7]:


#fill nan values with 0
clean_df = new_df.fillna(0)
clean_df.head()


# In[8]:


clean_df.info()


# In[9]:


clean_df['GitHubBigQuery_Repos']=clean_df['GitHubBigQuery_Repos'].astype(int)
clean_df


# In[10]:


clean_df.info()


# In[14]:


# Convert Pandas DataFrame To JSON Using orient = 'records' 
json_string = clean_df.to_json(orient='records')


# In[18]:



# specify the file path where you want to save the  data
json_path = '../static/data.json'
# write JSON string to file
with open(json_path, 'w') as f:
    f.write(json_string)








# In[13]:


engine = create_engine("postgresql://postgres:!Cricket07@localhost:5433/Programming_language")
connection = engine.connect()
clean_df.to_sql("programming_language", connection, if_exists="replace")


# In[ ]:




