# Get S&P500 list of companies tickers from NYSE

import requests
from bs4 import BeautifulSoup

# import numpy - numpy.array
# import numpy as np - np.array
# from numpy import array - array

# Sends a GET request to the specified URL - fetches the website
sp = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")

# print(sp) # Status code
# content - Returns the content of the response, in bytes, after which data can be pulled out of the HTML file
sp = BeautifulSoup(sp.content, 'html.parser')
# print(sp) # The page source code

# Empty list initialized
SP500 = []

# Find all <a> components and look for href in them
for each in sp.find_all('a', href=True):
    if 'nyse.com' in each.get('href'):  # Check if nyse.com is part of the link
        SP500.append(each.get('href').split("XNYS:")[
                     1].upper())  # Extract the end of it
    if len(SP500) == 500:
        break

print(SP500)
