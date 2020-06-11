import requests

# headers = {
#     'pragma': 'no-cache',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
#     'accept': '*/*',
#     'cache-control': 'no-cache',
#     'authority': 'www.thenorthface.com',
#     'x-requested-with': 'XMLHttpRequest',
#     'referer': 'https://www.thenorthface.com/shop/womens-jackets-vests-rainwear',
# }

params = (
    ('categoryId', '299273'),
    ('searchSource', 'N'),
    ('storeId', '7001'),
    ('catalogId', '20001'),
    ('langId', '-1'),
    ('beginIndex', '0'),
    ('returnProductsOnly', 'true'),
    ('requesttype', 'ajax'),
)
# response = requests.get('https://www.thenorthface.com/shop/VFAjaxGetFilteredSearchResultsView',  params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.thenorthface.com/shop/VFAjaxGetFilteredSearchResultsView?categoryId=299273&searchSource=N&storeId=7001&catalogId=20001&langId=-1&beginIndex=20&returnProductsOnly=true&requesttype=ajax', headers=headers, cookies=cookies)
response = requests.get("https://www.thenorthface.com/shop/VFAjaxGetFilteredSearchResultsView?categoryId=299284&searchSour"
                        "ce=N&storeId=7001&catalogId=20001&langId=-1&beginIndex=20&returnProductsOnly=true&requesttype=ajax")
print(response.content)
html_dump = open("thenorthface_listing.html", "w+")
html_dump.write(str(response.content))