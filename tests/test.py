import requests

url = 'http://localhost/admin/login/?next=/admin/'

with requests.Session() as session:
    session.get(url)
    csrftoken = session.cookies['csrftoken']
    print(csrftoken)
    response = session.post(
        url,
        data={
            'csrfmiddlewaretoken': csrftoken,
            'next': '/admin/',
            'password': 'passwordQ',
            'username': 'admin'
        },
        headers={
            'Referer': url
        }
    )

print(response)
print(response.status_code)
print(response.headers)
print(response.text)
