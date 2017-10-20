import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('only data.csv')

lon=data['lon']
lat=data['lat']
sol=data['sol']
win=data['win']

# Plot it out
fig, ax = plt.subplots()
#heatmap = ax.pcolor(nba_sort, cmap=plt.cm.Blues, alpha=0.8)

plt.scatter(lon, lat, c=win, alpha=0.5)
plt.show()