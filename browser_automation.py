import re, random, time, urllib
import requests,json, csv, sys, sha1
import openpyxl
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *


class Lazada_Indonesia():
    def __init__(self):
        option = webdriver.ChromeOptions()
        chrome_prefs = {}
        option.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
        # self.proxy = "103.19.59.50:3128"
        # option.add_argument('--proxy-server=%s' % self.proxy)
        self.browser = webdriver.Chrome(executable_path='/Users/aarthi/Documents/softwares/chromedriver', chrome_options=option)

    def browser_auto(self,q):
        headers= {
            'authority': 'www.lazada.sg',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
        }
        self.browser.header_overrides = headers
        self.browser.get("https://www.lazada.co.id/")
        url = "https://www.lazada.co.id/catalog/?&q=" + q
        self.browser.get(url)
        if "<title>captcha |" not in str(self.browser.page_source):
            data=re.search("<script>window.pageData=(.*?)</script>", self.browser.page_source)
        else:
            print("ba captcha")
            self.tearDown()
            sys.exit()
        headers['cookie']=""
        for c in self.browser.get_cookies():
            print(c.get('name'),c.get('value'))
            headers['cookie'] = headers['cookie'] + c.get('name') + "=" + c.get('value') + "; "
        return headers

    def req_module(self,headers, page,q):
        # q = "dark chocolate"
        headers = {
            'authority': 'www.lazada.sg',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json, text/plain, */*',
            'x-umidtoken': 'TE869C96C9CF6738187AB250B199C3BD4DA1CFBF4692530833BDCDFA76F',
            'x-csrf-token': 'e587df88edeee',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'x-ua': '124#PQ9jy0E6xG0xAqSKnJp6neKVVpoxsYdVWTVtyWkTXpXZVL668GPaUsDpV5pJb/xCEehsY5zizPmRBh2xpzKMM2YKLShQsZZaCCOte9vqzB+xTmhGuQAZgACbw+K2canTkdvxzND3y60M1bBL7PGoeyoV7am1Ld84VYO8g1+fdawg++9i3mW/HLarzBJ2VFYcERlxNrQA3WvcrtfZw8nE4m+N7yywdNHH/F+4ozWp9WcVpT0XJXtlsz0fq1XSrFacZJBzEVx7eZ2ZlMan6KvBIZYLlm92HL5PwYHlgTSd7ZeZlULJ4W4D7C9plmI4mfWZIqbtg5Sd1Z2ZlMXng7OBInYXbw/2m4+ZI8LLgTSo1n2elUX2g7vtIZ/plw/IHScRIMY+g/Md1ZIef2SGSfvteCYLlwY2LJ5xdiUnv/yUx527SX87ozCc4hLZ7aS/ik+VIXdfgaaXx5+EdTrs+HOR2Ultn6+6Ejy8BWKY3dAs+reePBkBC7QD0Ry6L1PclzFzVBhWYQugX6S/qja8/8lnceDGhebSzOPGEO0nRU9E1YlRVgC4MdbDMKRA879f28jjQpim8v/DUZ2R8b+u4JUSWZmTJWD1xvTSAy63BpCc4l1tirtsQuyRrGrBAfqME6/AFdMdaO/w0GehNlq+zrKKMQzCu94Qj75lutYW6dPV7MmNoMG0P3vvj6CEHeeY2VGsbvRyulCgeL6jpcRg4/yH/y7YRn27EFRcvRrWq+ucBAfzDk+3Icds4pWPw2XSazutbj/7ku9kYN+PShcJ7bWwpzmbxpxfRISp2s6qq7IwQjkikaCc43QobKoOhECgpjoW5Gd3o4aDYWg/3txb9jhBHHx1XTBtOiemKtROVnNBLE9zhVgVzbxqyLEBx59QcoBIcDLdYwC26h0q/TFNc+QAm0==',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
            'cookie': headers["cookie"]
        }
        params = (
            ('_keyori', 'ss'),
            ('ajax', 'true'),
            ('from', 'input'),
            ('page', str(page)),
            ('q', q),
            # ('spm', 'a2o4j.home.search.go.')
        )
        headers["referer"]="https://www.lazada.sg/catalog/?page="+str(page)+"&q="+q
        req=requests.Session()
        # req.proxies={'http':'http://'+self.proxy,'https':'https://'+self.proxy}
        response = req.get('https://www.lazada.co.id/catalog/', headers=headers, params=params)
        return response

    def get_extracted_prods(self, response):
        product = {}
        resp = json.loads(response.content)
        print(resp)
        try:
            product["page_no"] = resp.get("mainInfo").get("page")
            print(product["page_no"])
            product_items = resp.get("mods").get("listItems", [])
            product["count"] =resp.get("mainInfo").get("totalResults", 0)
            flag = 0
            for product_id in range(0, len(product_items)):
                flag = 1
                product["product_url"] = product_items[product_id].get("productUrl")
                product["sku"] = product_items[product_id].get("sku") + "_" + product_items[product_id].get("skuId")
                product["retailer"] = "Lazada-Indonesia"
                product["rank"] = int(product["page_no"]) * (product_id + 1)
                product["search_term"] = "detergent"
                product["product_name"] = product_items[product_id].get("name")
                product["brand"] = product_items[product_id].get("brandName")
                product["description"] = product_items[product_id].get("description")
                product["thumbnail"] = product_items[product_id].get("image")
                product["seller_name"] = product_items[product_id].get("sellerName")
                product["stock"] = product_items[product_id].get("inStock")
                product["rating"] = product_items[product_id].get("ratingScore")
                product["no_reviews"] = product_items[product_id].get("review")
                product["available_price"] = product_items[product_id].get("price")
                try:
                    product["mrp"] = product_items[product_id].get("originalPrice")
                    product["discount"] = product_items[product_id].get("discount")
                except:
                    product["mrp"] = available_price
                    product["discount"] = 0
                f1.write(json.dumps(product)+"\n")
        except:
            print("response captcha")
            sys.exit()
            # headers=self.browser_auto(q)
            # self.get_extracted_prods(self.req_module(headers,page,q))
        return flag

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    f1 = "result.json"
    html_dump = open(f1, "w")
    xlsx_file = Path('', 'Sample_Search_terms_Lazada.xlsx')
    wb_obj = openpyxl.load_workbook(xlsx_file)
    wsheet = wb_obj.active
    for row in wsheet.iter_rows():
        for cell in row:
            q=cell.value
            count = 0
            crawl = Lazada_Indonesia()
            headers = crawl.browser_auto(q)
            for page in range(1, 21):
                data = crawl.req_module(headers, page,q)
                flag=crawl.get_extracted_prods(data)
                if flag!=1:
                    break
    self.tearDown()
