#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  weather_constants.py
 #
 #  File Description:
 #      This Python script, weather_constants.py, contains generic Python constants
 #      for completing tasks in the Jupyter Notebook, weather.ipynb.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/24/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'weather_constants.py'


# In[3]:


CONSTANT_OPEN_WEATHERMAP_WEBSITE = 'http://api.openweathermap.org'

CONSTANT_API_DATA_UNITS = 'imperial'

CONSTANT_SET_OF_CITIES = 50

CONSTANT_WEATHER_DATA_FILE_PATH = './resources/cities_weather.csv'

CONSTANT_WEATHER_DATA_FILE_INDEX_NAME = 'city_id'


CONSTANT_MINIMUM_TEMPERATURE = 0

CONSTANT_MAXIMUM_TEMPERATURE = 120


CONSTANT_MINIMUM_HUMIDITY = 0

CONSTANT_MAXIMUM_HUMIDITY = 100


CONSTANT_MINIMUM_CLOUDINESS = 0

CONSTANT_MAXIMUM_CLOUDINESS = 100


CONSTANT_MINIMUM_WIND_SPEED = 0

CONSTANT_MAXIMUM_WIND_SPEED = 100


weather_conditions_dictionary \
    = {'temperature_range': [CONSTANT_MINIMUM_TEMPERATURE, CONSTANT_MAXIMUM_TEMPERATURE],
       'humidity_range': [CONSTANT_MINIMUM_HUMIDITY, CONSTANT_MAXIMUM_HUMIDITY],
       'cloudiness_range': [CONSTANT_MINIMUM_CLOUDINESS, CONSTANT_MAXIMUM_CLOUDINESS],
       'wind_speed_range': [CONSTANT_MINIMUM_WIND_SPEED, CONSTANT_MAXIMUM_WIND_SPEED]}

