#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer 


# In[4]:


df = pd.read_csv('D:\country_wise_latest.csv')


# In[5]:


df


# In[6]:


df.drop(['Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered'],axis=1,inplace=True)


# In[7]:


df


# In[10]:


imputer = SimpleImputer(strategy='constant')
df2 = pd.DataFrame(imputer.fit_transform(df),columns=df.columns)


# In[11]:


df2


# In[16]:


df2 = df2.rename(columns={'Country/Region':'Country'})


# In[17]:


df2


# In[22]:


df3 = df2.groupby(['Country'])[['Confirmed','Deaths','Recovered']].sum().reset_index()


# In[23]:


df3


# In[25]:


countries = df3['Country'].unique()
len(countries)


# In[41]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

countries = df3['Country'].unique()

for country in countries:
    C = df3[df3['Country'] == country]
    plt.scatter(np.arange(0, len(C)), C['Confirmed'], color='blue', label='Confirmed')
    plt.scatter(np.arange(0, len(C)), C['Deaths'], color='red', label='Deaths')
    plt.scatter(np.arange(0, len(C)), C['Recovered'], color='green', label='Recovered')
    plt.title(country)
    plt.xlabel('Overall Covid Days')
    plt.ylabel('Cases')
    plt.legend()
    plt.show()


# In[44]:


country_with_most_recovered = df3.loc[df3['Recovered'].idxmax(), 'Country']
most_recovered_cases = df3['Recovered'].max()

print(f"The country with the most recovered cases is {country_with_most_recovered} with {most_recovered_cases} recovered cases.")


# In[49]:


country_with_most_confirmed_cases = df3.loc[df3['Confirmed'].idxmax(), 'Country']
most_confirmed_cases = df3['Confirmed'].max()

print(f"The country with the most confirmed cases is {country_with_most_confirmed_cases} with {most_confirmed_cases} confirmed cases.")


# In[50]:


country_with_most_deaths = df3.loc[df3['Deaths'].idxmax(), 'Country']
most_death_cases = df3['Deaths'].max()

print(f"The country with the most death cases is {country_with_most_deaths} with {most_death_cases} death cases.")


# In[52]:


country_with_min_deaths = df3.loc[df3['Deaths'].idxmin(), 'Country']
min_death_cases = df3['Deaths'].min()

print(f"The country with the minimum death cases is {country_with_min_deaths} with {min_death_cases} death cases.")


# In[54]:


country_with_min_recovery = df3.loc[df3['Recovered'].idxmin(), 'Country']
min_recovery_cases = df3['Recovered'].min()

print(f"The country with the minimum recovered cases is {country_with_min_recovery} with {min_recovery_cases} recovered cases.")


# In[55]:


country_with_min_confirmed_cases = df3.loc[df3['Confirmed'].idxmin(), 'Country']
min_confirmed_cases = df3['Confirmed'].min()

print(f"The country with the minimum confirmed cases is {country_with_min_confirmed_cases} with {min_confirmed_cases} confirmed cases.")


# In[ ]:




