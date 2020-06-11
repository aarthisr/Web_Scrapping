import requests

headers = {
    'accept': 'application/json',
    'Referer': 'https://clivecoffee.com/collections/espresso-machines?',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Sec-Fetch-Mode': 'cors',
    'content-type': 'application/x-www-form-urlencoded',
}

params = (
    ('x-algolia-agent', 'Algolia for vanilla JavaScript (lite) 3.32.1;instantsearch.js (3.4.0);Vue (2.5.17);Vue InstantSearch (2.0.1);JS Helper (2.27.0)'),
    ('x-algolia-application-id', 'SONPDQSKHJ'),
    ('x-algolia-api-key', 'd3dc719c40f0d1b7e798735e5dce3399'),
)

data = {
  '{"requests":[{"indexName":"shopify_products_most_reviews_desc","params":"query': '',
  'maxValuesPerFacet': '20',
  'page': '1',
  'highlightPreTag': '__ais-highlight__',
  'highlightPostTag': '__/ais-highlight__',
  'filters': 'collections:espresso-machines',
  'facets': '["tags","vendor"]',
  'tagFilters': '"}]}'
}

response = requests.post('https://sonpdqskhj-dsn.algolia.net/1/indexes/*/queries', headers=headers, params=params, data=data)

response = requests.post('https://sonpdqskhj-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.32.1;instantsearch.js (3.4.0);Vue (2.5.17);Vue InstantSearch (2.0.1);JS Helper (2.27.0)&x-algolia-application-id=SONPDQSKHJ&x-algolia-api-key=d3dc719c40f0d1b7e798735e5dce3399', headers=headers, data=data)
print(response.content)