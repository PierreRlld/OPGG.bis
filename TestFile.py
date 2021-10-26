# ============
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from datacollectorv2 import modif, fonc_url, player_list

#setup =======
DRIVER_PATH = 'C:/chromedriver/chromedriver.exe'
ser=Service(DRIVER_PATH)                #Because of a DeprecationWarning : "executable_path has been deprecated, please use in a Service Object"
driver = webdriver.Chrome(service=ser)

# ===========
#var=['Champion','Result','CS','CSmin','Kills','Deaths','Assists','KDA','GameId']

username='Nobusuke'
name=modif(username)    # vvv
URL=fonc_url(name)   # URL SETUP
driver.get(URL)

#1
try : 
    cookies=driver.find_element(By.CLASS_NAME, 'css-1ey59fx')
    cookies.click()
except :
    pass

gametype='Normale'
game_list=driver.find_element(By.CLASS_NAME, 'GameItemList')    # "Block" of all games > should be extented to maximise the number of games located
games=game_list.find_elements(By.CLASS_NAME, 'GameItemWrap')    # Each game is now a selenium element

"""
===> Objectif : obtenir qui de nos potes jouaient avec nous
"""

lp=[]
for game in games :
    if game.find_element(By.CLASS_NAME,'GameType').text==gametype :
        team=game.find_element(By.CLASS_NAME,'Team')
        tl=[]
        tl.append(team.text)
        """
        for player in team :
            if (player.text in player_list):
                tl.append(player.text)
            else:
                pass
        """
        lp.append(tl)
    else: 
        pass
print(lp)

"""
result : 
[['Urgot\nYoungFlexx\nRammus\nZeroDreams\nVex\nTernauwies\nAshe\nChasMl�l\nMorgana\nZulrah'], ["Fiora\nNobusuke\nKha'Zix\nMainADC420\nYasuo\nEsterrrr2\nKai'Sa\nCharLoRamBo\nThresh\nNicolasFgrx"], ['Gnar\nchtis sournois\nQiyana\nTITO LA TORPILLE\nTwisted Fate\nAhr� God\nLucian\nNobusuke\nRell\nPIERR0 LA RAFALE']]
"""