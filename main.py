import pandas as pd
from datacollectorv2 import updategames, modif

pl=["PIERR0 LA RAFALE", "Nobusuke", "TITO LA TORPILLE", "chtis sournois", "CharLoRamBo"]    #usernames
var=['Champion','Result','CS','CSmin','Kills','Deaths','Assists','KDA','GameID']        #GameId=time/kda@champ
# Initializing dataframes =============
dP=pd.DataFrame(index=[0],columns=var)
dG=dP.copy()
dT=dP.copy()
dGr=dP.copy()
dC=dP.copy()

Set={"PIERR0 LA RAFALE":dP,"Nobusuke":dG,"TITO LA TORPILLE":dT,"chtis sournois":dGr,"CharLoRamBo":dC}


"""
def SetUpdate(username):
    df=Set[username]    #selecting the dataframe corresponding to the username
    up=updategames(username)
    if up[0]==None:
        return df 
    else :
        df.append(updategames(username),sort=False)
        df.set_index(i for i in range(1,len(df)+1))
        #delete games aldready in the dataset
        indexnames=df[].index
"""

test=updategames('Nobusuke')
testb=pd.DataFrame(Data=['Kennen', 'Lose', '279', 6.2, '5', '13', '2', '0.54', '45:33/0.54@Kennen'],index=[1],columns=var)