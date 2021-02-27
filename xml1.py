import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Saurav Salunke</name>
    <phone type = "intl">
    +19860908336
    </phone>
    <email hide ="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name;',tree.find('name').text)
print('ATTR:',tree.find('email').get('hide'))    
