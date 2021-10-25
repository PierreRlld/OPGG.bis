
#usernames
pl=["PIERR0 LA RAFALE", "Nobusuke", "TITO LA TORPILLE", "chtis sournois", "CharLoRamBo"]

def modif(charac):
    return charac.replace(" ","%20")

#list of players for opgg
plsearch=list(map(modif,pl))

import pandas as pd
