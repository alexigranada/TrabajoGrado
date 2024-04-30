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

ruta = 'Datos/Hora/1. La Cumbre/Precipitacion_LaCumbre_Hora.csv' #Ruta del archivo
df = pd.read_csv(ruta, delimiter=';') #Cargamos archivo

print(df)

''' Creamos el formato de la fecha'''
df['Fecha (UTC-05:00)'] = pd.to_datetime(df['Fecha (UTC-05:00)'], format='%Y-%m-%d %H:%M:%S')

''' Ploteamos datos con Plotly'''

variable = df['Valor (Millimetres)']
#temp_min = df['ValorMin']
#temp_media = df['ValorMedio']
time = df['Fecha (UTC-05:00)']

#name = str(df['NombreEstacion'][0])
title = f'Patron de la Precipiación estación: La Cumbre'

fig = go.Figure()
fig.add_trace(go.Bar(x=time, y=variable, name='Prec. Hora', marker_color='#03A9F4'))
#fig.add_trace(go.Scatter(x=time, y=temp, mode='lines', name='Temp. Máx', line=dict(color='#636EFA')))#EF553B
#fig.add_trace(go.Scatter(x=time, y=temp_media, mode='lines', name='Temp. Media', line=dict(color='#00CC96')))
#fig.add_trace(go.Scatter(x=time, y=temp_min, mode='lines', name='Temp. Mín', line=dict(color='#636EFA')))

fig.update_layout(title = title,
                  xaxis = dict(title='Años'),
                  yaxis = dict(title='Precipitación(mm/h)'),
                  title_x = 0.5)
fig.show()

''' Imprimir datos nulos'''
#df_nulos = df[df['ValorMax'].isnull() & df['ValorMin'].isnull()]
df_nulos = df[df['Valor (Millimetres)'].isnull()]
print(df_nulos)
#title_csv = f'Precipitacion_faltantes_LaCumbre.csv'
#df_nulos.to_csv(title_csv, sep=';', index=False)