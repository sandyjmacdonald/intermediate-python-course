#!/usr/bin/env python

import pandas as pd
import seaborn as sns

weather = pd.read_csv("weather-data-6-months.csv")

weather["time"] = pd.to_datetime(weather["time"])
weather.index = weather["time"]

daily = weather.resample("1D").mean()

sns.set_theme(style="darkgrid")
plot = sns.lineplot(x="time", y="temperature", data=daily)