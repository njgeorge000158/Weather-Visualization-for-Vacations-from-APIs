# **Weather Visualization for Ideal vacations from APIs**

----

### **Installation:**

----

If the computer has Anaconda, Jupyter Notebook, and a recent version of Python, the IPython notebook already has the following dependencies installed: datetime, io, json, matplotlib, numpy, pandas, pathlib, os, pandas, requests, requests_html, and scipy.

In addition to those modules, the Jupyter Notebook requires the following to execute: holoviews, hvplot, geoviews, geopy, aspose-words, dataframe-image, citypy.

Here are the requisite Terminal commands for the installation of these peripheral modules:

python3 -m pip install holoviews

python3 -m pip install hvplot

python3 -m pip install geoviews

python3 -m pip install geopy

python3 -m pip install aspose-words

python3 -m pip install dataframe-image

python3 -m pip install citypy

----

### **Usage:**

----

The IPython notebook, weather.ipynb, generates the CSV file, cities_weather.csv, which acts as input to vacations.ipynb.  These IPython Notebooks must have the following Python scripts in the same folder with it:

logx_constants.py

logx.py

mathx.py

matplotlibx.py

pandasx_constants.py

pandasx.py

vacationsx.py

weather_api_keys.py

weather_constants.py

weatherx.py

If the folders, logs and images, are not present, an IPython notebook will create them.  The folder, resources, contains the output file from weather.ipynb, cities_weather.csv, which is the input file for vacations.ipynb; the folder, logs, contains log files from testing the IPython Notebooks; and the folder, images, has the PNG and HTML files of the IPython Notebooks' tables and plots.

To place the IPython notebook in Log Mode or Image Mode set the parameter for the appropriate subroutine in coding cell #2 to True. If the program is in Log Mode, it writes log information to files in the folder, logs. If the program is in Image Mode, it writes all dataframes, hvplot maps, and matplotlib plots to PNG files in the folder, images.

----

### **Resource Summary:**

----

#### Source code

weather.ipynb, vacations.ipynb, logx_constants.py, logx.py, mathx.py, matplotlibx.py, pandasx_constants.py, pandasx.py, vacationsx.py, weather_api_keys.py, weather_constants.py, weatherx.py

#### Input files

cities_weather.csv (vacations.ipynb)

#### Output files

cities_weather.csv (weather.ipynb)

#### SQL script

n/a

#### Software

Jupyter Notebook, Pandas, Python 3.11.4

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

----

### **GitHub Repository Branches:**

----

#### main branch 

|&rarr; [./logx_constants.py](./logx_constants.py)

|&rarr; [./logx.py](./logx.py)

|&rarr; [./mathx.py](./mathx.py)

|&rarr; [./matplotlibx.py](./matplotlibx.py)

|&rarr; [./pandasx_constants.py](./pandasx_constants.py)

|&rarr; [./pandasx.py](./pandasx.py)

|&rarr; [./README.md](./README.md)

|&rarr; [./README.TECHNICAL.md](./README.TECHNICAL.md)

|&rarr; [./table-of-contents.md](./table-of-contents.md)

|&rarr; [./vacations.ipynb](./vacations.ipynb)

|&rarr; [./vacationsx.py](./vacationsx.py)

|&rarr; [./WeatherPy.ipynb](./WeatherPy.ipynb)

|&rarr; [./WeatherPyAPIFunctions.py](./WeatherPyAPIFunctions.py)

|&rarr; [./WeatherPyAPIKeys.py](./WeatherPyAPIKeys.py)

|&rarr; [./WeatherPyConstants.py](./WeatherPyConstants.py)

|&rarr; [./WeatherPyFunctions.py](./WeatherPyFunctions.py)

