import urllib.request, urllib.parse, urllib.error
import json

url = input()
handle = urllib.request.urlopen(url).read()
stuff = json.loads(handle)
total = 0
for num in range(len(stuff["comments"])):
	number = stuff["comments"][num]["count"]
	total = total + number
print(total)
