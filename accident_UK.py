
# coding: utf-8

# In[1]:


# Step: General cleaning of the data
# 1. Identify the areas with the most accidents.
# 2. Most dangerous roads
# 3. Accidents across different seasons
# 4. Most dangerous days
# 5. Most important causes of the accidents
# 6. Create a predictive model to evaluate the probability of car accidents
# 7. Create dashboard


# In[2]:


# import libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# file name & path name
dir_curr = os.getcwd()
dir_car = os.listdir(dir_curr)[2]
accident_files = ['accidents_2005_to_2007.csv']#,'accidents_2009_to_2011.csv', 'accidents_2012_to_2014.csv']


# load csv data
car_list = []
for file in accident_files:
    file_fullname = dir_car + '/' + file
    car_one = pd.read_csv(file_fullname, index_col=None, header=0)
    car_list.append(car_one)

car_total = pd.concat(car_list, axis=0, ignore_index=True)


# In[5]:


# 1. Identify the areas with the most accidents.
# visualize accidents in the map
# fig, axes = plt.subplots(nrows=2, ncols=2)
# plt.figure(1)
plt.subplot(1,2,1)
car_total.plot(kind='scatter', x='Longitude', y='Latitude', c = 'Urban_or_Rural_Area', s=3, cmap = plt.get_cmap("jet"))
# car_total.plot(kind='scatter', x='Longitude', y='Latitude', c = 'Urban_or_Rural_Area', s=3, cmap = plt.get_cmap("jet"))

# # Urban vs Rural area
# plt.subplot(2,1,2)
# bins = np.array([1.0, 1.5, 2.0]) # just two bins
# plt.hist(car_total['Urban_or_Rural_Area'], bins, normed=True)
# car_total['Urban_or_Rural_Area'].value_counts()

# ==== MUST SOLVE =====#
# 2. Most dangerous roads
def plot_roads(car_total):
    plt.hist(car_total['Road_Type'])
    # plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
    # plt.show()

plot_roads(car_total)
# In[8]:


# 3. Accidents across different seasons
a = pd.to_datetime(car_total['Date'])
car_total['Month'] = a.dt.strftime('%m').astype(str)
car_total['Year'] = a.dt.strftime('%Y').astype(str)

# === Month ===== #
def plot_by_month(car_total):
    n_month = 12
    car_summary = np.zeros(n_month)
    for month in range(n_month):
        n_accident_month = len(car_total[car_total['Month']==str(month+1).zfill(2)])
        car_summary[month] = n_accident_month
    # plot car accidents in each month
    plt.bar(range(n_month), car_summary)
    plt.show()
    return car_summary
plot_by_month(car_total)


# 4. Most dangerous days
# day of week
def bar_dayofweek(car_total):
    car_dayofweek = car_total['Day_of_Week'].value_counts().sort_index()
    DayNames = ['Sun','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    ax = car_dayofweek.plot.bar(x='Day_of_Week')
    # ax.set_xticks(DayNames)
    # plt.show()
bar_dayofweek(car_total)

'''
def plot_by_days(car_total):
    n_dayofweek = 7
    DayNames = ['Sun','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']#,'Sun']
    car_dayofweek = np.zeros(n_dayofweek)
    for day in range(n_dayofweek):
        n_accident_day = sum(car_total['Day_of_Week']==day+1)#.str.contains(DayNames[day]))
        car_dayofweek[day] = n_accident_day
    plt.bar(np.arange(n_dayofweek), car_dayofweek)
    plt.xticks(np.arange(n_dayofweek), DayNames)
    plt.show()
    return car_dayofweek

plot_by_days(car_total)
'''

# 5. Most important causes of the accidents
# plot by road surface
def pie_chart_road_surf(car_total):
    car_conds = (car_total['Road_Surface_Conditions'].value_counts())
    car_conds.plot(kind='pie', y='Road_Surface_Conditions', autopct='%1.1f%%',fontsize=10)
    plt.show()

pie_chart_road_surf(car_total)

# plot by weather
def pie_chart_weather(car_total):
    car_weather = car_total['Weather_Conditions'].value_counts()
    car_weather.plot(kind='pie', y='Weather_Conditions', autopct='%1.1f%%', fontsize=10)
    # plt.show()

pie_chart_weather(car_total)

car_total.keys()

car_conditions = []
n_conditions = len(conditions)
for cond in range(n_conditions):
    cond_count = (conditions[cond] == car_total['Road_Surface_Conditions']).sum()
    car_conditions[cond] = cond_count
car_conditions


# 6. Create a predictive model to evaluate the probability of car accidents
car_total
