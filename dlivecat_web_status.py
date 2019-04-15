#dlivecat_web_online_test
#https://maker.ifttt.com/trigger/test/with/key/hXmytxHquotaEQw593DchDHxE1y0JqNPOKYJQDGAXIf

import time
import requests
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

var = 1

def webtesting():
    req = Request("https://dlivecat.com")
    try:
        response = urlopen(req)
    except HTTPError as e:
        return ('The server couldn\'t fulfill the request with error code: ', e.code)
    except URLError as e:
        return ('Failed to reach a server with reason:', e.reason)
    else:
        return ('Website is working fine')
        

def application_alert():
    webtesting()
    report = {}
    report["value1"] = webtesting()
    requests.post("https://maker.ifttt.com/trigger/test/with/key/hXmytxHquotaEQw593DchDHxE1y0JqNPOKYJQDGAXIf", data=report) 

while var == 1:
    application_alert()
    time.sleep(10*60)
#webtesting()
#application_alert()
#time.sleep(20)