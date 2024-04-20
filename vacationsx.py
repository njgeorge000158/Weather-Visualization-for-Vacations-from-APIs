#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
#
#  File Name:  vacationsx.py 
#
#  File Description:
#      This Python script, vacationsx.py, provides functions for completing tasks 
#      associated with the Jupyter Notebook, vacations.ipynb. Here is the list:
#      
#  set_vacation_temperature_range
#  set_vacation_humidity_range
#  set_vacation_cloudiness_range
#  set_vacation_wind_speed_range
#
#  update_dataframe_location
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

import pandas as pd

from weather_api_keys import geoapify_key

pd.options.mode.chained_assignment = None


# In[2]:


CONSTANT_LOCAL_FILE_NAME = 'vacationsx.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_temperature_range
 #
 #  Function Description:
 #      This subroutine sets the vacation temperature range in Fahrenheit.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer minimum_temperature_integer
 #                          The parameter is the minimum vacation maximum temperature.
 #  integer maximum_temperature_integer
 #                          The parameter is the maximum vacation maximum temperature.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/26/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_vacation_temperature_range \
        (minimum_temperature_integer,
         maximum_temperature_integer):
    
    minimum_temperature_integer = int(minimum_temperature_integer)
        
    maximum_temperature_integer = int(maximum_temperature_integer)
        
        
    if minimum_temperature_integer < weather_constants.CONSTANT_MINIMUM_TEMPERATURE:
            
        minimum_temperature_integer = weather_constants.CONSTANT_MINIMUM_TEMPERATURE
            
    if maximum_temperature_integer > weather_constants.CONSTANT_MAXIMUM_TEMPERATURE:
            
        maximum_temperature_integer = weather_constants.CONSTANT_MAXIMUM_TEMPERATURE

    if minimum_temperature_integer > maximum_temperature_integer:

        minimum_temperature_integer, maximum_temperature_integer \
            = maximum_temperature_integer, minimum_temperature_integer
            
            
    weather_constants.weather_conditions_dictionary['temperature_range'][0] \
        = minimum_temperature_integer
        
    weather_constants.weather_conditions_dictionary['temperature_range'][1] \
        = maximum_temperature_integer


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_humidity_range
 #
 #  Function Description:
 #      This function sets the vacation humidity range.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer minimum_humidity_integer
 #                          The parameter is the minimum vacation humidity.
 #  integer maximum_humidity_integer
 #                          The parameter is the maximum vacation humidity.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/26/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_vacation_humidity_range \
        (minimum_humidity_integer,
         maximum_humidity_integer):

    minimum_humidity_integer = int(minimum_humidity_integer)
        
    maximum_humidity_integer = int(maximum_humidity_integer)
        
        
    if minimum_humidity_integer < weather_constants.CONSTANT_MINIMUM_HUMIDITY:
            
        minimum_humidity_integer = weather_constants.CONSTANT_MINIMUM_HUMIDITY
            
    if maximum_humidity_integer > weather_constants.CONSTANT_MAXIMUM_HUMIDITY:
            
        maximum_humidity_integer = weather_constants.CONSTANT_MAXIMUM_HUMIDITY
            
    if minimum_humidity_integer > maximum_humidity_integer:

        minimum_humidity_integer, maximum_humidity_integer \
            = maximum_humidity_integer, minimum_humidity_integer
        
            
    weather_constants.weather_conditions_dictionary['humidity_range'][0] \
        = minimum_humidity_integer
        
    weather_constants.weather_conditions_dictionary['humidity_range'][1] \
        = maximum_humidity_integer


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_cloudiness_range
 #
 #  Function Description:
 #      This function sets the vacation cloudiness range.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer minimum_cloudiness_integer
 #                          The parameter is the minimum vacation cloudiness.
 #  integer maximum_cloudiness_integer
 #                          The parameter is the maximum vacation cloudiness.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/26/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_vacation_cloudiness_range \
        (minimum_cloudiness_integer,
         maximum_cloudiness_integer):

    minimum_cloudiness_integer = int(minimum_cloudiness_integer)
        
    maximum_cloudiness_integer = int(maximum_cloudiness_integer)
        
        
    if minimum_cloudiness_integer < weather_constants.CONSTANT_MINIMUM_CLOUDINESS:
            
        minimum_cloudiness_integer = weather_constants.CONSTANT_MINIMUM_CLOUDINESS
            
    if maximum_cloudiness_integer > weather_constants.CONSTANT_MAXIMUM_CLOUDINESS:
            
        maximum_cloudiness_integer = weather_constants.CONSTANT_MAXIMUM_CLOUDINESS
            
    if minimum_cloudiness_integer > maximum_cloudiness_integer:

        minimum_cloudiness_integer, maximum_cloudiness_integer \
            = maximum_cloudiness_integer, minimum_cloudiness_integer
            
            
    weather_constants.weather_conditions_dictionary['cloudiness_range'][0] \
        = minimum_cloudiness_integer
        
    weather_constants.weather_conditions_dictionary['cloudiness_range'][1] \
        = maximum_cloudiness_integer


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  set_vacation_wind_speed_range
 #
 #  Function Description:
 #      This function sets the vacation wind speed range.
 #
 #
 #  Return Type: n/a
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  integer minimum_wind_speed_integer
 #                          The parameter is the minimum vacation wind speed.
 #  integer maximum_wind_speed_integer
 #                          The parameter is the maximum vacation wind speed.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/26/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def set_vacation_wind_speed_range \
        (minimum_wind_speed_integer,
         maximum_wind_speed_integer):

    minimum_wind_speed_integer = int(minimum_wind_speed_integer)
        
    maximum_wind_speed_integer = int(maximum_wind_speed_integer)
        
        
    if minimum_wind_speed_integer < weather_constants.CONSTANT_MINIMUM_WIND_SPEED:
            
        minimum_wind_speed_integer = weather_constants.CONSTANT_MINIMUM_WIND_SPEED
            
    if maximum_wind_speed_integer > weather_constants.CONSTANT_MAXIMUM_WIND_SPEED:
            
        maximum_wind_speed_integer = weather_constants.CONSTANT_MAXIMUM_WIND_SPEED
        
    if minimum_wind_speed_integer > maximum_wind_speed_integer:

        minimum_wind_speed_integer, maximum_wind_speed_integer \
            = maximum_wind_speed_integer, minimum_wind_speed_integer

        
    weather_constants.weather_conditions_dictionary['wind_speed_range'][0] \
        = minimum_wind_speed_integer
        
    weather_constants.weather_conditions_dictionary['wind_speed_range'][1] \
        = maximum_wind_speed_integer


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  update_dataframe_location
 #
 #  Function Description:
 #      This function takes a dataframe of vacation data, populates the location name 
 #      column, and returns the updated dataframe to the caller.
 #
 #
 #  Return Type: dataframe
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  dataframe
 #          input_dataframe The parameter is the input dataframe.
 #  string  column_name_string     
 #                          The parameter is the location column name in the dataframe.
 #  string  category_string The parameter is a search category.
 #  integer search_radius_integer  
 #                          The parameter is the search radius in feet.
 #  integer result_limit_integer   
 #                          The parameter is a limit on the number of results.
 #  string  language_string
 #                          The parameter is the language designation for the search.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/26/2023          Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def update_dataframe_location \
        (input_dataframe,
         column_name_string,
         category_string = 'accommodation.hotel',
         search_radius_integer = 10000,
         result_limit_integer = 20,
         language_string = 'en'):
    
    parameters_dictionary \
        = {'categories': [category_string],
           'filter': '',
           'bias': '',
           'limit': result_limit_integer,
           'lang': language_string,
           'apiKey': geoapify_key}

            
    if category_string == 'accommodation.hotel':
        
        category_name_string = 'hotel'
    
    elif category_string == 'catering.restaurant':
        
        category_name_string = 'restaurant'
        
    elif category_string == 'tourism.attraction':
        
        category_name_string = 'tourism attraction'
        
    else: return input_dataframe
        
    
    logx.print_and_log_text \
        (f'STARTING {category_name_string.upper()} SEARCH...\n\n')

             
    city_name_string_list = []

    location_name_string_list = []


    for index, row in input_dataframe.iterrows():

        longitude_float = input_dataframe.at[index, 'longitude']
        
        latitude_float = input_dataframe.at[index, 'latitude']
        
    
        parameters_dictionary['filter'] \
            = f'circle:{longitude_float},{latitude_float},{search_radius_integer}'
             
        parameters_dictionary['bias'] \
            = f'proximity:{longitude_float},{latitude_float}'
    

        url_string = 'https://api.geoapify.com/v2/places'
    
        
        response_dictionary \
            = requests.get(url = url_string, params = parameters_dictionary).json()
        
        if len(response_dictionary['features']) <= 0:
        
            continue
        
        
        for index, location in enumerate(response_dictionary['features']):
        
            try:
                
                location_name_string = location['properties']['name']

                location_name_string_list.append(location_name_string)
                
                logx.print_and_log_text \
                    (f'Located the following {category_name_string}...' \
                     + f'{location_name_string} ' \
                     + f"in {input_dataframe.at[index, 'city']}, " \
                     + f"{input_dataframe.at[index, 'country']}\n\n")

                break
            
            except:
             
                continue
        
        city_name_string_list.append(row['city'])

            
    temp_dataframe \
        = input_dataframe.apply \
            (lambda x: x[input_dataframe['city'].isin(city_name_string_list)])
            
    temp_dataframe.reset_index(drop = True, inplace = True)
             
    temp_dataframe[column_name_string] = pd.Series(location_name_string_list)
    
    
    logx.print_and_log_text(f'{category_name_string.upper()} SEARCH COMPLETE...\n\n')
            
             
    return temp_dataframe


# In[ ]:




