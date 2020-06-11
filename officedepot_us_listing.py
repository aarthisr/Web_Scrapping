import requests

headers = {
    'authority': 'www.officedepot.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': '',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
}
response = requests.get('https://www.officedepot.com/ajaxhtml/getLazyLoadSkuList.do?N=5+593067&seoText=office-chairs&offset=0&skuListView=grid_view&page=1', headers=headers)
print (response.content)
html_dump = open("officedepot_us_listing.html", "w")
html_dump.write(str(response.content))