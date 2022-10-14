# Proyecto_Opti
## Introducción

El siguiente repositorio contiene el código del proyecto del grupo 49, cuyo tema de trabajo fue la importacion de trigo para pan de forma eficiente.

Para descargar todo el código, se recomienda clonar el repositorio, para esto utilizar

git clone https://github.com/gsinay/Proyecto_Opti

## Librerias a utilizar.
Para el trabajo se utilizaron las librerias Pandas y xlsxwriter. Si bien xlsxwriter no estaba estpiulada como una libreria permitida en el enunciado, esta se utilizó para armar el archivo de los datos final luego de pasar por la interfaz Gurobi De no tenerlas instaladas, en un terminal nuevo deben correr el siguiente código: 
```
pip3 install pandas
```

y,

```
pip3 install xlsxwriter
```

## Funcionamiento
Se debe ejecutar el archivo main.py, el cual creará un nuevo archivo excel llamado FINAL_RESULTS.xlsx. Este archivo excel es el que se utilizó como referencia para los resultados a analizar en el trabajo, y para armar los gráficos adjuntos en la entrega. 

Es imporante notar que los datos definidos en main.py se procesan en el archivo lectura_datos.py, el cual recibe los datos "sin filtrar" de el archivo SostrosTrigo.xls, especialmente de la hoja Ultra_Arreglado y Calidades. 

## Integrantes:
- Juan Pablo Aguero
- Nicolas Añazco
- Valentina Barra
- Isidora Olivera
- Trinidad Schwarzenberg
- Gabriel Sinay



