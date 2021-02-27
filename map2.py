import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter the locationn name')
serviceurl = 'http:///py4e-dataa.dr-chuck.net/json?'
url = serviceurl + urllib.parse.urlencode({'address':address,'key':42})
data = urllib.request.urlopen(url).read().decode()
js=json.loads(data)
print(json.dump(js, indent =4))
placeid = js['results'][0]['place_id']
