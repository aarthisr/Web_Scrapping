import requests

headers = {
    'origin': 'https://www.cymax.com',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'content-type': 'application/json; charset=UTF-8',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'authority': 'www.cymax.com',
}

data = '{"productId":"530728"}'

response = requests.post('https://www.cymax.com/WebService/WService.svc/Reviews_Get', headers=headers, data=data)
print(str(response.content))