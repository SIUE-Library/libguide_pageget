import re
import sys
import requests

regex = r'"http:\/\/(www\.)?youtube.com\S*"'

print(sys.argv[1])
out = open("tomodify", "w")

num = 0
for line in open(sys.argv[1], "r"):
	print("checking page %d..." % num)
	num += 1
	html = requests.get("https://"+line).text
	matches = re.finditer(regex, html)
	for match in matches:
		print("on page %s http youtube link %s... detected" % (line[:-1], html[match.start():match.end()]))
#		write(out, line)

print("done")
