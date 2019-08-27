
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

# import libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import folium
from sklearn.preprocessing import OrdinalEncoder
# from arcgis.gis import GIS

# file name & path name
dir_curr = os.getcwd()
dir_car = os.listdir(dir_curr)[2]
accident_files = ['accidents_2005_to_2007.csv']#,'accidents_2009_to_2011.csv', 'accidents_2012_to_2014.csv']


# load csv data
car_list = []
for file in accident_files:
    file_fullname = dir_car + '/' + file
    car_one = pd.read_csv(file_fullname, index_col=None)
    car_list.append(car_one)

car_total = pd.concat(car_list, axis=0, ignore_index=True)
# car_total.to_csv('accidents_2005_to_2014.csv')

# feature selection
column_useless = ['Accident_Index','Location_Northing_OSGR','Location_Easting_OSGR','Police_Force',
'Local_Authority_(District)','Local_Authority_(Highway)','Junction_Detail','Junction_Control',
'Did_Police_Officer_Attend_Scene_of_Accident','LSOA_of_Accident_Location',
'Pedestrian_Crossing-Human_Control','Pedestrian_Crossing-Physical_Facilities']

car_total.drop(column_useless,1,inplace=True)
car_total.keys()

a = pd.to_datetime(car_total['Date'], dayfirst = True)
car_total['Month'] = a.dt.strftime('%m').astype(str)
car_total['Year'] = a.dt.strftime('%Y').astype(str)

# 1. Identify the areas with the most accidents.
# visualize accidents in the map
def map_overlay(car_total):
    car_total.plot(kind='scatter', x='Longitude', y='Latitude', s=3)#, cmap = plt.get_cmap("jet"))
    map_hooray = folium.Map(location=[51.5074, 0.1278], zoom_start = 10)

map_overlay(car_total)

# # Urban vs Rural area

# ==== MUST SOLVE =====#
# 2. Most dangerous roads
def plot_roads(car_total):
    plt.hist(car_total['Road_Type'])
    plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
    # plt.show()

plot_roads(car_total)

# carriageway risk
(car_total['Carriageway_Hazards'].value_counts()).plot(kind='bar')

# speed limit in the accident
(car_total['Speed_limit'].value_counts().sort_index().plot(kind='bar'))

# number of vehicles in the accident
# for accident in n_accidents:
def plot_number_vehicle(car_total):
    car_total['Number_of_Vehicles'].value_counts().sort_index().plot(kind='bar')
    # plt.xlim(-1, 10)

plot_number_vehicle(car_total)
# number of causalities
car_total['Number_of_Casualties'].value_counts().sort_index().plot(kind='bar')

# light conditions
car_total['Light_Conditions'].value_counts().plot(kind='bar')
# road class
car_total['1st_Road_Class'].value_counts()

# 3. Accidents across different seasons

# === Month ===== #
def plot_by_month(car_total):
    # n_month = 12
    car_month = car_total['Month'].value_counts().sort_index()
    n_month = len(car_month)
    plt.bar(np.arange(n_month), car_month)
    plt.xticks(np.arange(n_month),car_month.index)
    plt.show()

plot_by_month(car_total)


def plot_by_year(car_total):
    car_year = car_total['Year'].value_counts().sort_index()
    n_year = len(car_year)
    plt.plot(np.arange(n_year), car_year, '.--')
    plt.xticks(np.arange(n_year),car_year.index)#year_list)
    plt.show()

#==== Year ======#
plot_by_year(car_total)


# 4. Most dangerous days
# day of week
def bar_dayofweek(car_total):
    car_dayofweek = car_total['Day_of_Week'].value_counts().sort_index()
    DayNames = ['Sun','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    ax = car_dayofweek.plot.bar(x='Day_of_Week', color='gray')
    ax.set_xticklabels(DayNames, rotation=0)
    plt.show()
bar_dayofweek(car_total)


# 5. Most important causes of the accidents
# plot by road surface
def pie_chart_road_surf(car_total):
    car_conds = (car_total['Road_Surface_Conditions'].value_counts())
    # car_conds.plot(kind='pie', y='Road_Surface_Conditions', autopct='%1.1f%%',fontsize=10)
    car_conds.plot(kind='bar')
    plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
    plt.show()

pie_chart_road_surf(car_total)

# plot by weather
def pie_chart_weather(car_total):
    car_weather = car_total['Weather_Conditions'].value_counts()
    car_weather.plot(kind='bar', y='Weather_Conditions')#, autopct='%1.1f%%', fontsize=10)
    # plt.show()

pie_chart_weather(car_total)




# 6. Create a predictive model to evaluate the probability of car accidents
# accident by each hour
# def plot_car_time(car_total):
#     n_hours = 24
#     car_time = np.zeros(n_hours)
#     for time in range(n_hours):
#         car_time[time] =
#     return car_time
def plot_by_hour(car_total):
    pd_hour = pd.to_datetime(car_total['Time'], format = '%H:%M').dt.hour
    car_time = pd_hour.value_counts().sort_index()
# car_time.plot(kind='line')
# car_time = plot_car_time(car_total)
    plt.plot(car_time, '.--')
    plt.show()

plot_by_hour(car_total)
