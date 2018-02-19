##Wifi_data.py

import requests

url = 'http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=b087af42-2c54-4dbf-86c8-427d788779e5'

response = requests.get(url)

data = response.json()

print(data)