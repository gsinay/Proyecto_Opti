import pandas as pd
import random

random.seed(777) #para que los valores aleatorios sean siempre los mismos

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
ChileSRW = list(s["Chile SRW"])

c = dict() #precio de trigo de cada pais y tipo por semana
for i in semana:
    for trigo in Tr:
        for pais in S:
            if pais == "Chile":
                if trigo == "HRW":
                    c[(int(i), pais, trigo)] = ChileHRW[i-1]
                else:
                     c[(int(i), pais, trigo)] = ChileSRW[i-1]
            elif pais == "USA":
                if trigo == "HRW":
                    c[(int(i), pais, trigo)] = USAHRW[i-1]
                else:
                    c[(int(i), pais, trigo)] = USASRW[i-1]
            elif pais == "Argentina":
                if trigo == "HRW":
                    c[(int(i), pais, trigo)] = ArgHRW[i-1]
                else:
                     c[(int(i), pais, trigo)] = ArgSRW[i-1]
                if trigo == "HRW":
                    c[(int(i), pais, trigo)] = CanadaHRW[i-1]
                else:
                     c[(int(i), pais, trigo)] = CanadaSRW[i-1]
            
d = dict() # Demanda de toneladas de trigo por semana 
for i in semana:
    d[tuple(int(i))] = random.randrange(41000, 51000) #ocupamos estos valores por una tolerancia de 10% en el promedio de demanda anual por semana.
print(d)




