#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_excel("Temporary_data3_Left_Right_Copy.xlsx")
datacorr = data.corr()
pd.set_option("display.max_columns", 1500)
pd.set_option("display.max_row", 1800)
pd.set_option("display.width", 1000)
df=pd.DataFrame(data)
df.head()


# >**TASK-7A: Please apply one-hot encoding method on one of the categorical variables (not SEX/gender) for the given AD dataset. Please explain what kind of transformation occured on the dataset.**

# In[2]:


# apply one-hot encoding method on one of the categorical variables
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
encoder = OneHotEncoder(handle_unknown="ignore")
encoder_df = pd.DataFrame(encoder.fit_transform(df[["NACCAPOE"]]).toarray())
data_encoded=df.join(encoder_df)
data_encoded.head()


# >**TASK-7B: Please provide a couple of pivot tables in order to illustrate how SEX variable is influential on our target array (CDRGLOB). Please provide a few multidimensional analyses (not limited to two variables).**

# In[3]:


rsumfrm=pd.qcut(data['RSUPFRM'],4)
csfvol=pd.qcut(data['CSFVOL'],6)
data_encoded.pivot_table('RHIPPO',index=['CDRGLOB','SEX'],columns=csfvol)


# In[4]:


rsumfrm=pd.qcut(data['RSUPFRM'],4)
csfvol=pd.qcut(data['CSFVOL'],6)
data_encoded.pivot_table('CDRGLOB',index=['SEX',rsumfrm],columns=csfvol)


# In[5]:


rsumfrm=pd.qcut(data['RSUPFRM'],4)
csfvol=pd.qcut(data['CSFVOL'],6)
data_encoded.pivot_table('CDRGLOB',index=['SEX'],columns=csfvol)


# >**TASK-7C: Referring to the problem in part B, please provide a potential solution to the gender-based issue that appears as a bottleneck for the model development phase. One possible solution might be to provide normalization of the numeric columns with respect to the total brain volume (NACCBRNV column).**

# In[6]:


data_encoded_1=data_encoded.loc[:,'NACCICV':'RTRTEMM']
data_encoded_1


# In[7]:


data_encoded_2=data_encoded['NACCBRNV']
data_encoded_2


# In[8]:


data_encoded.loc[:,'NACCICV':'RTRTEMM']=data_encoded.loc[:,'NACCICV':'RTRTEMM'].div(data_encoded['NACCBRNV'], axis=0)
data_encoded


# >**TASK-7D: After the normalization process, please provide a correlation matrix to report the critical features that have high correlation (positive or negative) with the target array (CDRGLOB).**

# In[9]:


data_encoded_corr=data_encoded.corr()
data_encoded_corr


# In[10]:


data_encoded_corr_cdrglobclm=data_encoded_corr.loc['CDRGLOB'].abs()>0.4
data_encoded_corr_cdrglobclm[data_encoded_corr_cdrglobclm==True]


# In[11]:


data_crr_b4=data_encoded_corr[data_encoded_corr.loc['CDRGLOB'].abs()>0.4]['CDRGLOB']
data_crr_b4


# >**TASK-7E: Please develop 3 distinct formulas (in other words derived features like BMI score) that involve the critical features in Part-7D and then ensure that these derived features could be used as predictive variables for CDRGLOB (again correlation analysis will give you insight).**

# In[12]:


def f1(x,z):
  return x*z

def f2(x,y,z,k):
  return (k*y)+(z+x)

def f3(x,y):
  return (2*x)*(1/y)


# In[13]:


f1_data=f1(data_encoded['APA'],data_encoded['CSFVOL'])


# In[14]:


f2_data=f2(data_encoded['RLATVENT'],data_encoded['CERECSF'],data_encoded['LLATVENT'],data_encoded['INDEPEND'])


# In[15]:


f3_data=f3(data_encoded['NACCICV'],data_encoded['NACCMMSE'])


# In[16]:



for i in [f1_data,f2_data,f3_data]:
    (i - i.min()) / (i.max() - i.min())
    print(i)


# In[17]:


f1_data_norm= (f1_data - f1_data.min()) / (f1_data.max() - f1_data.min())
f2_data_norm= (f2_data - f2_data.min()) / (f2_data.max() - f2_data.min())
f3_data_norm= (f3_data - f3_data.min()) / (f3_data.max() - f3_data.min())


# In[18]:


data_w3_glb=pd.DataFrame((f1_data_norm,f2_data_norm,f3_data_norm,data_encoded["CDRGLOB"])).T
data_w3_glb.rename(columns={'Unnamed 0': 'F1', 'Unnamed 1': 'F2','Unnamed 2': 'F3'}, inplace=True)


# In[19]:


data_w3_glb.corr()['CDRGLOB']


# In[20]:


data_w3_glb.corr()


# In[21]:


import numpy as np
import matplotlib.pyplot as plt
plt.imshow( data_w3_glb.corr() , cmap = 'winter' , interpolation = 'nearest' )
plt.title( "2-D Heat Map" )
plt.show()

