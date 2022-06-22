#!/usr/bin/env python

outfile = open("numbers.txt", "w")
for i in range(10):
    outfile.write(str(i + 1) + "\n")
outfile.close()