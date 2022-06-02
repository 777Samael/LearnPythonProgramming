import json
import urllib.request

json_data_source = "https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/1/2/1880-2022/data.json"

with urllib.request.urlopen(json_data_source) as data:
    anomalies = json.loads(data.read().decode())
    print(anomalies)

with open('temperature_anomaly.json', 'w', encoding='utf-8') as testfile:
    json.dump(anomalies, testfile)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')

print("---")
