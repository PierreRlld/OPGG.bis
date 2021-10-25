from main import pl, plsearch

def fonc_url(username):
    return "https://euw.op.gg/summoner/userName="+username
#print(fonc_url(plsearch[0]))

URL=fonc_url(plsearch[0])

import requests
from bs4 import BeautifulSoup

test=requests.get("https://euw.op.gg/summoner/userName=PIERR0%20LA%20RAFALE")

page = requests.get(URL).text
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())
L=list(soup.select(".GameItemList .GameItemWrap"))
print(len(L))

table = soup.find("div", {"class": "GameItemList"})
gl = table.find_all("div", {"class": "GameItemWrap"})

results = soup.find(class="Content")
game_elements = results.find_all("div", class_="GameItemList")

"""
import requests
from bs4 import BeautifulSoup

data = requests.get("https://euw.op.gg/champion/leblanc/statistics/mid/build")
soup = BeautifulSoup(data.text, "html.parser")
table = soup.find_all("table", {"class": "champion-overview__table"})
tbody = table[1].find("tbody")
tr = tbody.find_all("tr", {"class": "champion-overview__row"})
"""

#https://www.scrapingbee.com/blog/selenium-python/
#https://www.codetd.com/en/article/8416771