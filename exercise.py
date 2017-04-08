import xml.etree.ElementTree as ET
import urllib

url = "https://www.vietcombank.com.vn/exchangerates/ExrateXML.aspx"
file = urllib.urlopen(url)
data = file.read()
tree = ET.fromstring(data)

print 'Ty gia:\n'
lst = tree.findall('Exrate')
for item in lst:
    print item.get('CurrencyName'),'(',item.get('CurrencyCode'),'): ',item.get('Transfer')
print '\n'    
tien = raw_input('Nhap vao so tien muon chuyen doi: ')    
currency = raw_input('Nhap vao don vi tien: ')
for item in lst:
    if currency == item.get('CurrencyCode'):
        quydoi = int(tien) * float(item.get('Transfer'))
        print 'Tien quy doi sang Viet Nam:',quydoi,'VND'
