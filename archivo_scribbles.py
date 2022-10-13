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
x = model.addVars(S,T,Tr, vtype = GRB.CONTINUOUS, name = "x_stTr") # cantidad de trigo tipo Tr a comprar del paıs s en la semana t.
y = model.addVars(S,T,Tr, vtype = GRB.CONTINUOUS, name="y_stTR") #cantidad de trigo a almacenar del paıs s en la semana t para la semana t+1
j = model.addVars(S,T,Tr, vtype = GRB.CONTINUOUS, name="j_stTr") #cantidad de trigo Tr almacenado del paıs s a utilizar en la semana t.

#Parámetros fijos
a = 4.5/6/4 #precio de almacenaje por semana
V = 2182547 #almacenaje maximo en metros cubicos
v = 1000/800 #m^3 ocupados por tonelada de trigo
r = 30 #30 semanas = 6 meses, vida util del trigo
vmax = 500000 #cantidad maxima a importar
vmin = 10000 #cantidad minima a tener almacenada
calidad_min = 0.8

#updatear
model.update()


#Restricciones
#naturalezad de las variables
model.addConstrs((x[s,t,tr] >= 0 for s in S for t in T for tr in Tr), name="NatX")
model.addConstrs((y[s,t,tr] >= 0 for s in S for t in T for tr in Tr), name="NatY")
model.addConstrs((j[s,t,tr] >= 0 for s in S for t in T for tr in Tr), name="NatJ")


#restriccion 1 -- demanda:
model.addConstrs((quicksum(x[s,t,tr] - y[s,t,tr] + j[s,t,tr] for s in S) == datos.d[t,tr] for t in T for tr in Tr), name="R1")
#restriccion 2 -- volumen max de almacenaje
model.addConstrs((quicksum(y[s,t,tr] * v for s in S) <= V for t in T for tr in Tr), name="R2")
#restriccion 3 -- cantidad maxima de importacion
model.addConstrs((quicksum((x[s,t-1,tr] * v) +  (y[s,t-1,tr] * v) +  (j[s,t,tr] * v) for tr in Tr for s in S) - quicksum(datos.d[t,tr] for tr in Tr) <= vmax for t in range(2,53)), name ="R3") #revisar lo de los indices de t
#restriccion 4: calidad!!!!!1
model.addConstrs((quicksum((x[s,t-1,tr] + y[s,t-1,tr] - j[s,t,tr]) * datos.q[s] for s in S for tr in Tr ) >= calidad_min * quicksum(x[s,t-1,tr] + y[s,t-1,tr] - j[s,t,tr] for s in S for tr in Tr) for t in range(2,52)), name="R5")
#restriccion 5 -- disponibilidad de uso de almacenaje
model.addConstrs((j[s,t,tr] <= quicksum(y[s,t-1,tr] - j[s,t-1,tr] for t in range(2,t)) for s in S for tr in Tr for t in T), name ="R5")  #el range(2,51) es desde la semana 2 hasta la semana t-1 (51)
# restriccion 6: vencimiento
model.addConstrs((quicksum(datos.d[t,tr] for t in T) >= quicksum(x[s,t-1,tr] for t in range(2, 52-r+1) for s in S) for tr in Tr),name="vencimiento1")
model.addConstrs((quicksum(y[s,t-1,tr] for s in S) == 0  for t in range(min(52, r+1), max(52,r))  for tr in Tr ), name="vencimiento2")
# restriccion 7: razon hrw a trigo total
model.addConstrs((quicksum(x[s,t,"HRW"] for s in ["USA", "Argentina", "Canada"]) >= 0.8 * quicksum(x[s,t,tr] for s in S for tr in Tr) for t in T), name="R7")
#restriccion 8: minimo a almacenar
model.addConstrs((quicksum(y[s,t,tr] - j[s,t,tr] for s in S for tr in Tr for t in range(1,x)) >= vmin for x in range(2,53)), name="R8")
#Restriccion 9: lo neto que sale de la bodega tiene que ser igual a lo que neto entra
model.addConstr((quicksum(j[s,t,tr] for s in S for t in T for tr in Tr) == quicksum(y[s,t,tr] for s in S for t in T for tr in Tr)))







#Función Objetivo
objetivo = quicksum(quicksum(quicksum((x[s,t,tr]*datos.c[t,s,tr]) + (y[s,t,tr]*a) for tr in Tr)for t in T) for s in S)
model.setObjective(objetivo, GRB.MINIMIZE)
model.optimize()

totalj = 0
totalc = 0
totaly = 0
for v in x.values():
    print("{}: {}".format(v.varName, v.X))
    totalc += v.X
for v in y.values():
    print("{}: {}".format(v.varName, v.X))
    totaly += v.X
for v in j.values():
    print("{}: {}".format(v.varName, v.X))
    totalj += v.X
print(totalj)
print(totalc)
print(totaly)



