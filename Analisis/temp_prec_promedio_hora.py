# -*- coding: utf-8 -*-
"""
Created on Wed July 26 00:35:31 2024

Gráfica de promedio hora de temperatura y precipitación en una sola salida gráfica

@author: Arturo A. Granada G.
"""

import pandas as PD
import plotly.graph_objects as GO
from plotly.subplots import make_subplots

r = 'Datos/V_Climaticas_Pacifico_Medicion_ERA.csv'

df = PD.read_csv(r, sep=';')
df['Fecha'] = PD.to_datetime(df['Fecha'], format='%Y-%m-%d %H:%M:%S')

df['Hora'] = df['Fecha'].dt.hour

promedio = df.groupby('Hora').mean().reset_index()

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(GO.Bar(x=promedio['Hora'], y=promedio['tp'], name='ERA5-Land', marker_color='#3366CC', opacity=0.7, width=0.4, yaxis='y1')) #
fig.add_trace(GO.Bar(x=promedio['Hora'], y=promedio['Ptotal'], name='Observación', marker_color='#DC3912', opacity=0.7, width=0.4, yaxis='y1')) #

fig.add_trace(GO.Scatter(x=promedio['Hora'], y=promedio['t2m'], mode='lines+markers', name='ERA5-Land', marker_color='#3366CC', line=dict(width=1.5), yaxis='y2'))#Rojo EF553B
fig.add_trace(GO.Scatter(x=promedio['Hora'], y=promedio['Tmedia'], mode='lines+markers', name='Observación', marker_color='#DC3912', line=dict(width=1.5), yaxis='y2'))#Verde 00CC96

title = f'Precipitación y temperatura promedio por hora, estación "Unipacifico"'
fig.update_layout(title = title,
                  title_font_size=22,
                  xaxis = dict(title='Hora (2015 - 2023)'),
                  yaxis = dict(title='Precipitación (mm)'),
                  yaxis2 = dict(title='Temperatura (°C)', side='right'),
                  template = 'seaborn',
                  title_x = 0.5)
fig.write_image('Clima promedio Unipacifico.png', width=1000, height=500, scale=4)
fig.show()
#print(promedio)

'''Descripción'''
print(df)
print(df.describe())

'''Calculo de valores nulos'''
nulos_temperatura = df['Tmedia'].isnull().sum()
nulos_precipitacion = df['Ptotal'].isnull().sum()

print(f'Temperatura nulos: {nulos_temperatura}')
print(f'Precipitación nulos: {nulos_precipitacion}')
