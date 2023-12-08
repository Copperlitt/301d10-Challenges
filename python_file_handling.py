#!/bin/bash

# Script Name:                    Python File Handling
# Author:                         Basil Evelyn
# Date of last revision           12/08/2023

# Create a new .txt file
with open ('example.txt', 'w') as file:
    # Append three lines to the file
    file.write('This is the first line.\n')
    file.write('This is the second line.\n')
    file.write('This is the third line.\n')

# Open the file to read and print the first line
with open('example.txt', 'r') as file:
    first_line = file.readline()
    print('First Line:', first_line)

# Delete the .txt file
import os
os.remove('example.txt')

print('.txt file deleted.')
