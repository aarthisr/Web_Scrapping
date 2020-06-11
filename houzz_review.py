import requests

headers = {
    'cookie': 'v=1563771484_9a38c298-5714-4800-a343-b42890a2ab1e_fe1aa665688585fc671088b5655302eb; vct=en-US-vxlcQjVdXBtcQjVd; _ga=GA1.2.1229315018.1563771505; _gcl_au=1.1.1278093668.1563771508; cto_lwid=ca679601-30e1-4e56-9150-5b04286c2eed; _fbp=fb.1.1563771515858.862859726; _csrf=yfggVZBlFfeY3khXktbXAl6c; ns=3; jsq=; prf=generalFilter%7C%7D17; documentWidth=1440; IR_gbd=houzz.com; can=0; jdv=1%2BDTkRe96RjavWNQ; _gid=GA1.2.1109913048.1565087734; _gat=1; IR_5454=1565088354501%7C0%7C1565087738164%7C%7C; QSI_HistorySession=https%3A%2F%2Fwww.houzz.com%2Fproducts%2Fliving-room%2Fcoffee-tables-prbr1-br~t_532~a_1268-24713453~1564734702472%7Chttps%3A%2F%2Fwww.houzz.com%2Fproducts%2Fbeginnings-corner-desk-cinnamon-cherry-prvw-vr~7397150~1565087737801%7Chttps%3A%2F%2Fwww.houzz.com%2Fproducts%2Fbeginnings-corner-desk-cinnamon-cherry-prvw-vr~7397150~1565088354731; hzd=5b977294-19b5-4552-8a68-456514f53818%3A2%3A%3Areview_sort%3A%3ANewest',
    'origin': 'https://www.houzz.com',
    'accept-encoding': 'gzip, deflate, br',
    'x-csrf-token': 'XGtTYrSf-Bn9pC231rBLgrSuw0YXN3Eh_X6o',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
    'x-requested-with': 'XMLHttpRequest',
    'x-hz-view-mode': 'null',
    'pragma': 'no-cache',
    'rrid': '5b977294-19b5-4552-8a68-456514f53818',
    'x-hz-request': 'true',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'www.houzz.com',
    'referer': 'https://www.houzz.com/products/beginnings-corner-desk-cinnamon-cherry-prvw-vr~7397150',
}

data = {
  'spaceId': '7397150',
  'fromItem': '0',
  'numItems': '1',
  'sortType': '2',
  'rating': ''
}

resp = requests.post('https://www.houzz.com/j/getProductReviews', headers=headers, data=data)

print(resp)
print(resp.content)
html_dump = open("houzz.html", "w+")
html_dump.write(str(resp.content))