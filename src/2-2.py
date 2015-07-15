
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

unames = ['user_id','gender','age','occupation','zip']


# In[7]:

users = pd.read_table('users.dat' , sep='::' , header=None, names=unames)


# In[8]:

users


# In[9]:

rnames = ['user_id','movie_id','rating','timestamp']


# In[10]:

ratings = pd.read_table('ratings.dat',sep = '::' , header = None, names =rnames)


# In[11]:

ratings


# In[12]:

mnames = ['movie_id','title','genres']


# In[13]:

movies = pd.read_table('movies.dat', sep = '::',header = None,names = mnames)


# In[14]:

movies


# In[15]:

data = pd.merge(pd.merge(ratings , users) , movies)


# In[16]:

data


# In[29]:

mean_ratings = data.pivot_table('rating', index = 'title', columns = 'gender', aggfunc = 'mean')


# In[30]:

mean_ratings


# In[31]:

ratings_by_title = data.groupby('title').size()


# In[32]:

ratings_by_title


# In[33]:

active_titles = ratings_by_title.index[ratings_by_title >= 250]


# In[39]:

active_titles


# In[40]:

mean_ratings = mean_ratings.ix[active_titles]


# In[41]:

mean_ratings


# In[42]:

top_female_ratings = mean_ratings.sort_index(by = 'F',ascending = False)


# In[43]:

top_female_ratings


# In[44]:

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']


# In[45]:

sorted_by_diff = mean_ratings.sort_index(by='diff')


# In[46]:

sorted_by_diff


# In[47]:

sorted_by_diff[::-1][:15]


# In[48]:

rating_std_by_title = data.groupby('title')['rating'].std()


# In[49]:

rating_std_by_title = rating_std_by_title.ix[active_titles]


# In[51]:

rating_std_by_title.order(ascending=False)[:10]


# In[ ]:



