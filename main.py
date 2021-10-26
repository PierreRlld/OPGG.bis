import pandas as pd
from datacollectorv2 import updategames, modif

pl=["PIERR0 LA RAFALE", "Nobusuke", "TITO LA TORPILLE", "chtis sournois", "CharLoRamBo"]    #usernames
var=['Champion','Result','CS','CSmin','Kills','Deaths','Assists','KDA','GameID']            #GameId=time/kda@champ
# Initializing dataframes =============
dP=pd.DataFrame(index=[0],columns=var)
dG=dP.copy()
dT=dP.copy()
dGr=dP.copy()
dC=dP.copy()

Set={"PIERR0 LA RAFALE":dP,"Nobusuke":dG,"TITO LA TORPILLE":dT,"chtis sournois":dGr,"CharLoRamBo":dC}

def SetUpdate(username):
    df=Set[username]    #selecting the dataframe corresponding to the username
    up=updategames(username)
    if up[0]==None:
        return df 
    else :
        for game in up :
            if (game[9] in df['GameId']) :
                up.remove(game)
            else :
                pass
        dftemp=pd.DataFrame(data=up,index=[len(up)],columns=var)
        dffin=df.append(dftemp,sort=False)
        dffin.set_index([i for i in range(1,len(dffin)+1)])
        
        return dffin


# test =======================
test=updategames('Nobusuke')
import pandas as pd
var=['Champion','Result','CS','CSmin','Kills','Deaths','Assists','KDA','GameID']        #GameId=time/kda@champ
testa=pd.DataFrame(data=test,index=[i for i in range(1,len(test)+1)],columns=var)
testb=pd.DataFrame(data=[['Kennen', 'Lose', '279', 6.2, '5', '13', '2', '0.54', '45:33/0.54@Kennen']],index=[1],columns=var)
testfin=testa.append(testb,sort=False)
print(testfin)