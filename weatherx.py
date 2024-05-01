#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
#
#  File Name:  weatherx.py 
#
#  File Description:
#      This Python script, weatherx.py, provides functions for completing tasks 
#      associated with the Jupyter Notebook, weather.ipynb. Here is the list:
#
#  return_city_weather_styler
#  return_city_names_list
#  return_weather_dataframe
#
#
#  Date            Description                             Programmer
#  ----------      ------------------------------------    ------------------
#  08/26/2023      Initial Development                     Nicholas J. George
#
#******************************************************************************************/

import logx
import weather_constants

import requests

from datetime import datetime
import numpy as np
import pandas as pd

from citipy import citipy
from weather_api_keys import weather_api_key

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'weatherx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  return_city_weather_styler
 #
 #  Function Description:
 #      This function receives a city weather dataframe, formats a copy of it 
 #      as a styler, and returns it to the caller.
 #
 #
 #  Return Type: styler
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe The parameter is the input dataframe.
 #  string  caption_string  The parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/26/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_city_weather_styler \
        (input_dataframe,
         caption_string):

    temp_dataframe = input_dataframe.copy()

    return \
        temp_dataframe \
            .style \
            .set_caption(caption_string) \
            .set_table_styles \
                ([{'selector': 'caption', 
                   'props': [('color', 'black'), 
                             ('font-size', '20px'),
                             ('font-style', 'bold'),
                             ('text-align', 'center')]}]) \
            .set_properties \
                (**{'text-align': 'center',
                    'border': '1.3px solid red',
                    'color': 'blue'}) \
            .format \
                ({'city': pandasx.GENERAL_TEXT_FORMAT,
                  'longitude': pandasx.FLOAT_FORMAT,
                  'latitude': pandasx.FLOAT_FORMAT,
                  'temperature': pandasx.TEMPERATURE_FLOAT_FORMAT,
                  'humidity': pandasx.PERCENT_INTEGER_FORMAT,
                  'cloudiness': pandasx.PERCENT_INTEGER_FORMAT,
                  'wind_speed': pandasx.FLOAT_FORMAT,
                  'country': pandasx.GENERAL_TEXT_FORMAT}) \
            .highlight_max \
                (subset = ['temperature', 'humidity', 'cloudiness', 'wind_speed'],
                 color = 'lime') \
            .highlight_min \
                (subset = ['temperature', 'humidity', 'cloudiness', 'wind_speed'],
                 color = 'yellow') \
            .hide()


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  return_city_names_list
 #
 #  Function Description:
 #      This function returns a list of cities from the API, citypy.
 #
 #
 #  Return Type: list
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/26/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/
    
def return_city_names_list():

    city_names_string_list = []

        
    latitude_range_float_tuple = (-90.0, 90.0)

    longitude_range_float_tuple = (-180.0, 180.0)


    random_latitude_float_array \
        = np.random.uniform \
            (latitude_range_float_tuple[0], 
             longitude_range_float_tuple[1], 
             size = weather_constants.CONSTANT_CITY_NAME_COUNT)

    random_longitude_float_array \
        = np.random.uniform \
            (longitude_range_float_tuple[0], 
             longitude_range_float_tuple[1], 
             size = weather_constants.CONSTANT_CITY_NAME_COUNT)


    latitude_longitude_float_tuple_list \
        = zip(random_latitude_float_array, random_longitude_float_array)


    for latitude_longitude_float_tuple in latitude_longitude_float_tuple_list:
    
        city_name_string \
            = citipy.nearest_city \
                (latitude_longitude_float_tuple[0], 
                 latitude_longitude_float_tuple[1]) \
                    .city_name
    
        if city_name_string not in city_names_string_list:
                
            city_names_string_list.append(city_name_string)
        
        
    return city_names_string_list


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  return_weather_dataframe
 #
 #  Function Description:
 #      This function returns weather information from the open weathermap website 
 #      using the requests module and a list of cities.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  string list
 #          city_names_string_list
 #                          This parameter is a list of city names.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/26/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def return_weather_dataframe(city_names_string_list):
    
    query_url_string \
        = f'{weather_constants.CONSTANT_OPEN_WEATHERMAP_WEBSITE}/data/2.5/weather?appid=' \
          + f'{weather_api_key}&units={weather_constants.CONSTANT_API_DATA_UNITS}&q='

    
    city_weather_dictionary_list = []

    record_count_integer = 0
    
    set_of_cities_count_integer = 1

    
    logx.print_and_log_text('\nCITY WEATHER DATA RETRIEVAL BEGINS...\n')


    for index, city_name in enumerate(city_names_string_list):
    
        if index % weather_constants.CONSTANT_SET_OF_CITIES == 0 \
           and index >= weather_constants.CONSTANT_SET_OF_CITIES:
        
            record_count_integer = 0
        
            set_of_cities_count_integer += 1

            
        logx.print_and_log_text \
            (f'\nProcessing record #{record_count_integer + 1} ' \
             + f'of set {set_of_cities_count_integer} for city, {city_name}.')
            

        city_url_string = query_url_string + city_name
            
        record_count_integer += 1
        
        
        try:

            city_weather_dictionary = requests.get(city_url_string).json()

            
            city_latitude_float = city_weather_dictionary['coord']['lat']

            city_longitude_float = city_weather_dictionary['coord']['lon']
        
            city_temperature_float = city_weather_dictionary['main']['temp']

            city_humidity_integer = city_weather_dictionary['main']['humidity']

            city_clouds_integer = city_weather_dictionary['clouds']['all']

            city_wind_speed_float = city_weather_dictionary['wind']['speed']
        
            city_country_string = city_weather_dictionary['sys']['country']

            city_datetime = datetime.fromtimestamp(city_weather_dictionary['dt'])
         

            city_weather_dictionary_list.append \
                ({'city': city_name, 
                  'latitude': city_latitude_float, 
                  'longitude': city_longitude_float, 
                  'temperature': city_temperature_float,
                  'humidity': city_humidity_integer,
                  'cloudiness': city_clouds_integer,
                  'wind_speed': city_wind_speed_float,
                  'country': city_country_string,
                  'date_time': city_datetime})
        
        except:
        
            logx.print_and_log_text \
                (f'\nThe script did not find the city, {city_name}. Skipping...')

        
    logx.print_and_log_text('\nCITY WEATHER DATA RETRIEVAL IS COMPLETE.') 
    
    city_weather_dataframe =  pd.DataFrame(city_weather_dictionary_list)

    city_weather_dataframe.index.name \
        = weather_constants.CONSTANT_WEATHER_DATA_FILE_INDEX_NAME
    
    
    return city_weather_dataframe


# In[ ]:




