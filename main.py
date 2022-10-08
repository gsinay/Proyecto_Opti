from gurobipy import Model, GRB, quicksum

#Conjuntos
T = range(53) #Semanas del año 
Tr = ["HRW","SRW"] #Tipos de trigo, 1= HRW, 2=SRW
# S = ACA HAY QUE RELLENAR DEPENDIENDO DE LOS DATOS!!!

##Generacion del modelo:
model = Model()

#Variables
x = model.addVars(S,T,Tr, vtype = GRB.BINARY, name = "x_stTr") # cantidad de trigo tipo Tr a comprar del paıs s en la semana t.
y = model.addVars(S,T,Tr, vtype = GRB.BINARY, name="y_stTR") #cantidad de trigo a almacenar del paıs s en la semana t para la semana t+1
J = model.affVars(S,T,Tr, vtype = GRB.BINARY, name="j_stTr") #cantidad de trigo Tr almacenado del paıs s a utilizar en la semana t.

#Parámetros (algunos hay que leer de la instancia de datos y hacerlos una lista que correspondan a los indices de sus conjuntos, otros son numeros)

#Por acá hay que poner el time limit, no me acuerdo como era

#updatear
model.update()


#R2-R16: restricciones de enunciado

#Función Objetivo
