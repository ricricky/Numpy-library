#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np


# In[10]:


arr = np.arange(0,11)


# In[11]:


arr


# In[12]:


# check the elment position simply

arr[7]


# In[13]:


# slicing
arr[0:4]


# In[14]:


arr[0:5]=100


# In[15]:


arr


# In[16]:


arr=np.arange(0,11)


# In[17]:


arr


# In[18]:


slice_of_arr= arr[0:6]


# In[19]:


slice_of_arr


# In[23]:


# when u want to broadcast or chahnge it to diff num , it affects the orgnl array


# In[25]:


slice_of_arr[:] = 99


# In[26]:


slice_of_arr


# In[27]:


arr


# In[4]:


import numpy as np


# In[8]:


arr_2d = np.array([[20,49,59],[70,80,90],[50,80,30]])


# In[9]:


arr_2d


# In[10]:


arr_2d[0,0]


# In[12]:


arr_2d[1][2]


# In[15]:


arr_2d[1]


# In[16]:


arr_2d[:2,1:]


# In[18]:


arr = np.arange(1,11)


# In[19]:


arr


# In[21]:


# comparison operators
arr < 5


# In[22]:


bool_arr = arr < 5


# In[23]:


bool_arr


# In[24]:


# gettng an array and using comparison oprtr with it will return boolean array
arr[bool_arr]


# In[34]:


# for practice

arr_2d = np.arange(50).reshape(5,10)


# In[35]:


arr_2d


# In[37]:


arr_2d[2:4,2:4]


# In[2]:


# practice 
import numpy as np
arr_3d = np.array([[40,50,60],[70,80,90],[35,45,55]])


# In[3]:


arr_3d


# In[7]:


arr_3d = np.arange(30).reshape(3,10)


# In[8]:


arr_3d


# In[10]:


np.zeros(2)


# In[11]:


arr_3d.argmax()


# In[13]:


arr_3d.argmin()


# In[18]:


np.eye(2)


# In[24]:


arr_4d = np.arange(5,50,5),(9,30,3)


# In[25]:


arr_4d


# In[35]:


arr_4d = np.linspace(2,20,1)


# In[36]:


arr_4d


# In[38]:


arr_4d.argmin()


# In[40]:


arr_4d[1:2]


# In[ ]:




