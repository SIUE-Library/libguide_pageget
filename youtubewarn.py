import re
import sys
import requests

regex = r"http:\/\/(www\.)?youtube.com"

print(sys.argv[1])
num = 0
for line in open(sys.argv[1], "r"):
	print("checking page %d..." % num)
	num += 1
	html = requests.get(line).text
	matches = re.finditer(regex, html)
	for match in matches:
		print("on page %s http youtube link %s... detected" % (line[:-1], html[match.start():match.end()+20]))

print("done")
