import requests

headers = {
    'authority': 'www.thenorthface.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'referer': 'https://www.thenorthface.com/shop/shoes-mens-running-training',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
}

# params = (
#     ('variationId', 'C3P'),
# )

# response = requests.get('https://www.thenorthface.com/shop/shoes-mens-running-training/mens-rovereto-running-shoes-nf0a3ml3', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
response = requests.get('https://www.thenorthface.com/shop/shoes-mens-sale/mens-thermoball-bootie-ii-nf0a3yux-c1?variationId=WU5', headers=headers)
print(response.content)
html_dump = open("thenorthface_product.html", "w+")
html_dump.write(str(response.content))
