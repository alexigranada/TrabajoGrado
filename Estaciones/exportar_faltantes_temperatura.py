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

ruta = 'C:/Datos/Estaciones Dagua/Temperatura_AEROPUERTO BUENAVENTUR [53115010].csv' #Ruta del archivo
df = pd.read_csv(ruta, delimiter=';') #Cargamos archivo

print(df.head())

''' Creamos el formato de la fecha'''
fechaformato = "%Y-%m-%d"
df['Fecha'] = pd.to_datetime(df['Fecha'], format=fechaformato)

''' Ploteamos datos con Plotly'''
#'''
temp_max = df['ValorMax']
temp_min = df['ValorMin']
temp_media = df['ValorMedio']
time = df['Fecha']

name = str(df['NombreEstacion'][0])
title = f'Patron de la Temperatura estación: {name}'

fig = go.Figure()
fig.add_trace(go.Scatter(x=time, y=temp_max, mode='lines', name='Temp. Máx', line=dict(color='#EF553B')))
fig.add_trace(go.Scatter(x=time, y=temp_media, mode='lines', name='Temp. Media', line=dict(color='#00CC96')))
fig.add_trace(go.Scatter(x=time, y=temp_min, mode='lines', name='Temp. Mín', line=dict(color='#636EFA')))

fig.update_layout(title = title,
                  xaxis = dict(title='Años'),
                  yaxis = dict(title='Temperatura (°C)'),
                  title_x = 0.5)
fig.show()

''' Imprimir datos nulos'''
df_nulos = df[df['ValorMax'].isnull() & df['ValorMin'].isnull()]

print(df_nulos)