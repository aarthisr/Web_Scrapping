import requests
#
f1 = open("static/cymax.html","w+")
headers = {
    'authority': 'www.cymax.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    # 'sec-fetch-mode': 'navigate',
    # 'sec-fetch-user': '?1',
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'sec-fetch-site': 'same-origin',
    # 'referer': 'https://www.cymax.com/',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
    # 'cookie': '__cfduid=d61a140f9f207bce11eeb4f9c3068bd0f1571124612; ASP.NET_SessionId=psgahz4v4yg3pi33st0ejuuf; VisitorID=008F8E15; ft=date=10/15/2019 12:30:12 AM&url=/Portal/Home/Home.aspx&referrer=https://www.google.com/; gclRef=gclsrc=&gclid=; Ref=src=&srcID=&srcInfo=www.cymax.com%2f&UrlReferrer=https%3a%2f%2fwww.google.com%2f; cseRef={}; ai_user=5ND46|2019-10-15T07:30:14.609Z; _hjid=c0b1fc01-edc1-4c61-b6a9-10925d6f5f77; _ga=GA1.2.1304871716.1571124615; _gid=GA1.2.370967945.1571124615; LocationZip=tsCv/EeTvUe6GdMs2y+dXe+OX6RaymS/; localOnly=0; csUrl=/Computer-Desks--C279.htm; LastCategoryId=279; ai_session=E0RTJ|1571124616011|1571126169812.39',
}

# response = requests.get('https://www.cymax.com/Office-Sets--C1412.htm')
# print(str(response.text))




# import requests

# headers = {
#     'authority': 'www.cymax.com',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-user': '?1',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'sec-fetch-site': 'same-origin',
#     'referer': 'https://www.cymax.com/desks--C0.htm?q=desks',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
#
# }
#
# params = (
#     ('q', 'desks'),
# )

# response = requests.get('https://www.cymax.com/desks--C0.htm', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
response = requests.get('https://www.cymax.com/desks--C0.htm?q=desks', headers=headers)
print(str(response.text))
f1.write(str(response.text) + "\n")
