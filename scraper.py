import requests
from bs4 import BeautifulSoup

url = "https://www.seloger.com/list.htm?projects=2,5&types=2,1&natures=1,2," \
      "4&places=[{%22divisions%22:[2238]}]&mandatorycommodities=0&enterprise=0&qsVersion=1.0"

req = requests.get(url)




