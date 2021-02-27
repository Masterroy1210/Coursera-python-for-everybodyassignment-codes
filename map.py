
import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


serviceurl = 'http://py4e-data.dr-chuck.net/json?'


while True :
     address = input('enter the location')
     url = serviceurl + urllib.parse.urlencode({'sensor' :'False','address':address})
     uh = urllib.request.urlopen(url,context=ctx)
     data = uh.read()
     try:
        js = json.loads(data)
     except:
        js = None
     placeid = js['results'][0]['place_id']
     print('Place id of the entered location is ',placeid)
