import requests

f1 = open("static/dsp.html","w+")

headers = {
    'authority': 'www.dickssportinggoods.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'none',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
}

response = requests.get('https://www.dickssportinggoods.com/p/nike-womens-epic-react-flyknit-2-running-shoes-18nikwpcrctflykntrnna/18nikwpcrctflykntrnna', headers=headers)
print(response.content)
f1.write(str(response.content) + "\n")
