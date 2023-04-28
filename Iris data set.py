#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[ ]:





# In[4]:


myfile=pd.read_csv("C:\\Users\\Super\\OneDrive\\Documents\\Iris Data.csv",index_col="Id")


# In[5]:


myfile


# In[ ]:





# In[6]:


myfile[44:45]


# In[7]:


myfile[120:150]


# In[8]:


x=myfile.SepalLengthCm


# In[32]:


y=myfile.SepalWidthCm


# In[33]:


a=myfile.PetalLengthCm


# In[34]:


b=myfile.PetalWidthCm


# In[35]:


plt.scatter(x,y,label="color")
plt.grid()


# In[36]:


plt.scatter(a,b,color="skyblue")
plt.grid()


# In[37]:


color=myfile.Species


# In[38]:


plt.scatter(x,y,label="color")
plt.scatter(a,b,label="color")
plt.grid()


# In[39]:


plt.scatter(x,y)
plt.grid()


# In[40]:


plt.scatter(a,y)
plt.grid()


# In[41]:


x=myfile["SepalLengthCm"]
y=myfile["SepalWidthCm"]
x2=myfile["PetalLengthCm"]
y2=myfile["PetalWidthCm"]
s=myfile["Species"]


# In[42]:


plt.subplot(1,2,1)
plt.hist2d(x,y,label="species",bins=30)
plt.subplot(1,2,2)
plt.plot(x2,y2,label="species",color="red",linestyle="dotted")


# In[46]:


myfile.plot.scatter("SepalLengthCm","SepalWidthCm")
plt.grid()


# In[9]:


myfile.plot()


# In[ ]:




