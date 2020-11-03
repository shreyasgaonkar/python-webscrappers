import datetime
import time
from bs4 import BeautifulSoup
import requests

URL = 'https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html'

source = requests.get(URL).text

soup = BeautifulSoup(source, 'lxml')
rate = soup.find('div')

try:
    score = (soup.select("div.mwsgeneric-base-html > p:nth-of-type(7)")[0].text)
    print(score)
except:
    print("Unable to parse website for current rate. Check CSS tag names from https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html")
