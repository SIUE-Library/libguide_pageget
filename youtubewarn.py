import re
import sys
import requests

regex = r"http:\/\/(www\.)?youtube.com"

print(sys.argv[1])
num = 0
for line in open(sys.argv[1], "r"):
	print("line %d" % num)
	num += 1
	html = requests.get(line).text
	matches = re.finditer(regex, html)
	for match in matches:
		print("on page %s http youtube link %s detected" % (line, line[match.start():match.end()]))

print("done")
