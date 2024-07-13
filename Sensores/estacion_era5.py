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

#rEra = 'Datos/CorrelacionPrecipitacion/Pacifico/ERAPacifico.csv' #Ruta del archivo ERA5
#rEst = 'Datos/CorrelacionPrecipitacion/Pacifico/PEPacifico.csv' #Ruta del archivo Estatción
r= 'Datos/CorrelacionPrecipitacion/Pacifico/ERAEstacionPacifico.csv'

#era = pd.read_csv(rEra, delimiter=',', index_col='Fecha',  parse_dates=['Fecha']) #Cargamos archivo Index
#estacion = pd.read_csv(rEst, delimiter=',', index_col='Fecha',  parse_dates=['Fecha'])
d= pd.read_csv(r, delimiter=',', index_col='Fecha',  parse_dates=['Fecha'])

print(d)
#print(estacion)
''' Creamos el formato de la fecha'''
#era5['datetime'] = pd.to_datetime(era5['datetime'], format='%Y-%m-%d %H:%M:%S')
#estacion['Fecha (UTC-05:00)'] = pd.to_datetime(estacion['Fecha (UTC-05:00)'], format='%d/%m/%Y %H:%M')
#df['Fecha (UTC-05:00)'] = pd.to_datetime(df['Fecha (UTC-05:00)'], format='%d/%m/%Y %H:%M')

'''Sumamos la precipitación por día en la estación'''
#es.set_index('Fecha (UTC-05:00)', inplace=True)
#es = es.resample('D').mean()
#es.reset_index(inplace=True)

#p_era = era['P4']
#p_est = estacion['Pacifico']
#time_era = era.index
#time_estacion = estacion.index
p_era4 = d['P4']
p_est = d['Pacifico']
time = d.index

fig = go.Figure()
#fig = px.bar(dch, x='Fecha', y='prcp', color_discrete_sequence=['darkblue']) #['blue'] - px.colors.qualitative.Dark24
#fig.add_trace(go.Scatter(x=time, y=p_era, mode='lines', name='Temperatura ERA5' )) #2ECC71 line=dict(color='#2ECC71'))
fig.add_trace(go.Bar(x=time, y=p_era4, name='ERA5', marker_color='#636EFA'))#Rojo
fig.add_trace(go.Bar(x=time, y=p_est, name='Observado', marker_color='#EF553B'))#Azul

title = f'Precipitacion ERA5 vs Estación U. Pacífico'
fig.update_layout(title=title,
                  xaxis = dict(title='Tiempo (Hora)'),
                  yaxis = dict(title='Precipitación (mm/hora)'),
                  template = 'seaborn', #'plotly_white' - 'plotly_dark' - 'ggplot2' - 'seaborn - 'simple_white'
                  title_font_size=22,
                  title_x = 0.5)
fig.show()
#fig.write_image("Patron_temperatura_era5_Upacifico.png", width=800, height=500, scale=4)
#title_font_family=
#estacion_nulos = df['Temp Media'].dropna()
correlacion = p_era4.corr(p_est)
print('Corrrelacion ERA5 y Observacion U. Pacífico: ', correlacion)