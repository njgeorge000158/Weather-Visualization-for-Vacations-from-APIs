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

  &emsp; |&rarr; [./images/vacationsFigure13CityWeatherLocations.html](./images/vacationsFigure13CityWeatherLocations.html)
  
  &emsp; |&rarr; [./images/vacationsFigure24VacationLocations.html](./images/vacationsFigure24VacationLocations.html)
  
  &emsp; |&rarr; [./images/vacationsFigure34HotelLocations.html](./images/vacationsFigure34HotelLocations.html)
  
  &emsp; |&rarr; [./images/vacationsFigure44RestaurantLocations.html](./images/vacationsFigure44RestaurantLocations.html)
  
  &emsp; |&rarr; [./images/vacationsFigure54TouristAttractionLocations.html](./images/vacationsFigure54TourismAttractionLocations.html)
  
  &emsp; |&rarr; [./images/vacationsTable12CityWeatherInformation.png](./images/vacationsTable12CityWeatherInformation.png)
  
  &emsp; |&rarr; [./images/vacationsTable23VacationLocations.png](./images/vacationsTable23VacationLocations.png)
  
  &emsp; |&rarr; [./images/vacationsTable33HotelLocations.png](./images/vacationsTable33HotelLocations.png)

  &emsp; |&rarr; [./images/vacationsTable43RestaurantLocations.png](./images/vacationsTable43RestaurantLocations.png)
  
  &emsp; |&rarr; [./images/vacationsTable53TouristAttractionLocations.png](./images/vacationsTable53TourismAttractionLocations.png)
  
  &emsp; |&rarr; [./images/weatherFigure15CityWeatherLocations.html](./images/weatherFigure15CityWeatherLocations.html)
  
  &emsp; |&rarr; [./images/weatherFigure19ImportedCityWeatherLocations.html](./images/weatherFigure19ImportedCityWeatherLocations.html)

  &emsp; |&rarr; [./images/weatherFigure21TemperatureVsLatitudeScatterPlotwRegression.png](./images/weatherFigure21TemperatureVsLatitudeScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/weatherFigure22HumidityVsLatitudeScatterPlotwRegression.png](./images/weatherFigure22HumidityVsLatitudeScatterPlotwRegression.png)
  
  &emsp; |&rarr; 
