import requests

headers= {'user-agent': 'my-agent/1.01',
'Accept-Encoding':'gzip'}
res= requests.get('http://www.httpbin.org', headers=headers)


def analyse(res):
    return {'status':res.status_code, 'headers':res.headers}

print(analyse(res))