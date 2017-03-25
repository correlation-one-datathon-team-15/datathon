import gmplot
import pandas as pd
import numpy as np

df = pd.read_csv('datasets/uber_trips_2014.csv', nrows=10000)
latitudes = list(df['pickup_latitude'])
longitudes = list(df['pickup_longitude'])
#gmap = gmplot.GoogleMapPlotter(40.7128, 74.0059, 16)
gmap = gmplot.GoogleMapPlotter.from_geocode("New York")


#gmap.scatter(latitudes, longitudes, '#3B0B39', size=40, marker=False)
#gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
#gmap.scatter(latitudes, longitudes, '#3B0B39', size=40, marker=False)
#gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
gmap.heatmap(latitudes, longitudes)

gmap.draw("mymap.html")
