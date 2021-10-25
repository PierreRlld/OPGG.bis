
pl=["PIERR0 LA RAFALE", "Nobusuke", "TITO LA TORPILLE", "chtis sournois", "CharLoRamBo"]    #usernames

def modif(charac):
    return charac.replace(" ","%20")
plsearch=list(map(modif,pl))    #list of players for opgg

import pandas as pd

var=['Champion','Result','CS','CSmin','Kills','Deaths','Assists','KDA']
dP=pd.DataFrame(index=[0],columns=var)
dG=dP.copy()
dT=dP.copy()
dC=dP.copy()
dGr=dP.copy()

print(dP)
