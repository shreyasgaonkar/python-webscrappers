"""Scrap data entry values into CSV"""

import re
import csv
import time
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://sulphuric-acid.com/Sulphuric-Acid-on-the-Web/Acid%20Plants/Acid_Plant_Index.htm'

NEW_URL = re.split(r'(\/)', BASE_URL)

MAIN_SOURCE = requests.get(BASE_URL).text
SOUP_MAIN = BeautifulSoup(MAIN_SOURCE, 'lxml')

ALL_LINKS = SOUP_MAIN.select('#page_content > table')


def get_company_data(href):
    """Get company info and feed into CSV"""
    print(f"Getting: {href.encode('utf-8')}")
    source = requests.get(href).text
    soup = BeautifulSoup(source, 'lxml')

    tr_key = soup.select('#page_content > table > tr > td:nth-of-type(1)')
    tr_value = soup.select('#page_content > table > tr > td:nth-of-type(2)')

    for i, j in enumerate(tr_key):
        tr_key[i] = j.text.strip()

    for i, j in enumerate(tr_value):
        tr_value[i] = re.sub(r'\s+', ' ', j.text.strip()).encode('utf-8').decode('utf-8')

    with open('results.csv', 'a', encoding='utf-8') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(tr_key)
        csv_writer.writerow(tr_value)


for a in ALL_LINKS[0].find_all('a', href=True):
    time.sleep(0.5)
    url = (f"{''.join(NEW_URL[:-1])}{a['href']}")
    try:
        get_company_data(url)
    except Exception as exp:
        print(f"Error fetching URL: {url}")
        print(exp)
