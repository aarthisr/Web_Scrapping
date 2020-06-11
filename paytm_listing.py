import requests

# cookies = {
#     'tvc_vid': '91576504475897',
#     '_ga': 'GA1.2.1232929201.1576504476',
#     '_gid': 'GA1.2.871586948.1576504476',
#     'cto_lwid': 'f37005ad-3e44-4fa7-a301-58d18c4d1a64',
#     '_fbp': 'fb.1.1576504476323.1576380061',
#     'returning_usr': '1',
#     '_dc_gtm_UA-36768858-21': '1',
# }

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Origin': 'https://paytmmall.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://paytmmall.com/watches_best_of_brands-llpid-198644',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
}

params = (
    ('channel', 'web'),
    ('child_site_id', '6'),
    ('site_id', '2'),
    ('version', '2'),
    ('items_per_page', '32'),
)

data = '{"tracking":{"current_page":"https://paytmmall.com/watches_best_of_brands-llpid-198644","prev_page":""},"context":{"device":{"os":"MacIntel","device_type":"PC","browser_uuid":"GA1.2.1232929201.1576504476","ua":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36","connection_type":"Unknown"},"channel":"WEB","user":{"ga_id":"GA1.2.1232929201.1576504476","user_id":null}}}'

response = requests.post('https://middleware.paytmmall.com/watches_best_of_brands-llpid-198644', headers=headers, params=params, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://middleware.paytmmall.com/watches_best_of_brands-llpid-198644?channel=web&child_site_id=6&site_id=2&version=2&items_per_page=32', headers=headers, cookies=cookies, data=data)
