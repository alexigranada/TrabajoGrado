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

ruta  = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_AEROPUERTO BUENAVENTUR [53115010].csv'
ruta1 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_BAJO CALIMA [54075020].csv'
ruta2 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_COLPUERTOS [53115020].csv'
ruta3 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_MISION LA [54075040].csv'

dato = pd.read_csv(ruta, delimiter=';')

''' Antes de concatenar ajustamos el formato de la fecha'''
dato['Fecha'] = pd.to_datetime(dato['Fecha'], format='%Y-%m-%d')

'''Ploteamos gráficas'''
max = dato['ValorMax']
med = dato['ValorMedio']
min = dato['ValorMin']
time = dato['Fecha']
name = str(dato['NombreEstacion'].iloc[0])#Columna 'NombreEstación' .iloc[posición'0']

fig = go.Figure()

fig.add_trace(go.Scatter(x=time, y=max, mode='lines', name='Temperatura Máx.', line=dict(color='#EF553B')))
fig.add_trace(go.Scatter(x=time, y=med, mode='lines', name='Temperatura Media.', line=dict(color='#00CC96')))
fig.add_trace(go.Scatter(x=time, y=min, mode='lines', name='Temperatura Mín.', line=dict(color='#636EFA')))
#fig.add_trace(go.Scatter(x=time, y=la_mis, mode='lines', name='La Misión Altura: 14 m.', line=dict(color='#A569BD')))

fig.update_layout(title = f'Temperatura dia {name} (1990 - 2023) ',
                  xaxis = dict(title='Años'),
                  yaxis = dict(title='Temperatura (°C)'),
                  title_x = 0.5,
                  template='plotly_white') #'plotly_white' - 'plotly_dark' - 'ggplot2' - 'seaborn - 'simple_white'
fig.show()
print('Finalizado sin errores')