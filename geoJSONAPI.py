import urllib.request, urllib.parse, urllib.error
import json

serviceUrl = "http://py4e-data.dr-chuck.net/json?"
address = input()
urlAddressAndKey = dict()
urlAddressAndKey["address"] = address
urlAddressAndKey["key"] = 42
url = serviceUrl + urllib.parse.urlencode(urlAddressAndKey)
handle = urllib.request.urlopen(url).read()
data = handle.decode()
js = json.loads(data)
place_ID = js["results"][0]["place_id"]
print(place_ID)