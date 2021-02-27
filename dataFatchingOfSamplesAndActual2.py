import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

handle = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_555936.html").read()
soup = BeautifulSoup(handle,"html.parser")
tags = soup("tr")
numDic = dict()
for tag in tags:
	string = str(tag)
	if re.search('>([0-9]+)<',string):
		num = re.findall('>([0-9]+)<',string)
		numDic[num[0]] = numDic.get(num[0],0) + 1
total = 0
for key,value in numDic.items():
	times = int(key) * value
	total = total + times
print(total)