# -*- coding: utf-8 -*-
"""
Created on Sun May 05 14:45:03 2024

Exploración de datos de sensor MODIS vs Observados por estaciones

@author: Arturo A. Granada G.
"""

'''Importamos librerias'''
import pandas as pd #Leer datos
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt #Graficas y limpiar datos

modis = 'Datos/MODIS Día/MODIS_LaCumbre_Dia.csv' #Ruta del archivo CHIRPS
es = 'Datos/Hora/V_Climaticas_LaCumbre_RL_Hora.csv' #Ruta del archivo Estatción

modis = pd.read_csv(modis, delimiter=';') #Cargamos archivo
es = pd.read_csv(es, delimiter=';')
#print(des)
#print(dch)
''' Creamos el formato de la fecha'''
modis['datetime'] = pd.to_datetime(modis['datetime'], format='%Y-%m-%d')
es['Fecha (UTC-05:00)'] = pd.to_datetime(es['Fecha (UTC-05:00)'], format='%d/%m/%Y %H:%M')

'''Sumamos la precipitación por día en la estación'''
es.set_index('Fecha (UTC-05:00)', inplace=True)
es = es.resample('D').mean()
es.reset_index(inplace=True)

title = f'CHIRPS vs Estación La Cumbre'
fig = go.Figure()

temp = modis['LST_Day_1km']
tes = es['Temp Media']
time = modis['datetime']

#fig = px.bar(dch, x='Fecha', y='prcp', color_discrete_sequence=['darkblue']) #['blue'] - px.colors.qualitative.Dark24
fig.add_trace(go.Scatter(x=time, y=temp, mode='lines', name='Temperatura MODIS', line=dict(color='#2ECC71'))) #2ECC71
fig.add_trace(go.Scatter(x=time, y=tes, mode='lines', name='Temperatura Estación', line=dict(color='#F44336')))
title = f'Temperatura MODIS vs Estación: La Cumbre'
fig.update_layout(title = title,
                  xaxis = dict(title='Día'),
                  yaxis = dict(title='Temperatura (Celsius)'),
                  template = 'plotly_white',
                  title_x = 0.5)
fig.show()