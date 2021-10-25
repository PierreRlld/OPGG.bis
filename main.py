import pandas as pd

pl=["PIERR0 LA RAFALE", "Nobusuke", "TITO LA TORPILLE", "chtis sournois", "CharLoRamBo"]

def modif(charac):
    return charac.replace(" ","+")

plsearch=list(map(modif,pl))
print(plsearch)