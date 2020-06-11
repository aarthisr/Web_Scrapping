import requests
import json, re
headers = {
    'Referer': 'https://www.officedepot.com/a/products/8442546/Sauder-Carson-Forge-Technology-Pier-Washington/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}

params = (
    ('passkey', 'cawBtQneBQUKVGwTxna9AAvIPFJuUzw9xB3UlOt5DIrC8'),
    ('apiversion', '5.5'),
    ('displaycode', '2563-en_us'),
    # ('resource.q0', 'products'),
    # ('filter.q0', 'id:eq:8442546'),
    # ('stats.q0', 'reviews'),
    # ('filteredstats.q0', 'reviews'),
    # ('filter_reviews.q0', 'contentlocale:eq:en_US'),
    # ('filter_reviewcomments.q0', 'contentlocale:eq:en_US'),
    ('resource.q1', 'reviews'),
    ('filter.q1', ['isratingsonly:eq:false', 'productid:eq:772253', 'contentlocale:eq:en_US']),
    ('sort.q1', 'submissiontime:desc'),
    ('stats.q1', 'reviews'),
    ('filteredstats.q1', 'reviews'),
    # ('include.q1', 'authors,products,comments'),
    # ('filter_reviews.q1', 'contentlocale:eq:en_US'),
    # ('filter_reviewcomments.q1', 'contentlocale:eq:en_US'),
    # ('filter_comments.q1', 'contentlocale:eq:en_US'),
    ('limit.q1', '20'),
    ('offset.q1', '5'),
    # ('limit_comments.q1', '3'),
    # ('resource.q2', 'reviews'),
    # ('filter.q2', ['productid:eq:8442546', 'contentlocale:eq:en_US']),
    # ('limit.q2', '1'),
    # ('resource.q3', 'reviews'),
    # ('filter.q3', ['productid:eq:8442546', 'isratingsonly:eq:false', 'issyndicated:eq:false', 'rating:gt:3', 'totalpositivefeedbackcount:gte:3', 'contentlocale:eq:en_US']),
    # ('sort.q3', 'totalpositivefeedbackcount:desc'),
    # ('include.q3', 'authors,reviews,products'),
    # ('filter_reviews.q3', 'contentlocale:eq:en_US'),
    # ('limit.q3', '1'),
    # ('resource.q4', 'reviews'),
    # ('filter.q4', ['productid:eq:8442546', 'isratingsonly:eq:false', 'issyndicated:eq:false', 'rating:lte:3', 'totalpositivefeedbackcount:gte:3', 'contentlocale:eq:en_US']),
    # ('sort.q4', 'totalpositivefeedbackcount:desc'),
    # ('include.q4', 'authors,reviews,products'),
    # ('filter_reviews.q4', 'contentlocale:eq:en_US'),
    # ('limit.q4', '1'),
)

response = requests.get('https://api.bazaarvoice.com/data/batch.json', params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.bazaarvoice.com/data/batch.json?passkey=cawBtQneBQUKVGwTxna9AAvIPFJuUzw9xB3UlOt5DIrC8&apiversion=5.5&displaycode=2563-en_us&resource.q1=reviews&filter.q1=isratingsonly%3Aeq%3Afalse&filter.q1=productid%3Aeq%3A8442546&filter.q1=contentlocale%3Aeq%3Aen_US&sort.q1=submissiontime%3Adesc&stats.q1=reviews&filteredstats.q1=reviews', headers=headers)
print(response.content)
html_dump = open("officedepot_review.html", "w+")
review_json = (re.search('"BatchedResults":(.*?),"SuccessfulRequests',str(response.content)).group(1))
# resp = json.loads(review_json)
html_dump.write(review_json)

params = (
    ('passkey', 'cawBtQneBQUKVGwTxna9AAvIPFJuUzw9xB3UlOt5DIrC8'),
    ('apiversion', '5.5'),
    ('displaycode', '2563-en_us'),
    ('resource.q0', 'reviews'),
    ('filter.q0', ['isratingsonly:eq:false', 'productid:eq:772253', 'contentlocale:eq:en_US']),
    ('sort.q0', 'submissiontime:desc'),
    ('stats.q0', 'reviews'),
    ('filteredstats.q0', 'reviews'),
    ('include.q0', 'authors,products,comments'),
    ('filter_reviews.q0', 'contentlocale:eq:en_US'),
    ('filter_reviewcomments.q0', 'contentlocale:eq:en_US'),
    ('filter_comments.q0', 'contentlocale:eq:en_US'),
    ('limit.q0', '30'),
    ('offset.q0', '4'),
    ('limit_comments.q0', '3'),
    ('callback', 'bv_1111_26268'),
)

response = requests.get('https://api.bazaarvoice.com/data/batch.json', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api.bazaarvoice.com/data/batch.json?passkey=cawBtQneBQUKVGwTxna9AAvIPFJuUzw9xB3UlOt5DIrC8&apiversion=5.5&displaycode=2563-en_us&resource.q0=reviews&filter.q0=isratingsonly%3Aeq%3Afalse&filter.q0=productid%3Aeq%3A772253&filter.q0=contentlocale%3Aeq%3Aen_US&sort.q0=submissiontime%3Adesc&stats.q0=reviews&filteredstats.q0=reviews&include.q0=authors%2Cproducts%2Ccomments&filter_reviews.q0=contentlocale%3Aeq%3Aen_US&filter_reviewcomments.q0=contentlocale%3Aeq%3Aen_US&filter_comments.q0=contentlocale%3Aeq%3Aen_US&limit.q0=30&offset.q0=4&limit_comments.q0=3&callback=bv_1111_26268', headers=headers)
