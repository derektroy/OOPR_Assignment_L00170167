"""
#
# File          :   L00170167_Q3_File_2.py
# Created       :    
# Author        :   Derek Troy
# Version       :   1.0.5
# Licensing     :   (C) 2021 Derek Troy LYIT
#                   Available under GNU Public License (GPL)
# Description   :   File to Scrape and Parse a Webpage from Apache Server
#
"""
# Import Required Modules
import requests
import bs4

# What Website are we going to look at
Web_url = "http://192.168.1.60"

# What are we going to do with that URL
r = requests.get(Web_url)

# Parse HTML Code
soup = bs4.BeautifulSoup(r.content, 'lxml')
print(soup.prettify())

# Find the headers
headers = soup.find_all("div", {"class": "section_header"})
print(headers)


# Count Apache2
def returncount(url, word):
    words = (soup.text.lower())
    words = words.split()
    return words.count(word.lower())


wordCount = returncount(Web_url, 'Apache2')
print('Apache2 Word Count =', wordCount)

wordCount = returncount(Web_url, 'Ubuntu')
print('Ubuntu Word Count =', wordCount)
