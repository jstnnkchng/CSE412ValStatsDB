import pandas as pd
import psycopg2

print("Starting...")

#load data
ESPdf=pd.read_csv("C:\\Users\\justi\\Documents\\CSE412\\Project\\ESportPersonCSV.csv")
playerdf=pd.read_csv("C:\\Users\\justi\\Documents\\CSE412\\Project\\PlayerCSV.csv")
coachdf=pd.read_csv("C:\\Users\\justi\\Documents\\CSE412\\Project\\CoachCSV.csv")
teamdf=pd.read_csv("C:\\Users\\justi\\Documents\\CSE412\\Project\\TeamCSV.csv")
agentdf=pd.read_csv("C:\\Users\\justi\\Documents\\CSE412\\Project\\AgentCSV.csv")
'''
print(ESPdf.shape)
print(playerdf.shape)
print(coachdf.shape)
print(teamdf.shape)
print(agentdf.shape)
'''
conn=psycopg2.connect(
    host="localhost",
    port=5435,
    database="postgres",
    user="postgres",
    password="postgres"
    )
curs=conn.cursor()
print("Opened Database")

#insert ESportPerson Data
for i in range(len(ESPdf)):
    tempUID=ESPdf.loc[i,"uid"]
    tempName="'{}'".format(ESPdf.loc[i,"ESPname"])
    tempAge=ESPdf.loc[i,"age"]
    tempCountry="'{}'".format(ESPdf.loc[i,"country"])
    tempJob="'{}'".format(ESPdf.loc[i,"job"])
    curs.execute("INSERT INTO public.ESportPerson VALUES({},{},{},{},{}) ON CONFLICT (uid) DO NOTHING;".format(tempUID,tempName,tempAge,tempCountry,tempJob))
conn.commit()

#insert team Data
for i in range(len(teamdf)):
    tempTID=teamdf.loc[i,"tid"]
    tempCountry="'{}'".format(teamdf.loc[i,"country"])
    tempName="'{}'".format(teamdf.loc[i,"tname"])
    tempWinnings=teamdf.loc[i,"winnings"]
    curs.execute("INSERT INTO public.Team VALUES({},{},{},{}) ON CONFLICT (tid) DO NOTHING;".format(tempTID,tempCountry,tempName,tempWinnings))
conn.commit()

#insert player Data
for i in range(len(playerdf)):
    tempPID=playerdf.loc[i,"pid"]
    tempTID=playerdf.loc[i,"tid"]
    tempWinnings=playerdf.loc[i,"winnings"]
    curs.execute("INSERT INTO public.Player VALUES({},{},{}) ON CONFLICT (pid) DO NOTHING;".format(tempPID,tempTID,tempWinnings))
conn.commit()

#insert coach Data
for i in range(len(coachdf)):
    tempCID=coachdf.loc[i,"cid"]
    tempTID=coachdf.loc[i,"tid"]
    curs.execute("INSERT INTO public.Coach VALUES({},{}) ON CONFLICT (cid) DO NOTHING;".format(tempCID,tempTID))
conn.commit()

#insert agent data
for i in range(len(agentdf)):
    tempPID=agentdf.loc[i,"pid"]
    tempName="'{}'".format(agentdf.loc[i,"name"])
    tempKD=agentdf.loc[i,"kd"]
    tempAvgscore=agentdf.loc[i,"avgscore"]
    curs.execute("INSERT INTO public.Agent VALUES({},{},{:.2f},{:.2f}) ON CONFLICT (name,pid) DO NOTHING;".format(tempPID,tempName,tempKD,tempAvgscore))
conn.commit()
'''
total=0
curs.execute("SELECT COUNT(uid) FROM public.ESportPerson;")
helper=curs.fetchone()
countInTable=helper[0]
print("{} entries in table ESportPerson".format(countInTable))
total+=countInTable

curs.execute("SELECT COUNT(pid) FROM public.Player;")
helper=curs.fetchone()
countInTable=helper[0]
print("{} entries in table Player".format(countInTable))
total+=countInTable

curs.execute("SELECT COUNT(cid) FROM public.Coach;")
helper=curs.fetchone()
countInTable=helper[0]
print("{} entries in table Coach".format(countInTable))
total+=countInTable

curs.execute("SELECT COUNT(tid) FROM public.Team;")
helper=curs.fetchone()
countInTable=helper[0]
print("{} entries in table Team".format(countInTable))
total+=countInTable

curs.execute("SELECT COUNT(pid) FROM public.Agent;")
helper=curs.fetchone()
countInTable=helper[0]
print("{} entries in table Agent".format(countInTable))
total+=countInTable

print("Total of {} entries in 412ValStats.db".format(total))
'''
conn.close()
print("Closed Database")

print("Ending...")