#Programmer: Jacob Grubb (jagrubb@siue.edu)
#Organization: Lovejoy Library
#Project: libguide_pageget
#File: getpages.py
#Description: Script for parsing through a list of urls, identifying links
#		within each file

import re
import requests
from bs4 import BeautifulSoup
import os

def main():
	print("okay")


def getUrls(address):
	response = requests.get(address)
	soup = BeautifulSoup(response.text, 'html.parser')
	name = soup.title.string
	name = name.replace("'", "")
	urlsWithin = []
	for link in soup.find_all('a'):
		urlsWithin.append(link.get('href'))
	return urlsWithin


