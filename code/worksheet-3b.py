#!/usr/bin/env python

import matplotlib.pyplot as plt

myfile = open("weather-data-1-week.csv", "r")

temps = []

for line in myfile:
    if not line.startswith("time"):
        line = line.rstrip().split(",")
        t_celsius = float(line[1])
        temps.append(t_celsius)

plt.plot(temps)
plt.show()