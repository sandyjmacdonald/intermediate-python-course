#!/usr/bin/env python

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

myfile = open("weather-data-1-day.csv", "r")
lines = myfile.readlines()

header = lines[0].rstrip().split(",")

outfile = open("ftemps.txt", "w")
outfile.write(header[1] + "\n")

for line in lines[1:]:
    line = line.rstrip().split(",")
    t_celsius = float(line[1])
    t_fahrenheit = celsius_to_fahrenheit(t_celsius)
    outfile.write(str(t_fahrenheit) + "\n")

outfile.close()