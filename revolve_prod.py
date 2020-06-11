import requests

# cookies = {
#     'JSESSIONID2': 'B26B00C74A27B863BBD1ECC26EC8371B.tc-atom_tomcat2',
#     'viewNumR1': '100',
#     'isPopupEnabledR1': 'true',
#     'pocketViewR1': 'front',
#     'searchMobileFilterByR1': '',
#     'sizeFilterByR1': '',
#     'shoeSizeFilterByR1': '',
#     'topSizeFilterByR1': '',
#     'bottomSizeFilterByR1': '',
#     'handbagFilterByR1': '',
#     'heelFilterByR1': '',
#     'riseFilterByR1': '',
#     'colorFilterByR1': '',
#     'priceFilterByR1': '',
#     'percentFilterByR1': '',
#     'currency': 'USD',
#     'currencyOverride': 'INR',
#     'userLanguagePref': 'en',
#     'fontsLoaded': '1',
#     'originalsource': '',
#     'remarketing': 'TypeA',
#     'optimizelyEndUserId': 'oeu1562070770342r0.5948454248153678',
#     'abNTF': 'variationTwo',
#     '_ga': 'GA1.2.631383387.1562070771',
#     '_gid': 'GA1.2.749177349.1562070771',
#     'crdl_revolvebID': '598707af-0a41-4f83-bb6b-17fc2e7c19a2',
#     'crdl_revolveaID': 'anonimTCYOlNeZMhZY5e2LawRz',
#     '_scid': 'ff1ce937-3941-4173-a46f-51e9caad7f8b',
#     '_fbp': 'fb.1.1562070772431.614333041',
#     'rskxRunCookie': '0',
#     'rCookie': 'btot4ucs8cwsci6xwhqa',
#     '_sctr': '1|1562005800000',
#     'lc_sso2506231': '1562070775132',
#     '__lc.visitor_id.2506231': 'S1562070774.9696758e58',
#     'userClosedNtfDialogCount': '1',
#     'userLastSeenNtfDialogDate': '2019-07-02',
#     'userSeenNtfDialogDate': '2019-07-02',
#     'visitor-cookie1': '2193484459',
#     'visitor-cookie30': '2193484459',
#     'sortByR2': 'featured',
#     '_sp_ses.9084': '*',
#     'SSP_AB_StyleFinder_20160425': 'Test',
#     'SSP_AB_StyleFinderPhase_20160425': 'Phase2',
#     'ntfPopupSuppressionCount': '4',
#     '_sp_id.9084': '9f0c6410-73c0-4d20-a072-396261b3ba0d.1562070789.1.1562070818.1562070789.dd03fe67-3ba8-4a48-857d-adefb4c54a0a',
#     'bb_PageURL': '%2Fcontent%2Fproducts%2Fapplicable-filters%2F%3F%26url%3Dhttps%253A%252F%252Fwww.revolve.com%252Fjackets-coats%252Fbr%252Fe4012a%252F%253Fnavsrc%253Dsubclothing',
#     'browserID': 'fu3RYrAMfAJ5O2ZiAPbQymJS5DzAjT',
#     'lastRskxRun': '1562070818078',
# }

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'https://www.revolve.com/jackets-coats/br/e4012a/?navsrc=subclothing',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
}

# params = (
#     ('d', 'Womens'),
#     ('page', '1'),
#     ('lc', '1'),
#     ('itrownum', '1'),
#     ('itcurrpage', '1'),
#     ('itview', '01'),
# )

# response = requests.get('https://www.revolve.com/pistola-camilo-jacket/dp/PSTL-WO3/', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.revolve.com/pistola-camilo-jacket/dp/PSTL-WO3/?d=Womens&page=1&lc=1&itrownum=1&itcurrpage=1&itview=01', headers=headers, cookies=cookies)
response = requests.get('https://www.revolve.com/pistola-camilo-jacket/dp/PSTL-WO3/?d=Womens&page=1&lc=1&itrownum=1&itcurrpage=1&itview=01', headers=headers)
print(response.content)
html_dump = open("revolve_prod.html", "w+")
html_dump.write(str(response.content))
