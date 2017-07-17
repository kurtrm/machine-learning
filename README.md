#Machine Learning
Kurt Maurer

##Purpose
This repo is dedicated to the purpose of learning the data analysis tools available in Python.

## Analyzing Boston Housing Market Data
The Boston data set provides the following information:
   -Per Capita Crime Rate By Town
   -Proportion of residential alnd zoned for lots > 25k sq ft.
   -Proportion of non-retail business acres per town.
   -Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
   -Nitrogen oxides concentration (parts per 10 million)
   -Avg number of rooms per dwelling
   -Proportion of owner-occupied units built prior to 1940
   -Weighted mean of distances to five Boston employment centres
   -Index of accessibility to radial highways
   -Full-value of property-tax rate per $10,000
   -Pupil-teacher ratio by town
   -Proportion of blacks per town 1000(Bk - 0.63)^2
   -Lower status of the population
   -Median value of owner-occupied homes in $1000s

### Goals   
I attempted to glean relationships visually through Matplotlib scatter plots between the following:
-The relationship between per-capita crime rate and the pupil-teacher ratio.  Differentiate between whether or not the suburb is bounded by the Charles River.
-The relationship between the proportion of black citizens and the distance to employment centers in Boston.
-The relationship between median value of owner-occuped homes and nitric oxide concentration along with median home value and the proportion of non-retail business (on the same plot).

### Source
The Boston housing data was provided by the following website:
https://vincentarelbundock.github.io/Rdatasets/datasets.html

## Imperfect Data
I downloaded the Fremont Bridge northbound and southbound bike count data in a csv file. This contains three columns: northbound bike count,
southbound bike count, and the hour of the day. I also downloaded the NOAA precipitation file for the Seattle area and attempted to find a relationship
between precipitation and the number of bikes crossing the bridge. Both contain errors that need to be fixed to be used, or at least to be put into a
datbase.

### Source
seattle.data.gov
NOAA 

