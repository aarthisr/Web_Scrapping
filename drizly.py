import requests
import re

headers = {
    'authority': 'drizly.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,kn;q=0.6',
}

response = requests.get('https://drizly.com/', headers=headers)
crsf = re.search(r'name="csrf-token" content="(.*?)"',response.content.decode('utf-8')).group(1)
print (crsf)
headers = {
    'accept-encoding': 'gzip, deflate, br',
    'x-csrf-token': crsf,
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,kn;q=0.6',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://drizly.com/',
    'authority': 'drizly.com',
    'x-requested-with': 'XMLHttpRequest','cookie':'_drizly_web_session'+str(response.headers.get("Set-Cookie").split("_drizly_web_session")[1].split(";")[0])+"; "
}

response = requests.get('https://drizly.com/modal/resolve_stores.json?latitude=40.7347439&longitude=-73.98366970000001&zip=10003', headers=headers)
print(response.content)

headers = {
    'origin': 'https://drizly.com',
    'accept-encoding': 'gzip, deflate, br',
    'x-csrf-token': crsf,
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,kn;q=0.6',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://drizly.com/',
    'authority': 'drizly.com',
    'x-requested-with': 'XMLHttpRequest','cookie':'_drizly_web_session'+str(response.headers.get("Set-Cookie").split("_drizly_web_session")[1].split(";")[0])+"; "
}

data = {
  'persist': 'false',
  'address[address1]': 'APT 307 305',
  'address[latitude]': '40.7347439',
  'address[longitude]': '-73.98366970000001',
  'address[city]': 'New York',
  'address[state]': 'NY',
  'address[stateLong]': 'New York',
  'address[country]': 'US',
  'address[country_code]': 'US',
  'address[zip]': '10003',
  'delivery_types': '20'
}

response = requests.post('https://drizly.com/location/async_create', headers=headers, data=data)



headers = {
    'authority': 'drizly.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'referer': 'https://drizly.com/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,kn;q=0.6','cookie':'_drizly_web_session'+str(response.headers.get("Set-Cookie").split("_drizly_web_session")[1].split(";")[0])+"; ",
}

response = requests.get('https://drizly.com/beer/ale/ipa/c15', headers=headers)

print (response.headers)

open("html.html","w+").write(response.content.decode('utf-8'))
print (response)