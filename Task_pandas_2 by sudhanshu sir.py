#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd


# In[35]:


df=pd.read_csv(r"C:\Users\shahi\Downloads\AgentPerformance (1).xlsx - Agent Performance Report.updated555.csv")


# In[41]:


df1=pd.read_csv(r"C:\Users\shahi\Downloads\Agent_Login_Report (4).xls - Agent Login Report.updated.csv")


# In[42]:


df1


# In[43]:


df1.dtypes


# In[36]:


df


# In[37]:


df.dtypes


# In[12]:


date1=pd.to_datetime(df['Date'])


# In[13]:


date1


# In[17]:


type(date1[0])


# In[18]:


df['date_converter']=date1


# In[21]:


df


# In[20]:


df['working_days']=5


# # 1 .Find out there avarage rating on weekly basis keep this in a mind that they take two days of leave

# In[26]:


df['avd_rate_wekkly']=df['Average Rating'] % df['working_days']


# In[27]:


df


# # 2 .Total working days for each agents 

# In[48]:


df1.groupby('Agent')['Date'].count() #but for df.agent why same not


# # 3. Total query that you have taken 

# In[54]:


df.groupby('Agent Name')['Total Chats'].sum()


# # 4. total Feedback that you have received 

# In[58]:


df.groupby('Agent Name')['Total Feedback'].sum()


# # 5. a agent name who have average rating between 3.5 to 4 

# In[63]:


df3=(df['Average Rating']>=3) & (df['Average Rating']<=4)


# In[75]:


df[df['Average Rating']==df3]['Agent Name']


# # 6 . Agent name who have rating lesss then 3.5 

# In[76]:


df4=df['Average Rating']<3


# In[89]:


df[df['Average Rating']==df4]['Agent Name']


# # 7 . agent name who have rating more then 4.5 

# In[80]:


df5=df['Average Rating']>4


# In[90]:


df[df['Average Rating']==df5]['Agent Name'] #ehy first numbers then


# # 8 . how many feedaback agents have received more then 4.5 average

# In[97]:


(df['Total Feedback']>4.5).sum()


# In[99]:


df['Total Feedback'].sum() ##extras ignore 


# # 9 . average weekly response time for each agent 

# In[108]:


data2=pd.to_datetime(df['Average Response Time'])


# In[110]:


df['Average Response Time_converter']=data2


# In[111]:


df.head()


# In[118]:


df.groupby('Average Response Time_converter')['Agent Name'].ipynb_checkpoints/


# In[126]:


df[['Agent Name','Average Response Time']]


# # 10 . average weekely resolution time for each agents 

# In[132]:


time=pd.to_datetime(df['Average Resolution Time'])


# In[135]:


df['avg_resolution_time']=time


# In[140]:


df['avg_resolution_time_weekly']=df['avg_resolution_time'].dt.week


# In[143]:


df['avg_resolution_time'].dt.week


# # 11 . list of all agents name 

# In[149]:


l=list(df['Agent Name']).count()


# In[148]:


l


# In[152]:


df['Agent Name'].count() #here duplicates also there


# # 12 . percentage of chat on which they have received a feedback 

# In[157]:


df['chat_per'] = (df['Total Feedback'] / df['Total Chats']) * 100


# In[158]:


df


# # 13 . Total contributation hour for each and every agents weekly basis 
# 

# # 14. total percentage of active hour for a month 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




