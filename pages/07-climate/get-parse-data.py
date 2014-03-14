import requests
import cStringIO
import csv

url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/CAN.csv'
response = requests.get(url)
if response.status_code != 200:
    print 'Failed to get data:', response.status_code
else:
    reader = cStringIO.StringIO(response.text)
    wrapper = csv.reader(reader)
    for record in wrapper:
        year = int(record[0])
        value = float(record[1])
        print year, ':', value
