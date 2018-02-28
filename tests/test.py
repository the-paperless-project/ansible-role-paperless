import requests

url = 'http://localhost/admin/login/?next=/admin/'

with requests.Session() as session:
    session.get(url)
    csrftoken = session.cookies['csrftoken']
    response = session.post(
        url,
        data={
            'csrfmiddlewaretoken': csrftoken,
            'next': '/admin/',
            'password': 'Vf3FUN2ozH1ReDoK',
            'username': 'admin'
        },
        headers={
            'Referer': url
        }
    )


print(response.status_code)
print(response.text)

assert response.status_code == 200
assert 'Paperless administration' in response.text