[./images/weatherFigure23HumidityVsCloudinessScatterPlotwRegression.png](./images/weatherFigure23HumidityVsCloudinessScatterPlotwRegression.png)

  &emsp; |&rarr; [./images/weatherFigure24WindSpeedvsLatitudeScatterPlotwRegression.png](./images/weatherFigure24WindSpeedvsLatitudeScatterPlotwRegression.png)
  
  &emsp; |&rarr; [./images/weatherFigure31CityWeatherLocationsNorthernHemisphere.html](./images/weatherFigure31CityWeatherLocationsNorthernHemisphere.html)
  
  &emsp; |&rarr; [./images/weatherFigure32CityWeatherLocationsSouthernHemisphere.html](./images/weatherFigure32CityWeatherLocationsSouthernHemisphere.html)

  &emsp; |&rarr; [./images/weatherFigure33CityWeatherLocationsEasternHemisphere.html](./images/weatherFigure33CityWeatherLocationsEasternHemisphere.html)
  
  &emsp; |&rarr; [./images/weatherFigure34CityWeatherLocationsWesternHemisphere.html](./images/weatherFigure34CityWeatherLocationsWesternHemisphere.html)
  
  &emsp; |&rarr; [./images/weatherFigure411TemperaturevsLatitudeNorthernHemisphere.png](./images/weatherFigure411TemperaturevsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure412TemperaturevsLatitudeSouthernHemisphere.png](./images/weatherFigure412TemperaturevsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure413TemperaturevsLatitudeEasternHemisphere.png](./images/weatherFigure413TemperaturevsLatitudeEasternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure414TemperaturevsLatitudeWesternHemisphere.png](./images/weatherFigure414TemperaturevsLatitudeWesternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure421HumidityvsLatitudeNorthernHemisphere.png](./images/weatherFigure421HumidityvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure422HumidityvsLatitudeSouthernHemisphere.png](./images/weatherFigure422HumidityvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure423HumidityvsLatitudeEasternHemisphere.png](./images/weatherFigure423HumidityvsLatitudeEasternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure424HumidityvsLatitudeWesternHemisphere.png](./images/weatherFigure424HumidityvsLatitudeWesternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure431CloudinessvsLatitudeNorthernHemisphere.png](./images/weatherFigure431CloudinessvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure432CloudinessvsLatitudeSouthernHemisphere.png](./images/weatherFigure432CloudinessvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure433CloudinessvsLatitudeEasternHemisphere.png](./images/weatherFigure433CloudinessvsLatitudeEasternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure434CloudinessvsLatitudeWesternHemisphere.png](./images/weatherFigure434CloudinessvsLatitudeWesternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure441WindSpeedvsLatitudeNorthernHemisphere.png](./images/weatherFigure441WindSpeedvsLatitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure442WindSpeedvsLatitudeSouthernHemisphere.png](./images/weatherFigure442WindSpeedvsLatitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure443WindSpeedvsLatitudeEasternHemisphere.png](./images/weatherFigure443WindSpeedvsLatitudeEasternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure444WindSpeedvsLatitudeWesternHemisphere.png](./images/weatherFigure444WindSpeedvsLatitudeWesternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure511TemperaturevsLongitudeNorthernHemisphere.png](./images/weatherFigure511TemperaturevsLongitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure512TemperaturevsLongitudeSouthernHemisphere.png](./images/weatherFigure512TemperaturevsLongitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure513TemperaturevsLongitudeEasternHemisphere.png](./images/weatherFigure513TemperaturevsLongitudeEasternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure514TemperaturevsLongitudeWesternHemisphere.png](./images/weatherFigure514TemperaturevsLongitudeWesternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure521HumidityvsLongitudeNorthernHemisphere.png](./images/weatherFigure521HumidityvsLongitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure522HumidityvsLongitudeSouthernHemisphere.png](./images/weatherFigure522HumidityvsLongitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure523HumidityvsLongitudeEasternHemisphere.png](./images/weatherFigure523HumidityvsLongitudeEasternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure524HumidityvsLongitudeWesternHemisphere.png](./images/weatherFigure524HumidityvsLongitudeWesternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure531CloudinessvsLongitudeNorthernHemisphere.png](./images/weatherFigure531CloudinessvsLongitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure532CloudinessvsLongitudeSouthernHemisphere.png](./images/weatherFigure532CloudinessvsLongitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure533CloudinessvsLongitudeEasternHemisphere.png](./images/weatherFigure533CloudinessvsLongitudeEasternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure534CloudinessvsLongitudeWesternHemisphere.png](./images/weatherFigure534CloudinessvsLongitudeWesternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure541WindSpeedvsLongitudeNorthernHemisphere.png](./images/weatherFigure541WindSpeedvsLongitudeNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure542WindSpeedvsLongitudeSouthernHemisphere.png](./images/weatherFigure542WindSpeedvsLongitudeSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure543WindSpeedvsLongitudeEasternHemisphere.png](./images/weatherFigure543WindSpeedvsLongitudeEasternHemisphere.png)

  &emsp; |&rarr; [./images/weatherFigure544WindSpeedvsLongitudeWesternHemisphere.png](./images/weatherFigure544WindSpeedvsLongitudeWesternHemisphere.png)

  &emsp; |&rarr; [./images/weatherTable14CityWeatherInformation.png](./images/weatherTable14CityWeatherInformation.png)

  &emsp; |&rarr; [./images/weatherTable18ImportedCityWeatherInformation.png](./images/weatherTable18ImportedCityWeatherInformation.png)

  &emsp; |&rarr; [./images/weatherTable25CityWeatherCorrelationMatrix.png](./images/weatherTable25CityWeatherCorrelationMatrix.png)

  &emsp; |&rarr; [./images/weatherTable31CityWeatherDataSetNorthernHemisphere.png](./images/weatherTable31CityWeatherDataSetNorthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherTable32CityWeatherInformationSouthernHemisphere.png](./images/weatherTable32CityWeatherInformationSouthernHemisphere.png)

  &emsp; |&rarr; [./images/weatherTable33CityWeatherInformationEasternHemisphere.png](./images/weatherTable33CityWeatherInformationEasternHemisphere.png)

  &emsp; |&rarr; [./images/weatherTable34CityWeatherInformationWesternHemisphere.png](./images/weatherTable34CityWeatherInformationWesternHemisphere.png)

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
