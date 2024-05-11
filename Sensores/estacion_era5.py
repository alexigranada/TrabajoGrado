# -*- coding: utf-8 -*-
"""
Created on Sun May 05 14:45:03 2024

Exploración de datos de sensor ERA5 vs Observados por las estaciones

@author: Arturo A. Granada G.
"""

'''Importamos librerias'''
import pandas as pd #Leer datos
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt #Graficas y limpiar datos

e5 = 'Datos/ERA5/ERA5_LaCumbre_Hora.csv' #Ruta del archivo CHIRPS
es = 'Datos/Hora/V_Climaticas_LaCumbre_RL_Hora.csv' #Ruta del archivo Estatción

era5 = pd.read_csv(e5, delimiter=';') #Cargamos archivo
es = pd.read_csv(es, delimiter=';')
print(era5)
#print(dch)
''' Creamos el formato de la fecha'''
era5['datetime'] = pd.to_datetime(era5['datetime'], format='%Y-%m-%d %H:%M:%S')
es['Fecha (UTC-05:00)'] = pd.to_datetime(es['Fecha (UTC-05:00)'], format='%d/%m/%Y %H:%M')

'''Sumamos la precipitación por día en la estación'''
#es.set_index('Fecha (UTC-05:00)', inplace=True)
#es = es.resample('D').mean()
#es.reset_index(inplace=True)

fig = go.Figure()

temp = era5['temperature_2m']
tes = es['Temp Media']
time = es['Fecha (UTC-05:00)']

#fig = px.bar(dch, x='Fecha', y='prcp', color_discrete_sequence=['darkblue']) #['blue'] - px.colors.qualitative.Dark24
fig.add_trace(go.Scatter(x=time, y=temp, mode='lines', name='Temperatura ERA5', line=dict(color='#2ECC71'))) #2ECC71
fig.add_trace(go.Scatter(x=time, y=tes, mode='lines', name='Temperatura Estación', line=dict(color='#F44336')))
title = f'Temperatura ERA5 vs Estación La Cumbre'
fig.update_layout(title = title,
                  xaxis = dict(title='Día'),
                  yaxis = dict(title='Temperatura (Celsius)'),
                  template = 'plotly_white',
                  title_x = 0.5)
fig.show()