|&rarr; [./Images/](./Images/)

  &emsp; |&rarr; [./Images/README.md](./Images/README.md)

  &emsp; |&rarr; [./Images/VacationPyFigure13CityWeatherLocations.png](./Images/VacationPyFigure13CityWeatherLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyFigure24VacationLocations.png](./Images/VacationPyFigure24VacationLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyFigure34HotelLocations.png](./Images/VacationPyFigure34HotelLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyFigure44RestaurantLocations.png](./Images/VacationPyFigure44RestaurantLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyFigure54TourismAttractionLocations.png](./Images/VacationPyFigure54TourismAttractionLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyTable12CityWeatherInformation.png](./Images/VacationPyTable12CityWeatherInformation.png)
  
  &emsp; |&rarr; [./Images/VacationPyTable23VacationLocations.png](./Images/VacationPyTable23VacationLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyTable33HotelLocations.png](./Images/VacationPyTable33HotelLocations.png)

  &emsp; |&rarr; [./Images/VacationPyTable43RestaurantLocations.png](./Images/VacationPyTable43RestaurantLocations.png)
  
  &emsp; |&rarr; [./Images/VacationPyTable53TourismAttractionLocations.png](./Images/VacationPyTable53TourismAttractionLocations.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure15CityWeatherLocations.png](./Images/WeatherPyFigure15CityWeatherLocations.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure19ImportedCityWeatherLocations.png](./Images/WeatherPyFigure19ImportedCityWeatherLocations.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure22HumidityVsLatitudeScatterPlot.png](./Images/WeatherPyFigure22HumidityVsLatitudeScatterPlot.png)
  
  &emsp; |&rarr; 
[./Images/WeatherPyFigure23CloudinessVsLatitudeScatterPlot.png](./Images/WeatherPyFigure23CloudinessVsLatitudeScatterPlot.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure24WindSpeedvsLatitudeScatterPlot.png](./Images/WeatherPyFigure24WindSpeedvsLatitudeScatterPlot.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure31CityWeatherLocationsNorthernHemisphere.png](./Images/WeatherPyFigure31CityWeatherLocationsNorthernHemisphere.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure32CityWeatherLocationsSouthernHemisphere.png](./Images/WeatherPyFigure32CityWeatherLocationsSouthernHemisphere.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure211TemperatureVsLatitudeScatterPlot.png](./Images/WeatherPyFigure211TemperatureVsLatitudeScatterPlot.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure212TemperatureVsLatitudeScatterPlotwRegression.png](./Images/WeatherPyFigure212TemperatureVsLatitudeScatterPlotwRegression.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure331TemperaturevsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure331TemperaturevsLatitudeNorthernHemisphere.png)
  
  &emsp; |&rarr; [./Images/WeatherPyFigure332TemperaturevsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure332TemperaturevsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure341HumidityvsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure341HumidityvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure342HumidityvsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure342HumidityvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure351CloudinessvsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure351CloudinessvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure352CloudinessvsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure352CloudinessvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure361WindSpeedvsLatitudeNorthernHemisphere.png](./Images/WeatherPyFigure361WindSpeedvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyFigure362WindSpeedvsLatitudeSouthernHemisphere.png](./Images/WeatherPyFigure362WindSpeedvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./Images/WeatherPyTable14CityWeatherInformation.png](./Images/WeatherPyTable14CityWeatherInformation.png)

  &emsp; |&rarr; [./Images/WeatherPyTable18ImportedCityWeatherInformation.png](./Images/WeatherPyTable18ImportedCityWeatherInformation.png)

|&rarr; [./Logs/](./Logs/)

  &emsp; |&rarr; [./Logs/20231001VacationPyDebug.txt](./Logs/20231001VacationPyDebug.txt)

  &emsp; |&rarr; [./Logs/20231001VacationPyLog.txt](./Logs/20231001VacationPyLog.txt)

  &emsp; |&rarr; [./Logs/20231001WeatherPyDebug.txt](./Logs/20231001WeatherPyDebug.txt)

  &emsp; |&rarr; [./Logs/20231001WeatherPyLog.txt](./Logs/20231001WeatherPyLog.txt)

  &emsp; |&rarr; [./Logs/README.md](./Logs/README.md)

|&rarr; [./Resources/](./Resources/)

  &emsp; |&rarr; [./Resources/CitiesWeather.csv](./Resources/CitiesWeather.csv)

  &emsp; |&rarr; [./Resources/README.md](./Resources/README.md)

----

### **References:**

----

[Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

[Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

[Python Documentation](https://docs.python.org/3/contents.html)

----

### **Authors and Acknowledgment:**

----

### Copyright

N. James George © 2023. All Rights Reserved.
