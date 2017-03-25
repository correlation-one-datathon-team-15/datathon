import pandas as pd
import datetime
import numpy as np


Uber_trips_2015 = pd.read_csv('uber_trips_2015.csv', delimiter=',')
#print(Uber_trips_2014.head())
#Uber_trips_2015 = pd.read_csv('uber_trips_2015.csv', delimiter=',')
#bases = pd.read_csv('bases.csv', delimiter=',')
#demographics = pd.read_csv('demographics.csv', delimiter=',')
#geographic = pd.read_csv('geographic.csv', delimiter=',')
#green_trips = pd.read_csv('green_trips.csv', delimiter=',')
#other_fhv_trips = pd.read_csv('other_fhv_trips.csv', delimiter=',')
#yellow_trips_2014_Q2 = pd.read_csv('yellow_trips_2014_Q2.csv', delimiter=',')
#yellow_trips_2014_Q3 = pd.read_csv('yellow_trips_2014_Q3.csv', delimiter=',')
#yellow_trips_2015_Q1 = pd.read_csv('yellow_trips_2015_Q1.csv', delimiter=',')
#yellow_trips_2015_Q2 = pd.read_csv('yellow_trips_2015_Q2.csv', delimiter=',')
#zones = pd.read_csv('zones.csv', delimiter=',')

Uber_trips_2015.pickup_datetime = pd.to_datetime(Uber_trips_2015.pickup_datetime)
#print(Uber_trips_2015.dtypes)

Uber_trips_2015 = Uber_trips_2015.dropna(axis=0)

d1 = datetime.time(5,0,0)
d2 = datetime.time(10,0,0)
#print(d1)
#print(d2)
#print(Uber_trips_2015.shape[0])
#print(Uber_trips_2014.head())
index = pd.DatetimeIndex(Uber_trips_2015['pickup_datetime'])

df = Uber_trips_2015.iloc[index.indexer_between_time('5:00','10:00')]
#print(df)
for row_num in range(df.shape[0]): 
	print(df.iloc[row_num:row_num+1])




