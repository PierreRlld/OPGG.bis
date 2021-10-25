from main import pl, plsearch

def fonc_url(username):
    return "https://euw.op.gg/summoner/userName="+username
#print(fonc_url(plsearch[0]))

URL=fonc_url(plsearch[0])

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#setup
DRIVER_PATH = 'C:/chromedriver/chromedriver.exe'
ser=Service(DRIVER_PATH)                #Because of a DeprecationWarning : "executable_path has been deprecated, please use in a Service Object"
driver = webdriver.Chrome(service=ser)

#main : 
driver.get(URL)
game_list=driver.find_element(By.CLASS_NAME, 'GameItemList')
games=game_list.find_elements(By.CLASS_NAME, 'GameItemWrap')

champs=[]

for game in games :
    champion=game.find_element(By.CLASS_NAME, 'ChampionName')
    champs.append(champion.text)
print(champs)

time.sleep(1) #sinon ferme dès que ça charge quand y'a rien après
driver.quit()


