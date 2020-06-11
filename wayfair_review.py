# import requests
#
# headers = {'origin': 'https://www.wayfair.com',
#            'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6',
#            'accept-encoding': 'gzip, deflate, br',
#            'use-path': 'true',
#            'authority': 'www.wayfair.com',
#            'referer': 'https://www.wayfair.com/furniture/pdp/greyleigh-ringgold-6-drawer-double-dresser-gryl5417.html?piid=33730778&page=2',
#            'accept': '*/*',
#            'pragma': 'no-cache',
#            'x-request-id': 'otAgYVpCE52gLvWh8ikzAg==',
#            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
#            'cache-control': 'no-cache',
#            'content-type': 'application/json'}
# # data = '{"query":"product_reviews_phone_queries~0","variables":{"product_sku":"GRYL5417","sort_order":"DATE_DESCENDING","page_number":1,"filter_rating":"","reviews_per_page":0,"search_query":"","language_code":"en"}}'
# #
# # response = requests.post('https://www.wayfair.com/graphql', headers=headers, data=data)
# # print(response.content)
# #
# # # data = '{"query":"product_reviews_phone_queries~0","variables":{"product_sku":"GRYL5417","sort_order":"RELEVANCE","page_number":2,"filter_rating":"","reviews_per_page":0,"search_query":"","language_code":"en"}}'
# data = '{"query":"product_reviews_phone_queries~0","variables":{"product_sku":"w000665977","sort_order":"DATE_DESCENDING","page_number":30,"filter_rating":"","reviews_per_page":0,"search_query":"","language_code":"en"}}'
# #
# # response = requests.post('https://www.wayfair.com/graphql', headers=headers, data=data)
#
#
# params = (
#     ('queryPath', 'product_reviews_phone_queries~0'),
# )
#
# # data = '{"query":"product_reviews_phone_queries~0","variables":{"product_sku":"W000665977","sort_order":"DATE_DESCENDING","page_number":1,"filter_rating":"","reviews_per_page":0,"search_query":"","language_code":"en"}}'
#
# response = requests.post('https://www.wayfair.com/graphql', headers=headers, params=params, data=data)
# print(response.content)
# #NB. Original query string below. It seems impossible to parse and
# #reproduce query strings 100% accurately so the one below is given
# #in case the reproduced version is not "correct".
# # response = requests.post('https://www.wayfair.com/graphql?queryPath=product_reviews_phone_queries~0', headers=headers, cookies=cookies, data=data)



import requests, json

# cookies = {
#     'CSNUtId': '23f2f229-5d09-684a-7dee-0b1876424002',
#     '_ga': 'GA1.2.131259126.1561032585',
#     '_pxvid': '4acd4a50-9354-11e9-87ba-0242ac12000e',
#     'rfGUID': '23f2f229-5d09-684a-7dee-0b1876424002',
#     'LowIntentModalHardClosed': '1',
#     'rskxRunCookie': '0',
#     'rCookie': 'pgd4zdf5odelojohb9lx7j',
#     'Current_Sort_B2B': '0',
#     'canary': '0',
#     '__ssid': '6e8c6173709deb602b4fe915eae6480',
#     'AppInterstitial': 'visit_date_1=2019-08-27&visit_date_2=2019-08-30&visit_date_3=2019-09-05',
#     'vid': 'a2d02064-5e21-9912-8587-d422a7a9f702',
#     'WFSID': '142874adb05a9eb22dd2875c63335d5d',
#     'WFDC': 'BO',
#     'serverUAInfo': '%7B%22browser%22%3A%22Google+Chrome%22%2C%22browserVersion%22%3A79.03945117%2C%22OS%22%3A%22Mac+OS+X%22%2C%22OSVersion%22%3A10.146%2C%22isMobile%22%3Afalse%2C%22isTablet%22%3Afalse%7D',
#     '_pxhd': '98cca2cd677addc8de6a05e727d7450903c95c4dbc61d448d4ef2802394de4f6:4acd4a50-9354-11e9-87ba-0242ac12000e',
#     '_gid': 'GA1.2.503125252.1579260180',
#     'AMP_TOKEN': '%24NOT_FOUND',
#     'pushNotificationsSignupSent': 'true',
#     'CSNBrief': 'SLoc%3Dbo1%26TopNavCSSCachedByBrowser%3Dtrue',
#     'dtr': '1',
#     'otx': 'otAgZF4hmRKFh9Qip6n3Ag%3D%3D',
#     'hideGoogleYolo': 'true',
#     'CSN': 'PRVW%3DSYPL3204%257CBGLS7656%257CBBME1860%257CSEHO6958%257CBGRS6531%257CGOL1499%257CAVBC1161%257CZSMT1064%257CW001774349%257CAR1752%257CAR1731%257CW001308432%26CLVW%3D54%257C145%257C32%257C6412%257C147',
#     '_px3': '4e098127051c4c427525425bb67489d33da80de6ab8a6c4f7bbd0486062ede36:mmq3cpNVQSRN0K2WvAwehqc1hvIKavejLLPyGM+BuzeKO1AbQR9XJXAp8qhV9lpXYAeSoo9151svRGgZpPEuCw==:1000:6Jrhur5X1yvhWq6YbpXiPiBqSR2CdCgezwlqt3ziyZK0ui5aTKSnHihJc16U+T1Ls7RkLneUb2ruW7+64aLUqGy4oeISE+M+bt8gbQxcTNRGt+kJAMb4SvSDE1QWdGEtwvUhXRuHBXNrDfxgfDu4MWUuhOTq6oJ5UK90wVxH15I=',
#     'CSNPersist': 'page_of_visit%3D2121%26latestRefid%3DSG',
#     'lastRskxRun': '1579260486446',
# }

headers = {
    'authority': 'www.wayfair.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json',
    'origin': 'https://www.wayfair.com',
    'use-path': 'true',
    'x-parent-txid': 'otAgb14hmj0o0TK0soDhAg==',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'content-type': 'application/json',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.wayfair.com/furniture/pdp/symple-stuff-mesh-task-chair-sypl3204.html',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
}

params = (
    ('queryPath', 'product_reviews_phone_queries~0'),
)

data = '{"query":"product_reviews_phone_queries~0","variables":{"product_sku":"SYPL3204","sort_order":"DATE_DESCENDING","page_number":2,"filter_rating":"","reviews_per_page":0,"search_query":"","language_code":"en"}}'

response = requests.post('https://www.wayfair.com/graphql', headers=headers, params=params, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.wayfair.com/graphql?queryPath=product_reviews_phone_queries~0', headers=headers, cookies=cookies, data=data)
print(json.dumps(str(response.content)))