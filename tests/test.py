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
            'password': 'Vf3FUN2ozH1ReDoK',
            'username': 'admin'
        },
        headers={
            'Referer': url
        }
    )


assert response.status_code == 200
print(response.text)
