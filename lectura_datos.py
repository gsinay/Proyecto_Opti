import pandas as pd
Tr = ["HRW","SRW"] #Tipos de trigo, 1= HRW, 2=SRW
S = ["Chile", "USA", "Argentina", "Canada"]

filename = "CostosTrigo.xls"
s = pd.read_excel(filename, "Ultra_Arreglado")
print(s)
semana = list(s["Semana"])
ArgHRW = list(s["Argentina HRW"])
ArgSRW = list(s["Argentina SRW"])
USAHRW = list(s["USA HRW"])
USASRW = list(s["USA SRW"])
CanadaHRW = list(s["Canada HRW"])
CanadaSRW = list(s["Canada SRW"])
ChileHRW = list(s["Chile HRW"])
ChileHRW = list(s["Chile SRW"])

c = dict()
for i in semana:
    c[int(i)] =  dict ()
    for trigo in Tr:
        for pais in S:
            tipopais = pais + " " + trigo
            c[int(i)][tipopais] = 

print(c)






