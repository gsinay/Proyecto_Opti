from gurobipy import Model, GRB, quicksum
import lectura_datos as datos


#Conjuntos
T = range(53) #Semanas del año 
Tr = ["HRW","SRW"] #Tipos de trigo, 1= HRW, 2=SRW
S = ["Chile", "USA", "Argentina", "Canada"]

##Generacion del modelo:
model = Model()
model.setParam("TimeLimit", 1800) #30 Minutos TimeLimit

#Variables de decisión 
x = model.addVars(S,T,Tr, vtype = GRB.INTEGER, name = "x_stTr") # cantidad de trigo tipo Tr a comprar del paıs s en la semana t.
y = model.addVars(S,T,Tr, vtype = GRB.INTEGER, name="y_stTR") #cantidad de trigo a almacenar del paıs s en la semana t para la semana t+1
j = model.addVars(S,T,Tr, vtype = GRB.INTEGER, name="j_stTr") #cantidad de trigo Tr almacenado del paıs s a utilizar en la semana t.

#Parámetros fijos
a = 4.5/6/4 #precio de almacenaje por semana
vmax = 2182547 #almacenaje maximo en metros cubicos
v = 1/800 #m^3 ocupados por kilogaramo de trigo
r = 24 #24 semanas = 6 meses, vida util del trigo


#Por acá hay que poner el time limit, no me acuerdo como era

#updatear
model.update()


#Restricciones

#Función Objetivo
 #objetivo = quicksum((x[s,t,tr] * (c[s,tr] + w )) + y[s,t]*a[t] for t in T for s in S for tr in Tr) 
 # A esto le falta el parametro a[t] y el parametro w, pero es la misma estructura
