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

#Requires: guides.csv (line-seperated list of urls)
def main():
	with open("./guides.csv", "r") as inFile:
		with open("./outfile.txt", "w") as outFile:
			urls = inFile.readlines()
			reg = re.compile("libguides\.siue\.edu")
			for url in urls:
				outFile.write(url)
				print("Reading: " + url)
				url_list = getUrls(url[:-1])
				for item in url_list:
					if(reg.search(str(item))):
						outFile.write('\t' + str(item) + '\n')


def getUrls(address):
	response = requests.get(address)
	soup = BeautifulSoup(response.text, 'html.parser')
	name = soup.title.string
	name = name.replace("'", "")
	urlsWithin = []
	for link in soup.find_all('a'):
		urlsWithin.append(link.get('href'))
	return urlsWithin

main()
