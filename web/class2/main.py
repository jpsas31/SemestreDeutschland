import bs4
import client
def analyse(response):
    status, *headers=response.decode().split('\r\n\r\n')[0].split('\r\n')
    print(status,headers)
    

      
client = client.MyClient('www.httpbin.org',80)

response=client.request('POST','post',{"user-agent": "fe"})


analyse(response)