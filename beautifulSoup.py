import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

urlName = input("Enter URL: ")
numCount = input("Enter count: ")
numPosition = input("Enter position: ")
count = int(numCount)
position = int(numPosition)
for i in range(count+1):
	handle = urllib.request.urlopen(urlName).read()
	soup = BeautifulSoup(handle,"html.parser")
	tags = soup("a")
	print("Retrieving:",urlName)
	urlName = tags[position-1].get("href",None)