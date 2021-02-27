import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx  = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum = 0
while True :
    url = input('Enter the url you want to open')
    uh = urllib.request.urlopen(url,context = ctx)
    data = uh.read()
    tree = ET.fromstring(data)
    com = tree.findall('.//count')
    for counts in com:
        value = counts.text
        sum = sum+int(value)
    print(sum)
