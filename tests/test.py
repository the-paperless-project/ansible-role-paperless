import requests

r = requests.get('http://localhost:80')
assert r.status_code == 301

r = requests.get('http://localhost:80/admin/')
assert r.status_code == 301

r = requests.get('http://localhost:80/admin/login/?next=/admin/')
assert r.status_code == 200
print(r.headers)
print(r.text)
