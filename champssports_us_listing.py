import requests
import json

headers = {
    'authority': 'www.champssports.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6'
}
#
# params = (
#     ('currentPage', '2'),
# )
#
# response = requests.get('https://www.champssports.com/product/nike-air-max-270-react-womens/T6174002.html', headers=headers)
# print(response.content)
# html_dump = open("champssports_us_listing.html", "w+")
# html_dump.write(str(response.content))
#
# #NB. Original query string below. It seems impossible to parse and
# #reproduce query strings 100% accurately so the one below is given
# #in case the reproduced version is not "correct".
# # response = requests.get('https://www.champssports.com/category/sport/running/womens/shoes.html?currentPage=2', headers=headers)
#
#
# headers = {
#     'Referer': 'https://www.champssports.com/product/nike-manoa-mens/54350003.html',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
# }

# params = (
#     ('passkey', 'cazWViSnYHCTQo2y3FAztJNtObxQr0ncomMhRxVVPWiQI'),
#     ('apiversion', '5.5'),
#     ('resource.q0', 'reviews'),
#     ('filter.q0', ['productid:eq:159963']),
# )
params = (
    ('passkey', 'cazWViSnYHCTQo2y3FAztJNtObxQr0ncomMhRxVVPWiQI'),
    ('apiversion', '5.5'),
    # ('displaycode', '8006-en_us'),
    ('resource.q0', 'reviews'),
    ('filter.q0', [ 'productid:eq:303226']),
    # ('sort.q0', 'rating:desc'),
    ('stats.q0', 'reviews'),
    # ('filteredstats.q0', 'reviews'),
    ('include.q0', 'authors,products'),
    # ('filter_reviews.q0', 'contentlocale:eq:en_US'),
    # ('filter_reviewcomments.q0', 'contentlocale:eq:en_US'),
    # ('filter_comments.q0', 'contentlocale:eq:en_US'),
    # ('limit.q0', '8'),
    # ('offset.q0', '0'),
    # ('limit_comments.q0', '3'),
    # ('callback', 'bv_1111_13713'),
)

response = requests.get('https://api.bazaarvoice.com/data/batch.json', headers=headers, params=params)
print(response.content)
html_dump = open("champssports_us_listing.html", "w+")
html_dump.write(str(response.content))
print(json.loads(response.content).get("BatchedResults").get("q0").get("Includes").get("Products").get("303226").get("ReviewStatistics").get("AverageOverallRating"))
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.bazaarvoice.com/data/batch.json?passkey=cazWViSnYHCTQo2y3FAztJNtObxQr0ncomMhRxVVPWiQI&apiversion=5.5&resource.q0=reviews&filter.q0=productid%3Aeq%3A159963', headers=headers)
# print(response.content)
# print(json.loads(response.content).get("BatchedResults").get("q0").get("Includes").get("Products").get("303226").get("ReviewStatistics").get("AverageOverallRating"))



