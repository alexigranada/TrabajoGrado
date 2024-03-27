'''Importamos librerias'''
import pandas as pd #Leer datos
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt #Graficas y limpiar datos
import numpy as np

ruta_hora = 'datos_exportados.csv' #Ruta del archivo
data_hora = pd.read_csv(ruta_hora, delimiter=',') #Cargamos archivo
print(data_hora)
#data_hora = pd.read_csv(ruta_hora, delimiter=';') #Cargamos archivo
#print('Registros, columnas:')
#print(data_hora.shape)
#print('Tabulación de los datos:')
#print(data_hora.head()) 

'''Miramos las variables categoricas y numericas'''
#data_max.info()
'''
object seria una varible de tipo categoria
int64 entero 
float64 real
'''
'''Pandas busca las variables numericas y nos mostrará información estadistica'''
#print(data.describe())
'''Si la desviación estantar (std) es igual a cero, eso quiere decir que los valores numericos no son iguales
Eliminamos información irrelevante de los datos'''
#data_hora.drop(columns=['Entidad', 'AreaOperativa', 'Departamento', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion'], inplace=True)

''' Agrupar por la columna 'NombreEstación' '''
#nombre_estacion_hora = data_hora.groupby('NombreEstacion')

'''
for estacion, grupo in estaciones:
    print(f"Grupo para la categoría '{estacion}':")
    print(grupo)
    print("\n")
'''
''' Convertimos en DataFrame'''
#estacion_hora = pd.DataFrame(data_hora)
#grupo_estaciones_min = pd.DataFrame(nombre_estacion_min)
#print('Dataset')
#print(estacion_hora)

#''' Agrupamos por categoria'''
#estacion_hora = nombre_estacion_hora.get_group(str(grupo_estaciones_hora[0][0]))
print('Entra')

hora = data_hora['Fecha']
valor = data_hora['Valor']
print(hora)
print(valor)

plt.figure(dpi=50, figsize=(10,5))
plt.plot(hora, valor, color = 'coral') #, linewidth=10, linestyle='--'

plt.title('Ahora si')
#plt.legend(['Temp Máx','Temp Mín', 'Temp Promedio']) 
plt.xlabel('Hora')
plt.ylabel('Temperatura (°C)')
plt.show()
print('Final 0')