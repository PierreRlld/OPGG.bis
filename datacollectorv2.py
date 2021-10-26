from main import pl, plsearch, var

def fonc_url(username):
    return "https://euw.op.gg/summoner/userName="+username
#print(fonc_url(plsearch[0]))

# URL SETUP :
URL=fonc_url(plsearch[1])

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#setup =======
DRIVER_PATH = 'C:/chromedriver/chromedriver.exe'
ser=Service(DRIVER_PATH)                #Because of a DeprecationWarning : "executable_path has been deprecated, please use in a Service Object"
driver = webdriver.Chrome(service=ser)
# ============

driver.get(URL)

try : 
    cookies=driver.find_element(By.CLASS_NAME, 'css-1ey59fx')
    cookies.click()
except :
    pass


#Updating profile but it doesn't seem to be needed
#profile=driver.find_element(By.CLASS_NAME, 'Profile')
#button=profile.find_element(By.CLASS_NAME, 'Buttons')
#button.click()

""" More games """
more=driver.find_element(By.CLASS_NAME, 'GameMoreButton Box')
more.click()

game_list=driver.find_element(By.CLASS_NAME, 'GameItemList')    # "Block" of all games > should be extented to maximise the number of games located
games=game_list.find_elements(By.CLASS_NAME, 'GameItemWrap')    # Each game is now a selenium element

#var=['GameId','Champion','Result','CS','CSmin','Kills','Deaths','Assists','KDA']
gametype='Normale'
L=[]
for game in games : #pb j'ai tous les types de game encore là
    lg=[]
    if game.find_element(By.CLASS_NAME,'GameType').text==gametype :
        lg.append(game.find_element(By.CLASS_NAME,'data-game-id').text)      #gameid
        lg.append(game.find_element(By.CLASS_NAME, 'ChampionName').text)     #champion
        lg.append(game.find_element(By.CLASS_NAME, 'GameResult').text)       #result
        cs=game.find_element(By.CLASS_NAME, 'CS tip')               
        lg.append(cs.text[0:3])     #CS
        csm=cs.text[-2]
        lg.append(csm)      #CSmin
        lg.append(game.find_element(By.CLASS_NAME,'Kill').text)     #kills
        lg.append(game.find_element(By.CLASS_NAME,'Death').text)    #deaths
        lg.append(game.find_element(By.CLASS_NAME,'Assist').text)   #assists
        kda=game.find_element(By.CLASS_NAME,'KDARatio')
        lg.append(kda.text[0:len(kda.text)-2])      #KDA
        L.append(lg)
    else :
        pass
print(L)

time.sleep(1) #sinon ferme dès que ça charge quand y'a rien après
driver.quit()


