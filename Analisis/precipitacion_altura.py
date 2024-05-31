# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:22:24 2024

Exploración de datos de precipitación de las Estaciones principales

@author: Arturo A. Granada G.
"""
import pandas as pd #Leer datos
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

ru = 'Datos/Precipitacion_UP.csv'
rc = 'Datos/Precipitacion_cumbre.csv'

rtu = 'Datos/Temperatura_UP.csv'
rtc = 'Datos/Temperatura_cumbre.csv'

df_u = pd.read_csv(ru, delimiter=';') #, index_col='Fecha', parse_dates=['Fecha']
df_c = pd.read_csv(rc, delimiter=';') #, index_col='Fecha', parse_dates=['Fecha']

df_tu = pd.read_csv(rtu, delimiter=';')
df_tc = pd.read_csv(rtc, delimiter=';')

df_u['Fecha'] = pd.to_datetime(df_u['Fecha'], format='%d/%m/%Y %H:%M')
df_c['Fecha'] = pd.to_datetime(df_c['Fecha'], format='%d/%m/%Y %H:%M')

df_tu['Fecha'] = pd.to_datetime(df_tu['Fecha'], format='%d/%m/%Y %H:%M')
df_tc['Fecha'] = pd.to_datetime(df_tc['Fecha'], format='%d/%m/%Y %H:%M')
print(df_u)
print(df_c)

''' Extraer la hora de la columna 'Fecha' '''
df_u['hora'] = df_u['Fecha'].dt.hour
df_c['hora'] = df_c['Fecha'].dt.hour

df_tu['hora'] = df_tu['Fecha'].dt.hour
df_tc['hora'] = df_tc['Fecha'].dt.hour
#print(df_u)

''' Agrupar por la hora y sumar los valores '''
u_hourly_sum = df_u.groupby('hora')['PrecipitacionT'].mean().reset_index()#Crea columna ID para cada registro
c_hourly_sum = df_c.groupby('hora')['Precipitacion'].mean().reset_index() #Crea columna ID para cada registro

tu_hourly_mean = df_tu.groupby('hora')['Tmedia'].mean().reset_index() #Crea columna ID para cada registro
tc_hourly_mean = df_tc.groupby('hora')['Tmedia'].mean().reset_index() #Crea columna ID para cada registro

print(u_hourly_sum)
print(c_hourly_sum)
print(tu_hourly_mean)

u_p = u_hourly_sum['PrecipitacionT']
c_p = c_hourly_sum['Precipitacion']

u_t = tu_hourly_mean['Tmedia']
c_t = tc_hourly_mean['Tmedia']

time = u_hourly_sum['hora']

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Bar(x=time, y=u_p, name='U. Pacífico', marker_color='#00A08B', yaxis='y1'))#Azul
fig.add_trace(go.Bar(x=time, y=c_p, name='La Cumbre', marker_color='#1616A7', yaxis='y1'))#Purpura AB63FA

fig.add_trace(go.Scatter(x=time, y=u_t, mode='lines+markers', name='Temp. U. Pacífico', marker_color='#00A08B', yaxis='y2'))#Rojo EF553B
fig.add_trace(go.Scatter(x=time, y=c_t, mode='lines+markers', name='Temp. La Cumbre', marker_color='#1616A7', yaxis='y2'))#Verde 00CC96

title = f'Precipitación y temperatura promedio por hora (2018-2021)'
fig.update_layout(title = title,
                  title_font_size=22,
                  xaxis = dict(title='Tiempo (Hora)'),
                  yaxis = dict(title='Precipitación (mm)'),
                  yaxis2 = dict(title='Temperatura (°C)', side='right'),
                  template = 'seaborn',
                  title_x = 0.5)
fig.show()
fig.write_image("PyT_Promedio_hora_estaciones.png", width=1200, height=500, scale=4)