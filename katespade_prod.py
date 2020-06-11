import requests

headers = {
    'authority': 'www.katespade.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'referer': 'https://www.katespade.com/clothing/dresses-jumpsuits/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pl;q=0.7,de;q=0.6',
    # '$cookie': '__cfduid=dfbd7783c62a387cc66608ae5d529b0481562070555; dwac_cdNociaagnCDoaaac48UbK1jBT=1dx7eqWh1vKPWzf2lAaU2rRJ_xlRwBHW9yg%3D|dw-only|||USD|false|US%2FEastern|true; cqcid=ac5gRMbReE8LyMHWQx52avPjTj; sid=1dx7eqWh1vKPWzf2lAaU2rRJ_xlRwBHW9yg; dwsecuretoken_495c23e097836278a1bd0fab55f847c5=aKOYXKx7iWO0J_oqa7bjwwrsiI-ScaGzTg==; isNewUser=false; dwanonymous_495c23e097836278a1bd0fab55f847c5=ac5gRMbReE8LyMHWQx52avPjTj; __cq_dnt=0; dw_dnt=0; dwsid=OictJlthIFm_f-23xPABvFuyqUWvAOd9xwxVroYHPmLjMShHyFM-_9NhcMxrg_TlkQlRDaJEJbUJHqUiBqnnXg==; customersegment=a; i10c.ss=1562070556406; i10c.uid=1562070556408:7103; __utma=108386968.1502914585.1562070557.1562070557.1562070557.1; __utmc=108386968; __utmz=108386968.1562070557.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gcl_au=1.1.748760683.1562070558; mt.v=2.1547437112.1562070558356; loginErrorMsg=false; dw=1; dw_cookies_accepted=1; __cq_seg=0~0.00\\u211~0.00\\u212~0.00\\u213~0.00\\u214~0.00\\u215~0.00\\u216~0.00\\u217~0.00\\u218~0.00\\u219~0.00; _ga=GA1.2.1502914585.1562070557; _gid=GA1.2.69603982.1562070561; testVersion=versionA; BVBRANDID=80c690f1-031d-468c-9848-ecd0ccd699e5; BVBRANDSID=a1d3fde7-968f-4276-a2f3-aa095c4e2291; sr_cr102_exp=2; _fbp=fb.1.1562070561676.677498930; sr_pik_session_id=c8de60b1-a176-db64-acf4-fa1989894c8d; sr_browser_id=15c904e8-8b2c-4529-a4a4-b7a83505f71b; bounceClientVisit1528v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0A1gIYICmKEVAJrWQMYD2AtkSADQgATjBAgAvkA; IASESSIONID=13e84680f4bf154b7794b875911ff2f4; _mibhv=anon-1562070563385-9903276590_7566; __idcontext=eyJjb29raWVJRCI6IkpWTklMTzJLWUI2Mk4zSFVURFI1TEw0T01WRVVSQkdENlZKUjdHNDY2U0xRPT09PSIsImRldmljZUlEIjoiSlZOSUxPMktZSkVLUlBQVFZIUk5aU05MTUo3Qkg1TUdWVkNEWEVGSTZHWlE9PT09IiwiaXYiOiIzSkNPTkFITkRKQTRFTzNQS0FDTlVPT0UzQT09PT09PSIsInYiOjF9; liveagent_oref=; liveagent_sid=6b548c50-043b-4606-92b3-3bf807ef8b0e; liveagent_vc=2; liveagent_ptid=6b548c50-043b-4606-92b3-3bf807ef8b0e; ub_101=nov=1&fvd=1562070570650&cPid=0&Zp=0&rvCid=ks-clothing-dresses-view-all&lOrdPids=0&ordAmt=0&rvPid=0&lvd=1562070570650&sid=1dx7eqWh1vKPWzf2lAaU2rRJ_xlRwBHW9yg=; __cq_uuid=4bbb25f0-9cc4-11e9-bf11-b1868589b172; stc113829=tsa:1562070561982.1400855212.6082687.8271338203774561.:20190702125951|env:1%7C20190802122921%7C20190702125951%7C3%7C1032238:20200701122951|uid:1562070561982.902388860.8305197.113829.1827473036.:20200701122951|srchist:1032238%3A1%3A20190802122921:20200701122951; _aa7988=1xf690; i10c.uservisit=6; _derived_epik=dj0yJnU9UXMtLUlrTGg2Y2JWM0p2Y1pFZlNtRkZKeGc1TkdIc0Embj1faEdQVGU2REJmOEtJVjlGTl83RE1BJm09MSZ0PUFBQUFBRjBiVGtFJnJtPTEmcnQ9QUFBQUFGMGJUa0U; __CG=u%3A1002556879017457700%2Cs%3A362518184%2Ct%3A1562070599737%2Cc%3A3%2Ck%3Awww.katespade.com%2F53%2F53%2F568%2Cf%3A1%2Ci%3A1; __utmb=108386968.21.9.1562071396721; _gat_UA-20555300-6=1; i10c.bdddb=c2-f0103ZLNqAeI3BH6yYOfG7TZlRtCrMwzKDQfPMtvESnCuVjBtyWjGtjitUxJosswxEpmWHdkESNCtx04RiOfGqfIlRUNpvwqPnlkPolfJSiIRsoms2WeLqeKlRtT3jxvKEOjKMDfJSvUoxo6uXWaGVZkqoAhloxqQlofPwYkJcS6fhQ6tzOgotZkQMtHDyjnA4lkPHeIKNnroxoY8XJKBvefrzwFru4qPnlkPglfJSiIRvjBTuTfbEZkqMupsusvz8qkl7wWr3iHtspjsuTFBve9SHoHqjyTKIPfPM3uiiAioxo6uXOfGvjfq4tMloxqPnlkPcxyESnCuVjBtyUlBvHjrXoHqjxVKDq3fhvfJSiIRsoBs1OftugfqRoMRjxVKDq3BuEMuNnHoyMAoz3aGv4ulRtCrMsvP8tJOPeoESNGw1t6tZSjE0ZkQQxIsjxVOHuiKMDjOQlCtXnGt4OfqujnrMtrpt4uKDQjVLgfM3iHtsolozT7WqeklSRGvjxVKDqBEETbESnCuVm6tZOfG5NQQ9oHqjyTN8qKKMd9TNnHoyM9oz3aGv37lRtCrMsvP8qlKNGwESoCtxjGU; mt.pevt=mr%3Dt1561124144%26mi%3D\'2.1547437112.1562070558356\'%26u%3D\'https://www.katespade.com/clothing/dresses-jumpsuits/\'%26e%3D\\u21(xi)%26ii%3D\\u21(\'4,2,31476,,,,1562070592,2,1562071396\')%26eoq%3D\\u21t',
}

response = requests.get('https://www.katespade.com/products/one-shoulder-midi-dress/NJMUA583.html', headers=headers)
print(response.content)
html_dump = open("katespade_prod.html", "w+")
html_dump.write(str(response.content))