
# coding: utf-8

# In[1]:

path = 'usagov_bitly_data2012-03-16-1331923249.txt'


# In[2]:

open (path).readline()


# In[3]:

import json


# In[4]:

records = [json.loads(line) for line in open(path)]


# In[5]:

records[0]


# In[6]:

records[0]['tz']


# In[7]:

print records[0]['tz']


# In[8]:

time_zones = [rec['tz']for rec in records]


# In[9]:

time_zones = [rec['tz']for rec in records if 'tz' in rec]


# In[10]:

time_zones[:10]


# In[14]:

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


# In[15]:

counts = get_counts(time_zones)


# In[17]:

counts['America/New_York']


# In[18]:

len(time_zones)


# In[20]:

def top_counts(count_dict , n = 10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


# In[21]:

top_counts(counts)


# In[23]:

from collections import Counter


# In[24]:

counts = Counter(time_zones)


# In[25]:

counts.most_common(10)


# In[26]:

from pandas import DataFrame , Series


# In[27]:

import pandas as pd; import numpy as np


# In[28]:

frame = DataFrame(records)


# In[29]:

frame


# In[30]:

frame['tz'][:10]


# In[32]:

tz_counts = frame['tz'].value_counts()


# In[33]:

tz_counts[:10]


# In[34]:

clean_tz = frame['tz'].fillna('Missing')


# In[35]:

clean_tz[clean_tz == ''] = 'Unknown'


# In[36]:

tz_counts = clean_tz.value_counts()


# In[37]:

tz_counts[:10]


# In[45]:

import matplotlib
get_ipython().magic(u'matplotlib inline')


# In[46]:

tz_counts[:10].plot(kind = 'barh',rot =0)


# In[47]:

frame['a'][1]


# In[48]:

results = Series([x.split()[0] for x in frame.a.dropna()])


# In[49]:

results[:5]


# In[50]:

cframe = frame[frame.a.notnull()]


# In[60]:

os = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')


# In[61]:

os


# In[62]:

os[:5]


# In[63]:

by_tz_os = cframe.groupby(['tz', os])


# In[64]:

add_counts = by_tz_os.size().unstack().fillna(0)


# In[65]:

add_counts


# In[66]:

indexer  =  add_counts.sum(1).argsort()


# In[67]:

indexer


# In[68]:

count_subset = add_counts.take(indexer)[-10:]


# In[69]:

count_subset


# In[71]:

count_subset.plot(kind = 'barh',stacked = True)


# In[72]:

normed_subset = count_subset.div(count_subset.sum(1), axis = 0 )


# In[73]:

normed_subset.plot(kind = 'barh ', stacked = True)


# In[ ]:



