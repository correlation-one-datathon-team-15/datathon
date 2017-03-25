import pandas
import random
import json
#n = 1880795 #number of records in file
filename = ''  # fill in csv filename
n = sum(1 for line in open(filename))
#n = 2653532 # number of records in file
s = 100000 #desired sample size
# selecting random sample of 100000 from Q2 uber
filename = "datasets/uber_trips_2014Q3.csv"
skip = sorted(random.sample(xrange(1,n),n-s))
print(type(skip))
df = pandas.read_csv(filename, skiprows=skip)
print(df)
df.to_csv('newfile.csv')  # change csv name
'''
latitudes = list(df['pickup_latitude'])
longitudes = list(df['pickup_longitude'])
out_dict = {'latitudes': latitudes, 'longitudes': longitudes}
print(out_dict)
with open('uber_2014Q3.json', 'w') as fileout:
    json.dump(out_dict, fileout)
'''
