#!/usr/bin/env python

import pandas as pd

weather = pd.read_csv("weather-data-6-months.csv")

weather["time"] = pd.to_datetime(weather["time"])
weather.index = weather["time"]

daily = weather.resample("1D").mean()
daily.sort_values(by="temperature", ascending=False, inplace=True)

print(daily)