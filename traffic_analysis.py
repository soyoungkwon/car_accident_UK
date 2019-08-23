# import libraries

import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# file name & path name
dir_curr = os.getcwd()
dir_car = os.listdir(dir_curr)[2]
# file_list = os.listdir(dir_car)
accident_files = ['accidents_2005_to_2007.csv','accidents_2009_to_2011.csv', 'accidents_2012_to_2014.csv']

# load csv data
car_list = []
for file in accident_files:
    file_fullname = dir_car + '/' + file
    car_one = pd.read_csv(file_fullname, index_col=None, header=0)
    car_list.append(car_one)

car_total = pd.concat(car_list, axis=0, ignore_index=True)

# plot basic data
car_total.plot(kind='scatter', x='Longitude', y='Latitude',c = 'Urban_or_Rural_Area', s=3, cmap = plt.get_cmap("jet"))
plt.show()

# Urban vs Rural area

bins = np.array([1.0, 1.5, 2.0]) # just two bins
plt.hist(car_total['Urban_or_Rural_Area'], bins, normed=True)
car_total['Urban_or_Rural_Area'].value_counts()

# Road type plot
plt.hist(car_total['Road_Type'])
plt.xticks(rotation=45, horizontalalignment='right', fontweight='light')
plt.show()

# Seasonality check
car_total['Date']
