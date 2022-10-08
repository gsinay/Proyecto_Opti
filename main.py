from gurobipy import Model, GRB, quicksum

#Conjuntos
T = range(53) #Semanas del año 
Tr = ["HRW","SRW"] #Tipos de trigo, 1= HRW, 2=SRW
S = ["Chile", "Estados Unidos", "Argentina"]

##Generacion del modelo:
model = Model()

#Variables de decisión 
x = model.addVars(S,T,Tr, vtype = GRB.INTEGER, name = "x_stTr") # cantidad de trigo tipo Tr a comprar del paıs s en la semana t.
y = model.addVars(S,T,Tr, vtype = GRB.INTEGER, name="y_stTR") #cantidad de trigo a almacenar del paıs s en la semana t para la semana t+1
j = model.addVars(S,T,Tr, vtype = GRB.INTEGER, name="j_stTr") #cantidad de trigo Tr almacenado del paıs s a utilizar en la semana t.

#ARMANDO LOS Parámetros

Precios = {"USA" : {"HRW" : 365, "SRW" : 384}, "ARG" : {"HRW" : 348, "SRW" : 9999999999}}
c = {{s, trigo} : Precios[S][Tr] for s in S for trigo in Tr}    




#Por acá hay que poner el time limit, no me acuerdo como era

#updatear
model.update()


#Restricciones

#Función Objetivo
