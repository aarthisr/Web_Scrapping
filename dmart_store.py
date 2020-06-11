import requests

# cookies = {
#     'SSESSb586e3670e1b160fd411312e259e4db8': 'gyao2d8CZ_K16MrtupQd9QQ_OubvOWi_fJ1y6mdvLks',
#     'ARRAffinity': '1028d78d666e9f22c35877ad4ad23915976477f8ae7826f5b20f2538d086ddf7',
#     'has_js': '1',
#     '_ga': 'GA1.2.1901525659.1560752732',
#     '_gid': 'GA1.2.487198706.1560752732',
# }

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://www.dmartindia.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.dmartindia.com/store-locator',
}

data = {
  'stateName': 'Andhra Pradesh',
  'cityName': 'Kakinada',
  'storeName': 'Kakinada',
  'view_store_address': 'store_address_display'
}

response = requests.post('https://www.dmartindia.com/controllers/action/StoreLocatorController.php', headers=headers, data=data)
print(response.content)