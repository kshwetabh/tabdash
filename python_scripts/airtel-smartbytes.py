import urllib2
from bs4 import BeautifulSoup

def getSmartByteData():
    smartbyte_url = "http://122.160.230.125:8080/gbod/gb_on_demand.do"
    remaining = {}

    request = urllib2.urlopen(smartbyte_url)
    data = request.read()
    soup = BeautifulSoup(data, "html.parser")

    gb_data = soup.select("div.detail > p > span")
    remaining["remaining_data"] = gb_data[0]
    remaining["remaining_days"] = gb_data[2]

    return remaining

# getSmartByteData()