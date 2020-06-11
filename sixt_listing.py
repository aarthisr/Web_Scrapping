import requests, json


q = '\u4F26\u6566\u5E0C\u601D\u7F57\u673A\u573A T2 T3 T4 '
uda = '2020-01-30'
rda= '2020-02-10'
headers = {
    'authority': 'www.sixt.cn',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.sixt.cn/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
}
params = (
    ('q', q),
    ('typ', 'pickup'),
)
response = requests.get('https://www.sixt.cn/reservation/app/stations/list.json', headers=headers, params=params)
response=json.loads(response.content)
uci=response.get("data").get("airports")[0].get("StationID")
print(uci)
params = (
    ('q', [q, q]),
    ('uci', uci),
    ('rci', uci),
    ('uda', uda),
    ('uti', '10:00'),
    ('rda', rda),
    ('rti', '10:00'),
)
response = requests.get('https://www.sixt.cn/reservation/offerselect', headers=headers, params=params)
print(response.cookies)
headers['cookie']= 'SXOC='+response.cookies["SXOC"]+'; SIXTCN='+response.cookies["SIXTCN"]+';'
data = {
  't': response.cookies["SXOC"]
}
response = requests.post('https://www.sixt.cn/reservation/offerselect', headers=headers, data=data, params=params)
html_dump = open("sixt_listing.html", "w")
html_dump.write(str(response.content, 'utf-8'))
print(response.cookies)

# params = (
#     ('uci', uci),
#     ('uda', uda),
#     ('uti', '10:00'),
#     ('rci', uci),
#     ('rda', rda),
#     ('rti', '10:00'),
#     ('grp', 'CDMR'),
#     ('pay', 'flexi'),
#     ('v', '0'),
#     ('sv', '0')
# )
# del headers['cookie']
# response = requests.get('https://www.sixt.cn/reservation/offerconfig', headers=headers, params=params)
# print(response.cookies)
# headers['cookie']= 'SXOC='+response.cookies["SXOC"]+';'
# # headers['cookie']= 'SXOC='+response.cookies["SXOC"]+'; SIXTCN='+response.cookies["SIXTCN"]+';'
# params = (
#     ('uci', uci),
#     ('uda', uda),
#     ('uti', '10:00'),
#     ('rci', uci),
#     ('rda', rda),
#     ('rti', '10:00'),
#     ('grp', 'CDMR'),
#     ('pay', 'flexi'),
#     ('v', '0'),
#     ('sv', '0')
# )
#
# data = {
#   't': response.cookies["SXOC"]
# }
#
# response = requests.post('https://www.sixt.cn/reservation/offerconfig', headers=headers, params=params, data=data)
#
# #NB. Original query string below. It seems impossible to parse and
# #reproduce query strings 100% accurately so the one below is given
# #in case the reproduced version is not "correct".
# # response = requests.post('https://www.sixt.cn/reservation/offerconfig?uci=7429&uda=2020-01-23&uti=10%3A00&rci=7429&rda=2020-01-30&rti=10%3A00&grp=CDMR&pay=flexi', headers=headers, data=data)
# print(response.content)
# print(response.status_code)
# html_dump = open("sixt_product.html", "w")
# html_dump.write(str(response.content, 'utf-8'))

