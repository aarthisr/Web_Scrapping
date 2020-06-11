import requests

# cookies = {
#     'tgw_l7_route': 'bade2719c4f699ac60a6ba17544e8561',
#     'iplocation': '%e4%b8%8a%e6%b5%b7%e5%b8%82%7c0%7c0',
#     'Hm_lvt_fd8a2efc13affa8f68d5420fa8d56dcb': '1560865030',
#     'Hm_lpvt_fd8a2efc13affa8f68d5420fa8d56dcb': '1560865030',
# }

headers = {
    'Pragma': 'no-cache',
    'Origin': 'http://www.littlesheep.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'text/plain, */*; q=0.01',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'http://www.littlesheep.com/ResTuarant',
}

data = {
  'SearchStore': '',
  'PageIndex': '1',
  'PageSize': '6',
  'CityId': '4001'
}
# response = requests.post('http://www.littlesheep.com/ResTuarant/_index', headers=headers, cookies=cookies, data=data)
response = requests.post('http://www.littlesheep.com/ResTuarant/_index', headers=headers, data=data)
print(response.content)
html_dump = open("littlesheep.html", "w+")
html_dump.write(str(response.content))