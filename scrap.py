import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the url you want to scrap....")
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('a')
position = input('Enter the position')
position = int(position)
position = position-1
count = input('enter the count')
count = int(count)
meter = 0
meter = int(meter)
while count !=meter :
    print('Tag:',tags[position])
    print('URL:',tags[position].get('href',None))
    print('Contents',tags[position].contents[0])
    print('Attr',tags[position].attrs)
    meter = meter+1
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = tags[position].get('href',None)
    print(url)
    html = urllib.request.urlopen(url ,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    print('break',meter,count)
