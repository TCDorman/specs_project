import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from server import webscraper

headers = {"Accept-Language": "en-US, en;1=0.5"}
url = "https://en.wikipedia.org/wiki/" + "Diego Mainz"
print(url)
results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")

print(soup.prettify())
personal_info = []
Club_Career = []
Granada = []
International_Career = []

wiki_div = soup.find_all('div', class_='mw-parser-output')

for container in wiki_div:
    name = container.p.b.text
    personal_info.append(name)

    more_info = container.p.text
    personal_info.append(more_info)

print(personal_info)

