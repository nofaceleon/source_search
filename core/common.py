import requests


def get_html(url, headers, method='GET', payload=None, encoding='utf-8', content='html'):
    if payload is None:
        payload = {}
    r = requests.request(method, url, headers=headers, data=payload, timeout=5)
    if r.status_code == 200:
        if content == 'html':
            r.encoding = encoding
            return r.text
        elif content == 'json':
            return r.json()
    else:
        print(f"请求失败, 状态码:{r.status_code}")