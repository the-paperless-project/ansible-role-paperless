import requests

r = requests.get('http://localhost:80/admin/login/?next=/admin/')
print(r.status_code)
