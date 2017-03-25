import matplotlib as plt
import pandas as pd
import zipcode
import geocoder
import numpy as np

data = pd.read_csv("../uber_trips_2014.csv", header=None)

lats = list(data[1])
longs = list(data[2])

bronx = 0
queens = 0
manhattan = 0
brooklyn = 0
statenIsland = 0
neighborhoods = {"bronx": 0, "queens": 0, "manhattan": 0, "brooklyn": 0, "statenIsland": 0}

for i in range(1, 1000):
    #print "example: " + lats[i] + " " + longs[i]
    lat = float(lats[i])
    lon = float(longs[i])
    location = geocoder.google([lat, lon], method='reverse')
    postal = -1
    if location.ok: #Location is valid
        postal = int(str(location.postal))
    if postal > -1:
        if postal >= 10451 and postal <= 10475:
            bronx += 1
            neighborhoods["bronx"] += 1
        elif postal >= 10001 and postal <= 10280:
            manhattan += 1
            neighborhoods["manhattan"] += 1
        elif postal >= 11201 and postal <= 11239:
            brooklyn += 1
            neighborhoods["brooklyn"] += 1
        elif postal >= 11354 and postal <= 11697:
            queens += 1
            neighborhoods["queens"] += 1
        elif postal >= 10301 and postal <= 10314:
            statenIsland += 1
            neighborhoods["statenIsland"] += 1
    print "postal: " + str(postal)
    if i % 10 == 0:
        print str(i) + ": bronx " + str(bronx) + ", manhattan " + str(manhattan) + ", queens " + str(queens) + ", brooklyn " + str(brooklyn) + ", statenIsland " + str(statenIsland)

objects = ("Bronx", "Queens", "Manhattan", "Brooklyn", "Staten Island")
y_pos = np.arange(len(objects))
performance = [bronx, queens, manhattan, brooklyn, statenIsland]

plt.bar(y_pos, performance, align='center', alpha=0.5)()
plt.title("Number of Rides per Neighborhood by Uber in 2014")
plt.ylabel("Rides")
#plt.set_xlabel("Neighborhood")
plot.xticks(y_pos, objects)
#plot.set_xticks(5) #5 neighborhoods
#plot.set_xticklabels(("Bronx", "Queens", "Manhattan", "Brooklyn", "Staten Island"))

plt.show()
