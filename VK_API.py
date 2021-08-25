#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
import vk_api
import os
import requests
import json
import random

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import sys


# In[2]:


token = ''


# In[3]:


vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()


# In[7]:


vk.messages.send(
        chat_id=1,
        random_id=1,
        message='Neo, wake up...')


# In[12]:


path = '/home/jupyter-a.mihejchik-8/Lesson_7_API/7_miniproject/save_test.csv'
file_name = 'save_test.csv'
path_to_file = path
upload_url = vk.docs.getMessagesUploadServer(peer_id=2000000001)["upload_url"]
file = {'file': (file_name, open(path_to_file, 'rb'))}
response = requests.post(upload_url, files=file)
json_data = json.loads(response.text)
json_data


# In[16]:


saved_file = vk.docs.save(file=json_data['file'], title=file_name)
saved_file


# In[18]:


attachment = 'doc{}_{}'.format(saved_file['doc']['owner_id'], saved_file['doc']['id'])
attachment


# In[19]:


vk.messages.send(
        chat_id=1,
        random_id=3,
        attachment = attachment,
        message='Neponjatno nihera')


# In[ ]:




