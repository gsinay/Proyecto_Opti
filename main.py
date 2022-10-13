from gurobipy import Model, GRB, quicksum
import lectura_datos as datos


#Conjuntos
T = range(1,53) #Semanas del año 2021
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
v = 1000/800 #m^3 ocupados por tonelada de trigo
r = 24 #24 semanas = 6 meses, vida util del trigo

#updatear
model.update()


#Restricciones
#Restricción 1 -- cumplimiento de demanda
model.addConstrs((quicksum(j[s,t,tr] + x[s,t,tr] for s in S) == datos.d[t,tr] + quicksum(y[s,t,tr] for s in S) for t in T for tr in Tr), name="R1")

#restriccion 2 -- volumen max de almacenaje
model.addConstrs((quicksum(y[s,t,tr] * v for s in S) <= vmax for t in T for tr in Tr), name="R2")

#restriccion 3 -- cantidad maxima de importacion
model.addConstrs((quicksum(quicksum( (x[s,t-1,tr] * v) +  (y[s,t-1,tr] * v) +  (j[s,t,tr] * v) for tr in Tr) for s in S) - quicksum(datos.d[t,tr] for tr in Tr) <= vmax for t in range(2,53)), name ="R3") #revisar lo de los indices de t

#restriccion 4 -- calidad

#restriccion 5 -- disponibilidad de uso de almacenaje
model.addConstrs((quicksum(j[s,t,tr] for s in S) <= quicksum(y[s,t-1,tr] for s in S) for t in range(2,52) for tr in Tr), name ="R5")  #el range(2,51) es desde la semana 2 hasta la semana t-1 (51)


#Función Objetivo
objetivo = quicksum(quicksum(quicksum((x[s,t,tr]*datos.c[t,s,tr]) + (y[s,t,tr]*a) for tr in Tr)for t in T) for s in S)
model.setObjective(objetivo, GRB.MINIMIZE)
model.optimize()