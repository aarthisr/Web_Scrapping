import requests

f1 = open("static/ebay_uk_listing.html","w+")
headers = {
    'authority': 'www.ebay.co.uk',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.ebay.co.uk/b/Furniture/3197/bn_1633685',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
}

response = requests.get('https://www.ebay.co.uk/b/Sofas-Armchairs-Couches/38208/bn_1633911')
print(response.status_code)
print(response.content)
f1.write(str(response.content) + "\n")