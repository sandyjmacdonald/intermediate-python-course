#!/usr/bin/env python

import matplotlib.pyplot as plt
from datetime import datetime

myfile = open("weather-data-1-week.csv", "r")

temps = []
times = []

for line in myfile:
    if not line.startswith("time"):
        line = line.rstrip().split(",")
        t_celsius = float(line[1])
        temps.append(t_celsius)
        dt = datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S")
        times.append(dt)

fig, ax = plt.subplots()

ax.plot(times, temps)

fig.autofmt_xdate()

ax.set_xlabel("Date")
ax.set_ylabel("Temp (°C)")
ax.set_title("Outside temperature")

plt.show()