#!/usr/bin/python

# Importing libraries (Tell the script to bring in some tools)
import psutil

# Generate CPU times as a tuple
print(f"CPU Time: {psutil.cpu_times()}\n")

# F-string example
val = `Orange`
print(f"{val} is the first thing on the list. Plese don't forget to get some {val"}