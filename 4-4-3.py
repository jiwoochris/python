from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'

import pandas as pd
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urlopen(req) as doc:
    html = BeautifulSoup(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]
    print(last_page)