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

|&rarr; [./weather_constants.py](./weather_constants.py)

|&rarr; [./weather.ipynb](./weather.ipynb)

|&rarr; [./weatherx.py](./weatherx.py)

|&rarr; [./images/](./images/)

  &emsp; |&rarr; [./images/README.md](./images/README.md)

  &emsp; |&rarr; [./images/vacationsFigure13CityWeatherLocations.png](./images/vacationsFigure13CityWeatherLocations.png)
  
  &emsp; |&rarr; [./images/vacationsFigure24VacationLocations.png](./images/vacationsFigure24VacationLocations.png)
  
  &emsp; |&rarr; [./images/vacationsFigure34HotelLocations.png](./images/vacationsFigure34HotelLocations.png)
  
  &emsp; |&rarr; [./images/vacationsFigure44RestaurantLocations.png](./images/vacationsFigure44RestaurantLocations.png)
  
  &emsp; |&rarr; [./images/vacationsFigure54TourismAttractionLocations.png](./images/vacationsFigure54TourismAttractionLocations.png)
  
  &emsp; |&rarr; [./images/vacationsTable12CityWeatherInformation.png](./images/vacationsTable12CityWeatherInformation.png)
  
  &emsp; |&rarr; [./images/vacationsTable23VacationLocations.png](./images/vacationsTable23VacationLocations.png)
  
  &emsp; |&rarr; [./images/vacationsTable33HotelLocations.png](./images/vacationsTable33HotelLocations.png)

  &emsp; |&rarr; [./images/vacationsTable43RestaurantLocations.png](./images/vacationsTable43RestaurantLocations.png)
  
  &emsp; |&rarr; [./images/vacationsTable53TourismAttractionLocations.png](./images/vacationsTable53TourismAttractionLocations.png)
  
  &emsp; |&rarr; [./images/weatherFigure15CityWeatherLocations.png](./images/weatherFigure15CityWeatherLocations.png)
  
  &emsp; |&rarr; [./images/weatherFigure19ImportedCityWeatherLocations.png](./images/weatherFigure19ImportedCityWeatherLocations.png)

  &emsp; |&rarr; [./images/weatherFigure22HumidityVsLatitudeScatterPlot.png](./images/weatherFigure22HumidityVsLatitudeScatterPlot.png)
  
  &emsp; |&rarr; 
[./images/weatherFigure23CloudinessVsLatitudeScatterPlot.png](./images/weatherFigure23CloudinessVsLatitudeScatterPlot.png)

  &emsp; |&rarr; [./images/weatherFigure24WindSpeedvsLatitudeScatterPlot.png](./images/weatherFigure24WindSpeedvsLatitudeScatterPlot.png)
  
  &emsp; |&rarr; [./images/weatherFigure31CityWeatherLocationsNorthernHemisphere.png](./images/weatherFigure31CityWeatherLocationsNorthernHemisphere.png)
  
  &emsp; |&rarr; [./images/weatherFigure32CityWeatherLocationsSouthernHemisphere.png](./images/weatherFigure32CityWeatherLocationsSouthernHemisphere.png)
  
  &emsp; |&rarr; [./images/weatherFigure211TemperatureVsLatitudeScatterPlot.png](./images/weatherFigure211TemperatureVsLatitudeScatterPlot.png)
  
  &emsp; |&rarr; [./images/weatherFigure212TemperatureVsLatitudeScatterPlotwRegression.png](./images/weatherFigure212TemperatureVsLatitudeScatterPlotwRegression.png)
  
  &emsp; |&rarr; [./images/weatherFigure331TemperaturevsLatitudeNorthernHemisphere.png](./images/weatherFigure331TemperaturevsLatitudeNorthernHemisphere.png)
  
  &emsp; |&rarr; [./images/weatherFigure332TemperaturevsLatitudeSouthernHemisphere.png](./images/weatherFigure332TemperaturevsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure341HumidityvsLatitudeNorthernHemisphere.png](./images/weatherFigure341HumidityvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure342HumidityvsLatitudeSouthernHemisphere.png](./images/weatherFigure342HumidityvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure351CloudinessvsLatitudeNorthernHemisphere.png](./images/weatherFigure351CloudinessvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure352CloudinessvsLatitudeSouthernHemisphere.png](./images/weatherFigure352CloudinessvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure361WindSpeedvsLatitudeNorthernHemisphere.png](./images/weatherFigure361WindSpeedvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure362WindSpeedvsLatitudeSouthernHemisphere.png](./images/weatherFigure362WindSpeedvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherTable14CityWeatherInformation.png](./images/weatherTable14CityWeatherInformation.png)

  &emsp; |&rarr; [./images/weatherTable18ImportedCityWeatherInformation.png](./images/weatherTable18ImportedCityWeatherInformation.png)

|&rarr; [./logs/](./logs/)

  &emsp; |&rarr; [./logs/20240420vacations_log.txt](./logs/20240420vacations_log.txt)

  &emsp; |&rarr; [./logs/20240420weather_log.txt](./logs/20240420weather_log.txt)

|&rarr; [./resources/](./resources/)

  &emsp; |&rarr; [./resources/cities_weather.csv](./resources/cities_weather.csv)

  &emsp; |&rarr; [./resources/README.md](./resources/README.md)

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

Nicholas J. George © 2023. All Rights Reserved.
