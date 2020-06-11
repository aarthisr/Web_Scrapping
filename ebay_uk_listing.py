import requests

headers = {
    'authority': 'www.ebay.co.uk',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'referer': 'https://www.ebay.co.uk/b/Wristwatches/31387/bn_1676345',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',

}

response = requests.get('https://www.ebay.co.uk/b/Pocket-Watches/3937/bn_1676647', headers=headers)
print(response.content)
html_dump = open("ebay_uk_listing.html", "w+")
html_dump.write(str(response.content))
