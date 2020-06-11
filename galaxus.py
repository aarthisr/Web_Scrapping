import requests

headers = {
    'authority': 'www.galaxus.de',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
    'cookie': 'ai_user=u6QBi|2019-06-19T06:26:23.827Z; .z=sQ/RX5gUr6YhkZcDGcWI4Q==; LoggedInUserId=NONE; ak_bmsc=0982550A6C273DB8DF554A9255C213630E621015FD5800008ED5095D23B5A14E~pl8ay9O8sc5q7mMyZlDMRvhSkmTXZASBzedduJi4+WPiyiBoykYjcd/3wj4ulUOaYNaxhRfPq+kRtLJfKvB4IjlbuXV2LDBXoPgA33aj15lT7f+zzAF9psn11r6Qv9lcBwvf5wOWZEr6ERZVOeXniW2Fk7dAQoQx0i1YWcGFGFV4Q42V6Xw4bIK7VWjRjcFA37BCInpJVYaw4JQ1A3jvRIQM9LByjhT9R7PbF4SZvtyM+TIhmUaa8EsPxF8AeM5Hxz; _gcl_au=1.1.1413907453.1560925591; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1964649581.1560925592; _gid=GA1.2.604762966.1560925592; _fbp=fb.1.1560925592250.1520449497; cookieMessageAccepted=1; AKA_A2=A; ClickedMarketingTeaserPerformanceIds=10572065=19.06.2019 12:07; g_affinity=8411fc954318e78dfac53faf91a834f0c5469fede5073423274f0e7aa1ad54fd; .sum=ActiveShopListId=-1&DefaultPickupSiteId=-1&ProductListDisplayModeForProductList=Panel&SelectedUserMenuTab=None&vat=true; DisplayedMarketingTeasers=11019262=19.06.2019 11:56&11439761=19.06.2019 11:56&11447168=19.06.2019 11:56&11427276=19.06.2019 11:56&11428794=19.06.2019 11:56&11464264=19.06.2019 11:56&11442654=19.06.2019 11:56&11439695=19.06.2019 11:56&11296764=19.06.2019 11:56&10570306=19.06.2019 11:56&10572069=19.06.2019 11:56&11019260=19.06.2019 11:56&10910436=19.06.2019 11:56&10570073=19.06.2019 11:56&10572065=19.06.2019 11:56&11147635=19.06.2019 11:56&10570293=19.06.2019 11:56&11231268=19.06.2019 12:07; ai_session=T19dK|1560925592862|1560926281538.395; _gat_UA-34235288-14=1; bm_sv=016FD24A151FAA7A7E78B3E962A2CA8E~Qd9Bolafj8leP4Xxp1bqpz1sqTHkqNJUIJOHeKZeoH9upsCiw/1Pe1hq3H+S3V3+z77/BlN2cDIyk6aCpElBZew4j5PNskLUz6BXhj5agfQo4u5sY+GsudsL5omwpIspXhGnFb3W6G9DcRhPoVc6e7FkrqydNagwaP0zZ3Zszq4=',
}

params = (
    ('tagIds', '614'),
    ('take', '1000'),
)

response = requests.get('https://www.galaxus.de/de/s1/producttype/notebook-6', headers=headers, params=params)
html_dump = open("galaxus_listing.html", "w+")
html_dump.write(str(response.content))
print(response.content)
# response = requests.get('https://www.galaxus.de/de/s1/producttype/notebook-6?tagIds=614&take=1000', headers=headers)
