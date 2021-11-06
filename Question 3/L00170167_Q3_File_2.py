"""
#
# File          :   L00170167_Q3_File_2.py
# Created       :    
# Author        :   Derek Troy
# Version       :   1.0.0
# Licensing     :   (C) 2021 Derek Troy LYIT
#                   Available under GNU Public License (GPL)
# Description   :   File to Scrape and Parse a Webpage from Apache Server
#
"""
# Import Required Modules
import requests
from bs4 import BeautifulSoup

# What Website are we going to look at
Web_url = "http://192.168.1.60"

# What are we going to do with that URL
r = requests.get(Web_url)

# Parse HTML Code
soup = BeautifulSoup(r.content, 'lxml')
print(soup.prettify())