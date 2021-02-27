import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input()
handle = urllib.request.urlopen(url).read()
tree = ET.fromstring(handle)
lst = tree.findall('comments/comment')
total = 0
for item in lst:
	numString = item.find('count').text
	num = int(numString)
	total = total + num
print(total)