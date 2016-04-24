
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')

import numpy as np
import matplotlib.pyplot as plt
import scipy
import xarray
import csv


# In[2]:

#Vars we want

temp = []
u_star = []
wind_dir = []
wind_spd = []
Year = []
Day = []
Month = []
Hour = []


# In[3]:



#open file

with open('tower_irgason_halfhourlydata-clean.csv','r') as f:
    r = csv.DictReader(f, delimiter=',')
    for row in r:
        Year.append(row['Year'])
        Month.append(row['Month'])
        Day.append(row['Day'])
        Hour.append( row['Hour (UTC)'])
        temp.append(row['Tair_sonic (deg C)'])
        wind_dir.append(row['wnd_dir_compass_corrected (deg)'])
        wind_spd.append(row['wnd_spd (ms-1)'])


# In[4]:

#convert to np array
temp = np.array(temp)
u_star = np.array(u_star)
wind_dir = np.array(wind_dir)
wind_spd = np.array(wind_spd)
Year = np.array(Year)
Day = np.array(Day)
Month = np.array(Month)
Hour = np.array(Hour)


# In[5]:

wind_dir = wind_dir.astype(float)
print(wind_dir[1:10])


# In[6]:

wind_dir_rad = (wind_dir / 180.0) * np.pi
radius = np.arange(0,1288,1)
print(wind_dir_rad[1:10])


# In[14]:


plt.polar(wind_dir_rad, radius, 's', ms=2)
a = plt.gca()
fig = plt.gcf()
fig.set_size_inches(10,10)
fig.set_dpi()
a.set_theta_zero_location('N')
a.set
plt.show()
print('done')


# In[ ]:




# In[ ]:



