import requests, json

import requests,json,time

headers = {
    'authority': 'srv.wego.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'doorkey': 'Bearer wego-eyJhbGciOiJIUzI1NiIsInR5cGUiOiJKV1QifQ.eyJyZWZlcnJlciI6Imh0dHBzOi8vd3d3LndlZ28uYWUiLCJob3N0Ijoid3d3LndlZ28uYWUiLCJ1YSI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE0XzYpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83OS4wLjM5NDUuMTMwIFNhZmFyaS81MzcuMzYiLCJhY2NlcHQiOiIqLyoiLCJjb3VudHJ5X2NvZGUiOiJJTiIsImFjY2VwdF9lbmNvZGluZyI6Imd6aXAsIGRlZmxhdGUsIGJyIiwiYWNjZXB0X2xhbmd1YWdlIjoiZW4tR0IsZW4tVVM7cT0wLjksZW47cT0wLjgscGw7cT0wLjcsZGU7cT0wLjYiLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xNF82KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzkuMC4zOTQ1LjEzMCBTYWZhcmkvNTM3LjM2IiwibGFuZ3VhZ2UiOiJlbi1HQiIsImNvbG9yRGVwdGgiOjI0LCJkZXZpY2VNZW1vcnkiOjgsImhhcmR3YXJlQ29uY3VycmVuY3kiOjgsInNjcmVlblJlc29sdXRpb24iOls5MDAsMTQ0MF0sImF2YWlsYWJsZVNjcmVlblJlc29sdXRpb24iOls5MDAsMTQ0MF0sInRpbWV6b25lT2Zmc2V0IjotMzMwLCJ0aW1lem9uZSI6IkFzaWEvQ2FsY3V0dGEiLCJzZXNzaW9uU3RvcmFnZSI6dHJ1ZSwibG9jYWxTdG9yYWdlIjp0cnVlLCJpbmRleGVkRGIiOnRydWUsImFkZEJlaGF2aW9yIjpmYWxzZSwib3BlbkRhdGFiYXNlIjp0cnVlLCJjcHVDbGFzcyI6Im5vdCBhdmFpbGFibGUiLCJwbGF0Zm9ybSI6Ik1hY0ludGVsIiwicGx1Z2lucyI6W1siQ2hyb21lIFBERiBQbHVnaW4iLCJQb3J0YWJsZSBEb2N1bWVudCBGb3JtYXQiLFtbImFwcGxpY2F0aW9uL3gtZ29vZ2xlLWNocm9tZS1wZGYiLCJwZGYiXV1dLFsiQ2hyb21lIFBERiBWaWV3ZXIiLCIiLFtbImFwcGxpY2F0aW9uL3BkZiIsInBkZiJdXV0sWyJOYXRpdmUgQ2xpZW50IiwiIixbWyJhcHBsaWNhdGlvbi94LW5hY2wiLCIiXSxbImFwcGxpY2F0aW9uL3gtcG5hY2wiLCIiXV1dXSwiY2FudmFzIjoiOTZhMjk2ZDIyNGYyODVjNjdiZWU5M2MzMGY4YTMwOTE1N2YwZGFhMzVkYzViODdlNDEwYjc4NjMwYTA5Y2ZjNyIsIndlYmdsIjoiOThjZTQyZGVlZjUxZDQwMjY5ZDU0MmY1MzE0YmVmMmM3NDY4ZDQwMWFkNWQ4NTE2OGJmYWI0YzAxMDhmNzVmNyIsIndlYmdsVmVuZG9yQW5kUmVuZGVyZXIiOiJJbnRlbCBJbmMufkludGVsKFIpIElyaXMoVE0pIFBsdXMgR3JhcGhpY3MgNjU1IiwiYWRCbG9jayI6dHJ1ZSwiaGFzTGllZExhbmd1YWdlcyI6ZmFsc2UsImhhc0xpZWRSZXNvbHV0aW9uIjpmYWxzZSwiaGFzTGllZE9zIjpmYWxzZSwiaGFzTGllZEJyb3dzZXIiOmZhbHNlLCJ0b3VjaFN1cHBvcnQiOlswLGZhbHNlLGZhbHNlXSwiZm9udHMiOlsiQW5kYWxlIE1vbm8iLCJBcmlhbCIsIkFyaWFsIEJsYWNrIiwiQXJpYWwgSGVicmV3IiwiQXJpYWwgTmFycm93IiwiQXJpYWwgUm91bmRlZCBNVCBCb2xkIiwiQXJpYWwgVW5pY29kZSBNUyIsIkNvbWljIFNhbnMgTVMiLCJDb3VyaWVyIiwiQ291cmllciBOZXciLCJHZW5ldmEiLCJHZW9yZ2lhIiwiSGVsdmV0aWNhIiwiSGVsdmV0aWNhIE5ldWUiLCJJbXBhY3QiLCJMVUNJREEgR1JBTkRFIiwiTWljcm9zb2Z0IFNhbnMgU2VyaWYiLCJNb25hY28iLCJQYWxhdGlubyIsIlRhaG9tYSIsIlRpbWVzIiwiVGltZXMgTmV3IFJvbWFuIiwiVHJlYnVjaGV0IE1TIiwiVmVyZGFuYSIsIldpbmdkaW5ncyIsIldpbmdkaW5ncyAyIiwiV2luZ2RpbmdzIDMiXSwiYXVkaW8iOiIxMjQuMDQzNDU4MDg4NzM3NjgifQ.mh2bTPBheFXWyMe0KgeXfawaKYjrY78pSxAX9-0oDHI',
    'origin': 'https://www.wego.ae',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.wego.ae/en/flights/searches/RUH-JED-2020-02-17:JED-RUH-2020-02-21/economy/1a:0c:0i?sort=price&order=asc',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
    'cookie': 'AWSALB=pd7gd/4tjzaJxI0tXy0+qfNxo4uQJC6KFSThQ9mZY8a6z8HawFNluliGNq4hJLl/f+p1d+HJm7ykqRjWQkANUB7QumhiyGDTQTpCa64Z+8QWoEEfxi6F64eq7Vwd',
}

params = (
    ('currencyCode', 'AED'),
    ('locale', 'en'),
)

data = '{"search":{"cabin":"economy","deviceType":"DESKTOP","appType":"WEB_APP","userLoggedIn":false,"adultsCount":1,"childrenCount":0,"infantsCount":0,"siteCode":"AE","currencyCode":"AED","locale":"en","legs":[{"departureAirportCode":"RUH","arrivalAirportCode":"JED","outboundDate":"2020-02-17"},{"departureAirportCode":"JED","arrivalAirportCode":"RUH","outboundDate":"2020-02-21"}]},"offset":0,"paymentMethodIds":[10,15],"providerTypes":[]}'

response = requests.post('https://srv.wego.com/v3/metasearch/flights/searches', headers=headers, params=params, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://srv.wego.com/v3/metasearch/flights/searches?currencyCode=AED&locale=en', headers=headers, data=data)
search_id=json.loads(response.content)
print(search_id.get("search").get("id"))
search_id = search_id.get("search").get("id")

headers = {
    'authority': 'srv.wego.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'doorkey': 'Bearer wego-eyJhbGciOiJIUzI1NiIsInR5cGUiOiJKV1QifQ.eyJyZWZlcnJlciI6Imh0dHBzOi8vd3d3LndlZ28uYWUiLCJob3N0Ijoid3d3LndlZ28uYWUiLCJ1YSI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE0XzYpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83OS4wLjM5NDUuMTMwIFNhZmFyaS81MzcuMzYiLCJhY2NlcHQiOiIqLyoiLCJjb3VudHJ5X2NvZGUiOiJJTiIsImFjY2VwdF9lbmNvZGluZyI6Imd6aXAsIGRlZmxhdGUsIGJyIiwiYWNjZXB0X2xhbmd1YWdlIjoiZW4tR0IsZW4tVVM7cT0wLjksZW47cT0wLjgscGw7cT0wLjcsZGU7cT0wLjYiLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xNF82KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzkuMC4zOTQ1LjEzMCBTYWZhcmkvNTM3LjM2IiwibGFuZ3VhZ2UiOiJlbi1HQiIsImNvbG9yRGVwdGgiOjI0LCJkZXZpY2VNZW1vcnkiOjgsImhhcmR3YXJlQ29uY3VycmVuY3kiOjgsInNjcmVlblJlc29sdXRpb24iOls5MDAsMTQ0MF0sImF2YWlsYWJsZVNjcmVlblJlc29sdXRpb24iOls5MDAsMTQ0MF0sInRpbWV6b25lT2Zmc2V0IjotMzMwLCJ0aW1lem9uZSI6IkFzaWEvQ2FsY3V0dGEiLCJzZXNzaW9uU3RvcmFnZSI6dHJ1ZSwibG9jYWxTdG9yYWdlIjp0cnVlLCJpbmRleGVkRGIiOnRydWUsImFkZEJlaGF2aW9yIjpmYWxzZSwib3BlbkRhdGFiYXNlIjp0cnVlLCJjcHVDbGFzcyI6Im5vdCBhdmFpbGFibGUiLCJwbGF0Zm9ybSI6Ik1hY0ludGVsIiwicGx1Z2lucyI6W1siQ2hyb21lIFBERiBQbHVnaW4iLCJQb3J0YWJsZSBEb2N1bWVudCBGb3JtYXQiLFtbImFwcGxpY2F0aW9uL3gtZ29vZ2xlLWNocm9tZS1wZGYiLCJwZGYiXV1dLFsiQ2hyb21lIFBERiBWaWV3ZXIiLCIiLFtbImFwcGxpY2F0aW9uL3BkZiIsInBkZiJdXV0sWyJOYXRpdmUgQ2xpZW50IiwiIixbWyJhcHBsaWNhdGlvbi94LW5hY2wiLCIiXSxbImFwcGxpY2F0aW9uL3gtcG5hY2wiLCIiXV1dXSwiY2FudmFzIjoiOTZhMjk2ZDIyNGYyODVjNjdiZWU5M2MzMGY4YTMwOTE1N2YwZGFhMzVkYzViODdlNDEwYjc4NjMwYTA5Y2ZjNyIsIndlYmdsIjoiOThjZTQyZGVlZjUxZDQwMjY5ZDU0MmY1MzE0YmVmMmM3NDY4ZDQwMWFkNWQ4NTE2OGJmYWI0YzAxMDhmNzVmNyIsIndlYmdsVmVuZG9yQW5kUmVuZGVyZXIiOiJJbnRlbCBJbmMufkludGVsKFIpIElyaXMoVE0pIFBsdXMgR3JhcGhpY3MgNjU1IiwiYWRCbG9jayI6dHJ1ZSwiaGFzTGllZExhbmd1YWdlcyI6ZmFsc2UsImhhc0xpZWRSZXNvbHV0aW9uIjpmYWxzZSwiaGFzTGllZE9zIjpmYWxzZSwiaGFzTGllZEJyb3dzZXIiOmZhbHNlLCJ0b3VjaFN1cHBvcnQiOlswLGZhbHNlLGZhbHNlXSwiZm9udHMiOlsiQW5kYWxlIE1vbm8iLCJBcmlhbCIsIkFyaWFsIEJsYWNrIiwiQXJpYWwgSGVicmV3IiwiQXJpYWwgTmFycm93IiwiQXJpYWwgUm91bmRlZCBNVCBCb2xkIiwiQXJpYWwgVW5pY29kZSBNUyIsIkNvbWljIFNhbnMgTVMiLCJDb3VyaWVyIiwiQ291cmllciBOZXciLCJHZW5ldmEiLCJHZW9yZ2lhIiwiSGVsdmV0aWNhIiwiSGVsdmV0aWNhIE5ldWUiLCJJbXBhY3QiLCJMVUNJREEgR1JBTkRFIiwiTWljcm9zb2Z0IFNhbnMgU2VyaWYiLCJNb25hY28iLCJQYWxhdGlubyIsIlRhaG9tYSIsIlRpbWVzIiwiVGltZXMgTmV3IFJvbWFuIiwiVHJlYnVjaGV0IE1TIiwiVmVyZGFuYSIsIldpbmdkaW5ncyIsIldpbmdkaW5ncyAyIiwiV2luZ2RpbmdzIDMiXSwiYXVkaW8iOiIxMjQuMDQzNDU4MDg4NzM3NjgifQ.mh2bTPBheFXWyMe0KgeXfawaKYjrY78pSxAX9-0oDHI',
    'origin': 'https://www.wego.ae',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.wego.ae/en/flights/searches/RUH-JED-2020-02-17:JED-RUH-2020-02-21/economy/1a:0c:0i?sort=price&order=asc',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
    #'cookie': 'AWSALB=hJj349aRqCB9banD+XfyV1B4tlmFlw7WcF1wyKyUCJVkmSXTVX4BtGhvrUT+15tlveQot7JwsZ0O7Bf0WdV3vH/mgTqfZSnc/KcG4wimPzHvCJKrU0VXZv4Hfzb0',
}

params = (
    ('currencyCode', 'AED'),
    ('locale', 'en'),
    ('paymentMethodIds/[/]', ['10', '15']),
    ('offset', '5399'),
)
time.sleep(2)
response = requests.get('https://srv.wego.com/v3/metasearch/flights/searches/'+search_id+'/results?currencyCode=AED&locale=en&paymentMethodIds[]=10&paymentMethodIds[]=15&offset=5399', headers=headers)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://srv.wego.com/v3/metasearch/flights/searches/f63488a5f0950a05/results?currencyCode=AED&locale=en&paymentMethodIds\[\]=10&paymentMethodIds\[\]=15&offset=5399', headers=headers)
# print(response.content)
fare_details = json.loads(response.content)
print(fare_details.get("fares")[0])