from main import pl, plsearch

def fonc_url(username):
    return "https://euw.op.gg/summoner/userName="+username
#print(fonc_url(plsearch[0]))

URL=fonc_url(plsearch[0])

import requests
from bs4 import BeautifulSoup

test=requests.get("https://euw.op.gg/summoner/userName=PIERR0+LA+RAFALE")

page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
table = soup.find("div", {"class": "GameItemList"})
gl = table.find_all("div", {"class": "GameItemWrap"})

results = soup.find(class="Content")
game_elements = results.find_all("div", class_="GameItemList")

#==========
#test 
"""
import requests
from bs4 import BeautifulSoup

data = requests.get("https://euw.op.gg/champion/leblanc/statistics/mid/build")
soup = BeautifulSoup(data.text, "html.parser")
table = soup.find_all("table", {"class": "champion-overview__table"})
tbody = table[1].find("tbody")
tr = tbody.find_all("tr", {"class": "champion-overview__row"})
"""