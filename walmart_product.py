import requests
import re
import json
import time

f=open("static/walmart_missing_seed.json", "r")
of=open('wal_dump','w')
for url in f:
    print(url.replace("\n",""))
    dic = {}
    headers = {
        'authority': 'www.walmart.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    response = requests.get(url.replace("\n",""))
    description_more = re.search('prod-ProductHighlights-description.*?>(.*?)</div>',str(response.content))
    description= re.search(
        'itemprop="description">\s*(.*?)\s*</div>',
        str(response.content))
    dic["url"]=url.replace("\n","")
    if description_more:
        dic["description_more"]=description_more.group(1)
    else:
        print("no description_more")
    print("-----------------------")
    if description:
        dic["description"]=description.group(1)
    else:
        print("no description")
    print("-----------------------")
    AboutThisBundle = re.search(
        'class="About.*?-description.*?>\s*(.*?)\s*</div>',
        str(response.content))
    if AboutThisBundle:
        dic["AboutThisBundle"]=AboutThisBundle.group(1)
    else:
        print("no AboutThisBundle")
    AboutThisBundle = re.findall(
        '<li>(.*?)</li>',
        str(response.content))
    if AboutThisBundle:
        dic["Allli"] = AboutThisBundle
    else:
        print("no AboutThisBundle")
    print(json.dumps(dic))
    of.write(json.dumps(dic))
    of.write("\n")
