#!/usr/bin/python3


# Import libraries
import requests

# Declaration of variables
address = input("Type in a destination url (format: google.com"): \n")

# Concatenation of strings
user_url = str('https://' + address)

# Ask the user for whoch HTTP method to use
choice = input("Select the HTTP method from the following list: \n get \n post \n put \n delete \n head \n patch \n options \n")

# 
