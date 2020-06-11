import requests

headers = {
    'authority': 'www.notebooksbilliger.de',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'referer': 'https://www.notebooksbilliger.de/notebooks',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
}

response = requests.get('https://www.notebooksbilliger.de/asus+vivobook+s406ua+bm013t', headers=headers)
print(response)
html_dump = open("notebooksbilliger_prod.html", "w+")
html_dump.write(str(response.content))
