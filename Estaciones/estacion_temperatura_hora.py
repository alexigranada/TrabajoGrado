# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:33:48 2024
Exploración de temperatura de las estaciones del IDEAM
@author: Arturo A. Granada g.
"""

'''Importamos librerias'''
import pandas as pd #Leer datos
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt #Graficas y limpiar datos
import numpy as np

ruta_hora = 'Datos/Estaciones/Temperatura_hora.csv' #Ruta del archivo

data_hora = pd.read_csv(ruta_hora, delimiter=',') #Cargamos archivo
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
data_hora.drop(columns=['Entidad', 'AreaOperativa', 'Departamento', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion'], inplace=True)

''' Agrupar por la columna 'NombreEstación' '''
nombre_estacion_hora = data_hora.groupby('NombreEstacion')

'''
for estacion, grupo in estaciones:
    print(f"Grupo para la categoría '{estacion}':")
    print(grupo)
    print("\n")
'''
''' Convertimos en DataFrame'''
grupo_estaciones_hora = pd.DataFrame(nombre_estacion_hora)
#grupo_estaciones_min = pd.DataFrame(nombre_estacion_min)


''' Agrupamos por categoria'''
estacion_hora = nombre_estacion_hora.get_group(str(grupo_estaciones_hora[0][1]))
print('Entra')
name = str(grupo_estaciones_hora[0][1])
#estacion_hora.to_csv(f'datos_{name}.csv', index=False)
print(estacion_hora)
''' Creamos el formato de la fecha'''
#fechaformato_hora = "%Y-%m-%d %H:%M"
#estacion_hora['Fecha'] = pd.to_datetime(estacion_hora['Fecha'], format=fechaformato_hora)

''' Crear un rango de fechas completo '''
#rango_fechas_completo_hora = pd.date_range(start='2000-09-01 07:00', end='2020-09-11 13:00', freq='H')

''' Crear un DataFrame con las fechas completas '''
#df_completo_estacion_hora = pd.DataFrame({'Fecha': rango_fechas_completo_hora})
#df_final_estacion_hora = pd.merge(df_completo_estacion_hora, estacion_hora, on='Fecha', how='left')
#print('Estación hora:')
#print(df_final_estacion_hora)

'''' Calculamos los valores nulos'''
valores_nulos_hora = estacion_hora['Valor'].isnull().sum()
print('Datos faltantes hora: ')
print(valores_nulos_hora)

''' Fusionar los DataFrames en base a la columna 'Fecha'''
#unir_df = pd.merge(df_final_estacion_max, df_final_estacion_min, on='Fecha')
#print('Unión')
#print(unir_df)
''' Sumar las variables correspondientes '''
#unir_df['ValorMedio'] = (unir_df['Valor_x'] + unir_df['Valor_y'])/2
#print(unir_df)

''' Ploteamos las graficas'''
temp_hora = estacion_hora['Valor']
time_hora = estacion_hora['Fecha']

title = f'Patron de la Temperatura estación: {name}'

fig = go.Figure()
fig.add_trace(go.Scatter(x=time_hora, y=temp_hora, mode='lines', name='Temp. Hora', line=dict(color='#EF553B')))


fig.update_layout(xaxis = dict(title='Horas'),
                  yaxis = dict(title='Temperatura (°C)'),
                  title = title,
                  title_x = 0.5)
fig.show()

'''
fig = px.line(df_final_estacion_max, x='Fecha', y='Valor', title=title)
fig.add_line(df_final_estacion_min, x='Fecha', y='Valor')
fig.show()
'''

#plt.figure(dpi=150, figsize=(15,5))
#plt.plot(time_hora, temp_hora, color = 'coral', linewidth=10) #, linestyle='--'
#plt.plot(time_media, temp_media, color = 'yellowgreen', linewidth=0.9)
#plt.plot(time_min, temp_min, color = 'skyblue', linewidth=0.9, marker='.')

#plt.xticks(E1['Fecha'][:4], rotation=45)
#name = str(grupo_estaciones_hora[0][0])
#title = f'Patron de la Temperatura estación: {name}'
#plt.title(title)
#plt.legend(['Temp Máx','Temp Mín', 'Temp Promedio']) 
#plt.xlabel('Hora')
#plt.ylabel('Temperatura (°C)')
#plt.show()
#print('Final')