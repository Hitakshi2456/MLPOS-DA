#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd


# In[36]:


#QUESTION 1


# In[37]:


Survey=pd.read_excel('SampleSurvey.xlsx',sheet_name="Data")


# In[38]:


Survey.head()


# In[39]:


#QUESTION 2


# In[40]:


Survey.groupby('collection_date').count()['response_id']


# In[41]:


#QUESTION 3


# In[42]:


Survey['age'] = pd.to_numeric(Survey['age'], errors='coerce')


Survey.dropna(subset=['age'], inplace=True)


total_respondents = len(Survey)

respondents_under_45 = len(Survey[Survey['age'] < 45])

proportion_under_45 = respondents_under_45 / total_respondents

print("Proportion of respondents aged less than 45:", proportion_under_45)


# In[43]:


Survey


# In[ ]:


#QUESTION 4


# In[44]:


def age_group(e):
    if(e in range(18,25)):
        return "18-25"
    if(e in range(25,40)):
        return "25-40"
    if(e in range(40,55)):
        return "40-55"
    if(e in range(55,120)):
        return "55+"

Survey['age-group']=Survey['age'].apply(age_group)
Survey.head()


# In[ ]:


#QUESTION 5


# In[52]:


sample=Survey.groupby('age-group').count()
sample[['response_id']]


# In[53]:


print("Max : ",sample['response_id'].max())


# In[ ]:


#QUESTION 6


# In[55]:


print("Ans",len(Survey[(Survey['Past_Vote']=='RJD') & (Survey['Vote_Now']=='RJD')])/len(Survey))


# In[ ]:


#QUESTION 7


# In[ ]:




