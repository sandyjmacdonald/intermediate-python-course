#!/usr/bin/env python

# myfile = open("weather-data-1-day.csv", "r")
# print(dir(myfile))

# myfile = open("weather-data-1-day.csv", "r")
# lines = myfile.readlines()

# print(lines[0])
# print(lines[99])

# for line in lines:
#     line = line.rstrip()
#     line = line.split(",")
#     print(line)

myfile = open("weather-data-1-day.csv", "r")
lines = myfile.readlines()

header = lines[0].rstrip().split(",")
print(header[-1])

for line in lines[1:]:
    line = line.rstrip().split(",")
    light_value = float(line[-1])
    light_value = round(light_value)
    print(light_value)