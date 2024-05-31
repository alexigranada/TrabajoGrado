# -*- coding: utf-8 -*-
"""
Created on Sun May 29 07:49:49 2024

Exploración de datos de precipitación de ERA5-Land y Estaciones principales

@author: Arturo A. Granada G.
"""

'''Importamos librerias'''
import pandas as pd #Leer datos
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt #Graficas para datos

r = 'Datos/Precipitacion_cumbre.csv'
ch = 'Datos/Estaciones/IDEAM/CHIRPS Dia Valle/CHIRPS_LaCumbre_Dia.csv' #Ruta del archivo CHIRPS

df = pd.read_csv(r, delimiter=';', index_col='Fecha',  parse_dates=['Fecha'])
df_ch = pd.read_csv(ch, delimiter=';', index_col='Fecha',  parse_dates=['Fecha'])


#df = df.dropna()
df_dia = df.resample('D').sum()
print(df_dia)
print(df_ch)

estacion = df_dia['Precipitacion'][:90]
era5 = df_dia['total_precipitation'][:90]
chirps = df_ch['prcp'][:90]
time = df_ch.index
fig = go.Figure()

fig.add_trace(go.Bar(x=time, y=estacion, name='Observación', marker_color='#EF553B'))#Rojo
fig.add_trace(go.Bar(x=time, y=era5, name='Estimación ERA5', marker_color='#636EFA'))#Azul
fig.add_trace(go.Bar(x=time, y=chirps, name='Estimación CHIRPS', marker_color='#AB63FA'))#Morado

title = f'Precipitación estación La Cumbre'
fig.update_layout(title = title,
                  title_font_size=22,
                  xaxis = dict(title='Día'),
                  yaxis = dict(title='Precipitación (mm/día)'),
                  template = 'seaborn',
                  title_x = 0.5)
fig.show()
#fig.write_image("Precipitacion_dia_LaCumbre_OE.png", width=800, height=500, scale=4)


''' PRECIPITACIÓN SEMANAL'''
#df_semana = df.resample('W').sum()
#print(df_semana)

#estacion2 = df_semana['PrecipitacionT']
#era52 = df_semana['total_precipitation']
#time2 = df_semana.index

#fig2 = go.Figure()

#fig2.add_trace(go.Bar(x=time2, y=estacion2, name='EstaciónT', marker_color='#636EFA'))#Morado
#fig2.add_trace(go.Bar(x=time2, y=era52, name='ERA5', marker_color='#EF553B'))#Rojo

#title2 = f'Precipitación ERA5 y Estación U. Pacífico'
#fig2.update_layout(title = title2,
#                  title_font_size=22,
#                  xaxis = dict(title='Semana'),
#                  yaxis = dict(title='Precipitación (mm/semanal)'),
#                  template = 'seaborn',
#                  title_x = 0.5)
#fig2.show()
#fig2.write_image("PrecipitacionT_semana_era5_UP.png", width=800, height=500, scale=4)


'''PRECIPITACIÓN MENS'''

#df_mes = df.resample('ME').sum()
#print(df_mes)

#estacion3 = df_mes['PrecipitacionT']
#era53 = df_mes['total_precipitation']
#time3 = df_mes.index

#fig3 = go.Figure()

#fig3.add_trace(go.Bar(x=time3, y=estacion3, name='EstaciónT', marker_color='#636EFA'))#Morado
#fig3.add_trace(go.Bar(x=time3, y=era53, name='ERA5', marker_color='#EF553B'))#Rojo

#title3 = f'Precipitación ERA5 y Estación U. Pacífico'
#fig3.update_layout(title = title,
#                  title_font_size=22,
#                  xaxis = dict(title='Mes'),
#                  yaxis = dict(title='Precipitación (mm/mes)'),
#                  template = 'seaborn',
#                  title_x = 0.5)
#fig3.show()
#fig3.write_image("PrecipitacionT_mes_era5_UP.png", width=800, height=500, scale=4)