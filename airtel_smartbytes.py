import urllib2
from bs4 import BeautifulSoup
import re

def getSmartByteData():
    smartbyte_url = "http://122.160.230.125:8080/gbod/gb_on_demand.do"
    remaining = {}

    request = urllib2.urlopen(smartbyte_url)
    data = request.read()
    soup = BeautifulSoup(data, "html.parser")

    gb_data = soup.select("div.detail > p > span")
    remaining["remaining_data"] = re.sub("[^0-9.]", "", gb_data[0].text)
    remaining["remaining_days"] = re.sub("[^0-9]", "", gb_data[2].text)
    remaining["remaining_pct"] = format(float(remaining["remaining_data"]) * 100/ 105, '.0f')

    print remaining
    return remaining

# getSmartByteData()