import client
def analyse(response):
    status, *headers=response.decode().split('\r\n\r\n')[0].split('\r\n')
    return {'status':status, 'headers':headers}

    

      
client = client.MyClient('www.httpbin.org',80)


response0=client.request('HEAD','get')
response1=client.request('HEAD','get',{'user-agent': 'my-agent/1.01',
'Accept-Encoding':'gzip'})


print(analyse(response0))
print(analyse(response1))
