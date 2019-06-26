import requests
import sys
import re
import time

input = open("pages", "r")
pattern = "<img[^>]*>"
url = '((\/\/)|(http:\/\/)|(www\.))[^"]+'
for page in input:
	html = requests.get("http://"+page).text
	time.sleep(.1)
	matches = re.finditer(pattern, html)
	for match in matches:
		temp = html[match.start():match.end()]
		m = re.search(url, temp).group(0)
		print(m)
