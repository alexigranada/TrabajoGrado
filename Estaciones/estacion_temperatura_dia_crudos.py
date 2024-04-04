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
#import matplotlib.pyplot as plt #Graficas y limpiar datos

ruta_max = 'Datos/Estaciones/IDEAM/Descarga 0/Tempmax1990-2000.csv' #Ruta del archivo
ruta_min = 'Datos/Estaciones/IDEAM/Descarga 0/Tempmin1990-2000.csv' #Ruta del archivo
data_max = pd.read_csv(ruta_max, delimiter=',') #Cargamos archivo
data_min = pd.read_csv(ruta_min, delimiter=',') #Cargamos archivo
#print('Registros, columnas:')
#print(data.shape)
#print('Tabulación de los datos:')
print(data_max.head()) 
print(data_min.head())
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
data_max.drop(columns=['Entidad', 'AreaOperativa', 'Departamento', 'Municipio', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion'], inplace=True)
data_min.drop(columns=['Entidad', 'AreaOperativa', 'Departamento', 'Municipio', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion'], inplace=True)

''' Agrupar por la columna 'NombreEstación' '''
nombre_estacion_max = data_max.groupby('NombreEstacion')
nombre_estacion_min = data_min.groupby('NombreEstacion')

''' Convertimos en DataFrame'''
grupo_estaciones_max = pd.DataFrame(nombre_estacion_max)
grupo_estaciones_min = pd.DataFrame(nombre_estacion_min)
name = str(grupo_estaciones_max[0][3])

''' Agrupamos por categoria'''
estacion_max = nombre_estacion_max.get_group(str(grupo_estaciones_max[0][3]))
estacion_min = nombre_estacion_min.get_group(str(grupo_estaciones_min[0][3]))

''' Creamos el formato de la fecha'''
estacion_max['Fecha'] = pd.to_datetime(estacion_max['Fecha'], format='%Y-%m-%d %H:%M')
estacion_min['Fecha'] = pd.to_datetime(estacion_min['Fecha'], format='%Y-%m-%d %H:%M')

''' Crear un rango de fechas completo '''
rango_fechas_completo_max = pd.date_range(start='1989-12-01', end='1999-12-31')
rango_fechas_completo_min = pd.date_range(start='1989-12-01', end='1999-12-31')

''' Crear un DataFrame con las fechas completas '''
df_completo_estacion_max = pd.DataFrame({'Fecha': rango_fechas_completo_max})
df_final_estacion_max = pd.merge(df_completo_estacion_max, estacion_max, on='Fecha', how='left')
print('Estación máx:')
print(df_final_estacion_max)
df_completo_estacion_min = pd.DataFrame({'Fecha': rango_fechas_completo_min})
df_final_estacion_min = pd.merge(df_completo_estacion_min, estacion_min, on='Fecha', how='left')
print('Estación Min: ')
print(df_final_estacion_min)

''' Imprimir datos nulos max'''
#df_nulos_estacion_max = df_final_estacion_max[df_final_estacion_max['Valor'].isnull()]
#print('Registros Nulos Máx')
#print(df_nulos_estacion_max)
''' Exportar el DataFrame nulos max a un archivo CSV '''
#title_max = f'Temperatura_max_{name}.csv'
#df_nulos_estacion_max.to_csv(title_max, sep=';', index=False)

''' Imprimir datos nulos min'''
#df_nulos_estacion_min = df_final_estacion_min[df_final_estacion_min['Valor'].isnull()]
#print('Registros Nulos Min')
#print(df_nulos_estacion_min)
''' Exportar el DataFrame nulos min a un archivo CSV '''
#title_min = f'Temperatura_min_{name}.csv'
#df_nulos_estacion_min.to_csv(title_min, sep=';', index=False)

'''' Calculamos los valores nulos'''
#valores_nulos_max = df_final_estacion_max['Valor'].isnull().sum()
#print('Datos faltantes max: ')
#print(valores_nulos_max)

#valores_nulos_min = df_final_estacion_min['Valor'].isnull().sum()
#print('Datos faltantes min: ')
#print(valores_nulos_min)

''' Fusionar los DataFrames en base a la columna 'Fecha'''
unir_df = pd.merge(df_final_estacion_min, df_final_estacion_max, on='Fecha')
print('Unión')
print(unir_df)
''' Sumar las variables correspondientes '''
#unir_df['ValorMedio'] = (unir_df['Valor_x'] + unir_df['Valor_y'])/2
#print(unir_df)

''' Ploteamos las graficas'''
#'''
temp_max = unir_df['Valor_x']
temp_min = unir_df['Valor_y']
time_max = unir_df['Fecha']
#time_min = df_final_estacion_min['Fecha']
#temp_media = data_max['ValorMedio']
#time_media = data_max['Fecha']

title = f'Patron de la Temperatura estación: {name}'

fig = go.Figure()
fig.add_trace(go.Scatter(x=time_max, y=temp_max, mode='lines', name='Temp. Máx', line=dict(color='#EF553B')))
#fig.add_trace(go.Scatter(x=time_media, y=temp_media, mode='lines', name='Temp. Media', line=dict(color='#00CC96')))
fig.add_trace(go.Scatter(x=time_max, y=temp_min, mode='lines', name='Temp. Mín', line=dict(color='#636EFA')))

fig.update_layout(title = title,
                  xaxis = dict(title='Años'),
                  yaxis = dict(title='Temperatura (°C)'),
                  title_x = 0.5,
                  template='plotly_white')
fig.show()

''' Exportar el DataFrame nulos max a un archivo CSV '''
title = f'Temperatura_1990-2000_{name}.csv'
unir_df.to_csv(title, sep=';', index=False)

#'''
'''
fig = px.line(df_final_estacion_max, x='Fecha', y='Valor', title=title)
fig.add_line(df_final_estacion_min, x='Fecha', y='Valor')
fig.show()


plt.figure(dpi=150, figsize=(15,5))
plt.plot(time_max, temp_max, color = 'coral', linewidth=2, linestyle='--')
plt.plot(time_media, temp_media, color = 'yellowgreen', linewidth=0.9)
plt.plot(time_min, temp_min, color = 'skyblue', linewidth=0.9, marker='.')

#plt.xticks(E1['Fecha'][:4], rotation=45)
name = str(grupo_estaciones_max[0][0])
title = f'Patron de la Temperatura estación: {name}'
plt.title(title)
plt.legend(['Temp Máx','Temp Mín', 'Temp Promedio']) 
plt.xlabel('Año')
plt.ylabel('Temperatura (°C)')
'''