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

ruta_e5 = 'Datos/ERA5/LaCumbre/ERA5_LaCumbre_Hora.csv' #Ruta del archivo ERA5
ruta_estacion = 'Datos/Hora/V_Climaticas_LaCumbre_RL_Hora.csv' #Ruta del archivo Estatción

era5 = pd.read_csv(ruta_e5, delimiter=';') #Cargamos archivo
estacion = pd.read_csv(ruta_estacion, delimiter=';')
print(era5)
#print(dch)
''' Creamos el formato de la fecha'''
era5['datetime'] = pd.to_datetime(era5['datetime'], format='%Y-%m-%d %H:%M:%S')
estacion['Fecha (UTC-05:00)'] = pd.to_datetime(estacion['Fecha (UTC-05:00)'], format='%d/%m/%Y %H:%M')

'''Sumamos la precipitación por día en la estación'''
#es.set_index('Fecha (UTC-05:00)', inplace=True)
#es = es.resample('D').mean()
#es.reset_index(inplace=True)

fig = go.Figure()

temp = era5['temperature_2m']
tes = estacion['Temp Media']
time = estacion['Fecha (UTC-05:00)'][:120]

#fig = px.bar(dch, x='Fecha', y='prcp', color_discrete_sequence=['darkblue']) #['blue'] - px.colors.qualitative.Dark24
fig.add_trace(go.Scatter(x=time, y=temp, mode='lines', name='Temperatura ERA5' )) #2ECC71 line=dict(color='#2ECC71'))
fig.add_trace(go.Scatter(x=time, y=tes, mode='lines', name='Temperatura Estación')) #line=dict(color='#F44336'))

title = f'Temperatura ERA5 vs Estación La Cumbre'
fig.update_layout(title=title,
                  xaxis = dict(title='Tiempo (Hora)'),
                  yaxis = dict(title='Temperatura (°C)'),
                  template = 'seaborn', #'plotly_white' - 'plotly_dark' - 'ggplot2' - 'seaborn - 'simple_white'
                  title_font_size=22,
                  title_x = 0.5)
fig.show()
fig.write_image("Patron_temperatura_era5_lacumbre.png", width=800, height=500, scale=4)
#title_font_family=
estacion_nulos = estacion['Temp Media'].dropna()
correlacion = estacion_nulos.corr(temp)
print('Patron Estacion vs ERA5 (Temperatura)', correlacion)