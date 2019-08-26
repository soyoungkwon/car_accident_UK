
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
# from arcgis.gis import GIS

# file name & path name
dir_curr = os.getcwd()
dir_car = os.listdir(dir_curr)[2]
accident_files = ['accidents_2005_to_2007.csv','accidents_2009_to_2011.csv', 'accidents_2012_to_2014.csv']


# load csv data
car_list = []
for file in accident_files:
    file_fullname = dir_car + '/' + file
    car_one = pd.read_csv(file_fullname, index_col=None, header=0)
    car_list.append(car_one)

car_total = pd.concat(car_list, axis=0, ignore_index=True)


# 1. Identify the areas with the most accidents.
# visualize accidents in the map
def map_overlay(car_total):
    car_total.plot(kind='scatter', x='Longitude', y='Latitude', c = 'Urban_or_Rural_Area', s=3)#, cmap = plt.get_cmap("jet"))
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



# 3. Accidents across different seasons
a = pd.to_datetime(car_total['Date'])
car_total['Month'] = a.dt.strftime('%m').astype(str)
car_total['Year'] = a.dt.strftime('%Y').astype(str)

# === Month ===== #
def plot_by_month(car_total):
    # n_month = 12
    car_month = car_total['Month'].value_counts().sort_index()
    n_month = len(car_month)
    plt.bar(np.arange(n_month), car_month)
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
    # plt.show()
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


# road conditions
# car_conditions = []

def plot_road_conds(car_total):
    road_conds = car_total['Road_Surface_Conditions'].value_counts().index
    # n_road_conds = len(road_conds)
    car_road_conds = car_total['Road_Surface_Conditions'].value_counts()
    car_road_conds.plot(kind='bar', y='Road_Surface_Conditions')
    plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
plot_road_conds(car_total)


# 6. Create a predictive model to evaluate the probability of car accidents car_total['Accident_Severity'].value_counts()
car_total['Number_of_Casualties'].value_counts()
# accident by each hour
def car_time(car_total):
    n_hours = 24
    car_time = np.zeros(n_hours)
    for time in range(n_hours):
        car_time[time]

pd_hour = pd.to_datetime(car_total['Time'], format = '%H:%M').dt.hour
car_time = pd_hour.value_counts().sort_index()
car_time.plot(kind='line')


car_month = car_total['Month'].value_counts().sort_index()
car_month.plot(kind='bar')
