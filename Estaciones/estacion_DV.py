# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:33:48 2024
Exploración dato Dirección del Viento de las estaciones del IDEAM
@author: Arturo A. Granada g.
"""

'''Importamos librerias'''
import pandas as pd #Leer datos
import plotly.express as px #Para graficas simples
import plotly.graph_objects as go #Para graficas complejas

'''Cargamos datos'''
ruta = 'Datos/IDEAM/Estaciones Dagua IDEAM/VA_hora/Dir_viento_SILOE - AUT [26085160].csv'
dato = pd.read_csv(ruta, delimiter=';')

''' Tabulamos los primeros 5 datos'''
#print(dato.info())

''' Eliminamos columnas innecesarias'''
dato.drop(columns=['Municipio'], inplace=True)

''' Creamos el formato de la fecha'''
dato['Fecha'] = pd.to_datetime(dato['Fecha'], format='%Y-%m-%d %H:%M')

''' Crear un rango de fechas completo '''
rango_hora = pd.date_range(start=dato['Fecha'].min(), end=dato['Fecha'].max(), freq='h')

''' Crear un DF con el rango de fecha completo '''
df_rango_hora = pd.DataFrame({'Fecha': rango_hora})

''' Unimos DF por la columna 'Fecha' '''
df = pd.merge(df_rango_hora, dato, on='Fecha', how='left')# Usar la clave del marco Izquierdo (El completo)
print(df)
''' Calculamos los valores nulos'''
values_null = df['Valor'].isnull().sum()
print(f'Valores nulos: {values_null}')

''' Llenamos valores faltantes (Constantes)'''
name = str(df['NombreEstacion'][0])
codigo = df['CodigoEstacion'][0]
lat = df['Latitud'][0]
lon = df['Longitud'][0]
altura = df['Altitud'][0]

df['NombreEstacion'] = df['NombreEstacion'].fillna(name)
df['CodigoEstacion'] = df['CodigoEstacion'].fillna(codigo)
df['Latitud'] = df['Latitud'].fillna(lat)
df['Longitud'] = df['Longitud'].fillna(lon)
df['Altitud'] = df['Altitud'].fillna(altura)

''' Renombramos la columna Valor'''
df = df.rename(columns={'Valor': 'DV'})

''' Ploteamos los datos'''
valor = df['DV']
time  = df['Fecha']

fig = go.Figure()
fig.add_trace(go.Scatter(x=time, y=valor, mode='lines', name='Dir. Viento'))

fig.update_layout(title=f'Dirección del viento: {name}',
                  title_x= 0.5)
fig.show()

''' Exportar el DataFrame a un archivo CSV '''
title = f'DV_hora_{name}.csv'
df.to_csv(title, sep=';', index=False)

print('Fin')
print(df)