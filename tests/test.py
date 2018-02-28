import requests

url = 'http://localhost:80'
print(url)
r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.text)

url = 'http://localhost:80/admin/'
print(url)
r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.text)

url = 'http://localhost:80/admin/login/?next=/admin/'
print(url)
r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.text)
