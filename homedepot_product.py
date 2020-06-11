import requests
import json
import re

headers = {
    'pragma': 'no-cache',
    '$cookie': 'THD_CACHE_NAV_PERSIST=; x-thd-canaveral-assignment=SearchNavRank%3A7%3A1%2CBrowseSort%3A3%3A1; RES_TRACKINGID=55383034193828236; ResonanceSegment=1; s_ecid=MCMID%7C69470383924551955890550272502254406648; _pxvid=92c84fa5-a7cb-11e9-9efc-0242ac120009; cto_lwid=05041453-9e99-4d3d-8f46-85548a8b32cf; _gcl_au=1.1.1804555449.1563282840; ftr_ncd=6; _ga=GA1.2.1628532330.1563282841; aam_mobile=seg%3D1131078; aam_uuid=69219034001955404000560039578354427277; _mibhv=anon-1563282840896-8429901190_4577; _fbp=fb.1.1563282842323.1480318878; WRUID15e=2346392675172403; _abck=30ED6298F88FCB2B6592E5B8B4EEEBB7~0~YAAQDwEkF6McG+FrAQAAHC7r+gKaayqkbpc1CSPK03qSDdqlY/A/VaKV3soWZkvrLcFOxV8SVQ9picX6LZSRAcVYznRMd206FVReqH17PWB8U9pnFN0dj75fK6Yz/EjMPEjOnjrJ/kQuy8GeesPoBVLzoTNp/vmPiJNuLLiIDLh7qbh1CDTBz8ncfmj58vGEOPTQ+U3F+9Kw1V4Lr0HYG9eP62JN3QQTcz+dXYNISflO5RKYUHGxFiITLTL0fUYpik2/pjEIkIsVUJHLgCC5kfOdP+WBD8rBvWRF7L9KTVfWKYMGkXTwetocbAw=~-1~-1~-1; LPVID=U2ZTMxNzM3MmJiZTQ1ZTY0; _br_uid_2=uid%3D6266871018999%3Av%3D12.0%3Ats%3D1563282841618%3Ahc%3D3; __CT_Data=gpv=3&ckp=tld&dm=homedepot.com&apv_4_www23=3&cpv_4_www23=3&rpv_4_www23=3; _derived_epik=dj0yJnU9YkQyN09Ub0dTUUJYZ0lzRzB0QW44d0F2dVVYOC16MUMmbj1kU05jZWxETjdJTlBKQU9uS19kSHZ3Jm09MSZ0PUFBQUFBRjAxVENzJnJtPTEmcnQ9QUFBQUFGMDFUQ3M; ctm={\'pgv\':7754324253864312|\'vst\':1018007906466946|\'vstr\':7792092448704378|\'intr\':1563775431312|\'v\':1|\'lvst\':8181}; HD_DC=origin; bm_sz=D2CC8681D9B97B3F09EE877FE91CA7CD~YAAQPAEkF7NL1U5sAQAAd0j8UQTBoRZSXmqhTlSp9vNhRwBp5XXVClcjmNJt4Q/bZWhV7lBrmAZt0jtmqq9Xh1YhWs/vbLv+DTXC1d3wQ4+lm1mkIfw6l+1J6lvRrdasys65Ae43wzq7Nx5+THqy5Qkre1PwD6Xe7Wl9RKsq42KEmGh6u2PMuhfFFo3d6VkROkNN; check=true; THD_SESSION=; THD_CACHE_NAV_SESSION=; AMCVS_F6421253512D2C100A490D45%40AdobeOrg=1; AMCV_F6421253512D2C100A490D45%40AdobeOrg=-1712354808%7CMCIDTS%7C18111%7CMCMID%7C69470383924551955890550272502254406648%7CMCAAMLH-1565348389%7C7%7CMCAAMB-1565348389%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1564750789s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-940903607%7CvVersion%7C4.3.0; THD_FORCE_LOC=1; THD_INTERNAL=0; WORKFLOW=LOCALIZED_BY_GPS_HIGH; DETA_ZIP=96913; _px=MAgMduJ23Xf4usCezzhJGHyXYavqdHbxNi+5+ROfk4kRBsq6koA9OIeHu18qj+3WdXuVUrrf5HH3TR4Fo1btaA==:1000:k4LlaGXX8tmpsxn+PWEtoS1GFHzIrnEbQVNkGE6CbEp62aOBuCLFMKnuswneDl5iBk/0zTMjbB6MVd0rYhmbia1SNAdLtxWTXv3R2zlQQK08MiegRUQdd7lQoh7SfL/Xp6mN/Z/Nb1ykeSqOzw21/YSj4dcLAyQsxsrAymZeZTazpmX00lCoDVaXsdd1fBjbbUqqq7/XnWiGyEJLMWi4WkNc7mOfKuIjW43kC0xrpupe5chRPPn7yTlRSfU7a02CLUSLPV7XZXTokQM53UaExg==; ak_bmsc=EE4A6D9E12F00B4B20A368E85CABAB151724013CD93A00009F17445D06835D29~plYp1gNIIRxadh5U4C/drDzTvSux5J8Q0sxaVUSvxnE19hCRN3BN/HA7CwypLGfQFqU2PBRgfBNP6PR0Xnzt2hm/lSgatkkuSjl05LkOPx1GGo3jt0n8M9x68FdDMJ9+Q7ayAGK144TJmRjFhwqkSGOBDsL9ATtTEM4EFoZY/Xc20V3EdJs0aIi7I5DfY3WQo/5uHduXxzdmwtL0fRKm80zm/MihAbh7ugH6cqz5XOPug5pzHm/4G278G95p3y77DF; thda.s=80363d9f-1a22-47ca-2b60-c28dfe0e7083; thda.u=5f86cd24-2b3b-298a-1745-9d3a9ff5cd02; THD_PERSIST=C4%3D1710%2BGuam%20-%20Tamuning%20-%20Tamuning%2C%20GU%2B%3A%3BC4_EXP%3D1596279592%3A%3BC24%3D96913%3A%3BC24_EXP%3D1596279592%3A%3BC34%3D32.1%3A%3BC34_EXP%3D1564830001%3A%3BC39%3D1%3B7%3A00-20%3A00%3B2%3B6%3A00-22%3A00%3B3%3B6%3A00-22%3A00%3B4%3B6%3A00-22%3A00%3B5%3B6%3A00-22%3A00%3B6%3B6%3A00-22%3A00%3B7%3B6%3A00-22%3A00%3A%3BC39_EXP%3D1564747192; s_pers=%20s_nr365%3D1564743604618-Repeat%7C1596279604618%3B%20s_dslv%3D1564743604623%7C1659351604623%3B; s_sess=%20stsh%3D%3B%20s_pv_pName%3Dproductdetails%253E308744254%3B%20s_pv_pType%3Dpip%3B%20s_pv_cmpgn%3D%3B%20s_cc%3Dtrue%3B; ats-cid-AM-141099-sid=85695777; forterToken=9dfbb923afd04282b84724f037c25361_1564743604688__UDF43_9ck; IR_gbd=homedepot.com; IR_8154=1564743604746%7C0%7C1564743604746; akaau=1564743917~id=69a34ceebb10d0bc440025e2af7eb3f8; bm_sv=BFB172F1B1D8AC7F4FA499B50C794455~qU+mLRvkY9TZEB3mggGtdKWmWXBBYYsKJ+eI9gpdOOTF1UrejN+lKWYASj1HTzPy+nPacchRJ0Wi/hg6JItCX8BXIPfsuwpHBAw3MPtnbt0frXvZune/DNZ6bqbPaKndkviWKGflBZxY0J8zeJppeRrAY+BYLBhpmvXgtine9mA=; mbox=PC#79b1ec169b9144d491987aa40c89e690.17_69#1627988426|session#cb45aaafcf1e4b0e80b133130e767574#1564745486; tt_billing_name=true; _pxde=6e9311bee1944757280dc41b5dae4891b5259b009962d2217795064e1669bc9b:eyJ0aW1lc3RhbXAiOjE1NjQ3NDM2MjY3MTYsImluY19pZCI6WyJkZjhiZTUzZDBkYTczMDQ4ZWEzYzFmZjViYjgxNTI0YSJdfQ==',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'cache-control': 'no-cache',
    'authority': 'www.homedepot.com',
    'referer': 'https://www.homedepot.com/p/SAUDER-Manhattan-Gate-Mystic-Oak-4-Shelf-Etagere-422385/308744254',
}
seed = open("static/homedepot.json", "r+")
out_json = open("static/homedepot_out_1.json", "w+")
recrawl_json = open("static/homedepot_recrawl.json", "w+")
response = "<Response [404]>"
res = {"url": "", "no_reviews": ""}
for url in seed:
    print(url)
    item_id = re.findall("\/(\d*)",url)
    print(item_id[-1])
    # params = (
    #     ('itemId', item_id[-1]),
    #     ('storeId', '1710'),
    #     ('irgCount', '5'),
    # )
    params = (
        ('anchor', item_id[-1]),
        ('storeid', '1710'),
        ('key', 'x5w9jA8tWVGcqRhujrHTvjRwQfH8MkFc'),
    )
    count = 0
    while True:
        # response = requests.get('https://www.homedepot.com/p/svcs/getProductIrgData/v1', headers=headers, params=params)
        response = requests.get('https://www.homedepot.com/dynamicrecs/fbt', headers=headers, params=params)
        # print(response)
        if str(response) == "<Response [200]>" or count >= 15:
            break
        count += 1
    if count < 15:
        json_content = json.loads(response.content)
        print(json_content)
        # no_reviews = (json_content.get("primary").get("ratingsReviews").get("totalReviews"))
        no_reviews = json_content.get("products")[0].get("reviews")
        print(no_reviews)
        res["url"] = url
        res["no_reviews"] = no_reviews
        out_json.write(json.dumps(res))
        out_json.write("\n")
    else:
        print(url)
        recrawl_json.write(url)
        recrawl_json.write("\n")




# response = requests.get('https://www.homedepot.com/dynamicrecs/fbt', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.homedepot.com/dynamicrecs/fbt?anchor=308737643&storeid=1710&key=x5w9jA8tWVGcqRhujrHTvjRwQfH8MkFc', headers=headers)
