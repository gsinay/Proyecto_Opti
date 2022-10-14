import pandas as pd
import random

random.seed(777) #para que los valores aleatorios sean siempre los mismos

Tr = ["HRW","SRW"] #Tipos de trigo, 1= HRW, 2=SRW
S = ["Chile", "USA", "Argentina", "Canada"]

filename = "CostosTrigo.xls"
costos = pd.read_excel(filename, "Ultra_Arreglado")

semana = list(costos["Semana"])
ArgHRW = list(costos["Argentina HRW"])
ArgSRW = list(costos["Argentina SRW"])
USAHRW = list(costos["USA HRW"])
USASRW = list(costos["USA SRW"])
CanadaHRW = list(costos["Canada HRW"])
CanadaSRW = list(costos["Canada SRW"])
ChileHRW = list(costos["Chile HRW"])
ChileSRW = list(costos["Chile SRW"])

c = dict() #precio de trigo de cada pais y tipo por semana... tiena la forma c = {(1, chile, hrw) : numero, etc.}
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
            else:
                if trigo == "HRW":
                    c[(int(i), pais, trigo)] = CanadaHRW[i-1]
                else:
                     c[(int(i), pais, trigo)] = CanadaSRW[i-1]
            
d = dict() # Demanda de toneladas de trigo por semana. tiena la forma d = {(1, hrw) : numero, (1,srw) : numero, etc.}
for i in semana:
    demanda = random.randrange(41000, 51000)
    for trigo in Tr:
        proporcion = random.randrange(8, 10) #valor aleatorio de proporcion de demanda de hrw  mayor a 80%
        if trigo == "HRW":
            d[(int(i), trigo)] = random.randrange(41000, 51000)*(proporcion/10) #ocupamos estos valores por una tolerancia de 10% en el promedio de demanda anual por semana.
        else:
             d[(int(i), trigo)] = random.randrange(41000, 51000)*(1-(proporcion/10))
calidades = pd.read_excel(filename, "Calidades")
calidades_lista = list(calidades["Calidades"])
print(calidades_lista)
q = dict()
for i in range(len(calidades_lista)):
    if i == 0:
        q[("Chile")] = calidades_lista[i]
    elif i == 1:
        q[("USA")] = calidades_lista[i]
    if i == 2:
        q[("Argentina")] = calidades_lista[i]
    else:
        q[("Canada")] = calidades_lista[i]








