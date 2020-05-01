import requests
import csv
import datetime


with open('March.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        resp = requests.post('https://api.antares.nullteam.info/mon/record/', json={
        #resp = requests.post('http://localhost/mon/record/', json={
            'machine_id': int(row[0]),
            'date_captured': datetime.datetime.strptime(row[1], '%d.%m.%Y %H:%M').isoformat(),
            'temperature': float(row[2].replace(',', '.')),
            'vibration': float(row[3].replace(',', '.')),
            'power': float(row[4].replace(',', '.')),
            'system_load': float(row[5].replace(',', '.')),
            'work_time': int(row[6]),
        }, auth=requests.auth.HTTPBasicAuth('machine', 'tokenpassword'))
        print(resp.text)

