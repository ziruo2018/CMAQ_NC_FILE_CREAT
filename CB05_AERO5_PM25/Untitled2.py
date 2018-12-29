
# coding: utf-8

# In[78]:


import pandas as pd 


# In[79]:


file_spe = pd.read_excel(r"C:\Users\lenovo\Desktop\模型物种分配\网格分配.xls")


# In[80]:


file_spe['PM2_5'].head()


# In[81]:


file_pm25_coefficient = pd.read_excel(r"C:\Users\lenovo\Desktop\模型物种分配\CB05_AERO5\AERO5_不同行业分配系数.xlsx",index_col='物种')


# In[82]:


file_pm25_coefficient['工业锅炉（烧煤）']


# In[83]:


file1 = file_spe['PM2_5'].copy()


# In[84]:


#新建DATAFRAME
file = pd.DataFrame()


# In[85]:


file['PM2_5']=file1


# In[86]:


for name in file_pm25_coefficient['工业锅炉（烧煤）'].index:
    file[name]=file['PM2_5']*file_pm25_coefficient['工业锅炉（烧煤）'][name]


# In[90]:


file.to_excel(r'C:\Users\lenovo\Desktop\模型物种分配\CB05_AERO5\PM2_5.xlsx',index=None)

