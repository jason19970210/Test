#test.py


import requests

res = requests.get("https://www.google.com")

print(res.text)