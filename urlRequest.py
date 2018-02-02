import requests
r = requests.get('https://elpais.com/')
print(r.json())
print(r.headers)
