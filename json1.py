import urllib.request,urllib.parse,urllib.error
import ssl
import json

ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter the address of the website')
uh = urllib.request.urlopen(url , context=ctx)

count = 0
sum=0
data = uh.read()
info = json.loads(str(data.decode()))

for item in info['comments'] :
    count = count+1
    sum = sum+item['count']
print(sum)
