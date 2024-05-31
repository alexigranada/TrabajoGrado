# -*- coding: utf-8 -*-
"""
Created on Sun May 05 14:45:03 2024

Exploración de datos de precipitación de CHIRPS

@author: Arturo A. Granada G.
"""

'''Importamos librerias'''
import pandas as pd #Leer datos
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt #Graficas para datos

ch = 'Datos/Estaciones/IDEAM/CHIRPS Dia Valle/CHIRPS_LaCumbre_Dia.csv' #Ruta del archivo CHIRPS
ch_top = 'Datos/Estaciones/IDEAM/CHIRPS Dia Valle/CHIRPS_Top_LaCumbre_Dia.csv' #Ruta del archivo CHIRPS
ch_right = 'Datos/Estaciones/IDEAM/CHIRPS Dia Valle/CHIRPS_Right_LaCumbre_Dia.csv' #Ruta del archivo CHIRPS
ch_top_right = 'Datos/Estaciones/IDEAM/CHIRPS Dia Valle/CHIRPS_Top-Right_LaCumbre_Dia.csv' #Ruta del archivo CHIRPS
es = 'Datos/Precipitacion_cumbre.csv' #Ruta del archivo Estatción

dch = pd.read_csv(ch, delimiter=';', index_col='Fecha',  parse_dates=['Fecha']) #Cargamos archivo
des = pd.read_csv(es, delimiter=';', index_col='Fecha',  parse_dates=['Fecha'])
dch_top = pd.read_csv(ch_top, delimiter=';', index_col='Fecha',  parse_dates=['Fecha'])
dch_right = pd.read_csv(ch_right, delimiter=';', index_col='Fecha',  parse_dates=['Fecha'])
dch_top_right = pd.read_csv(ch_top_right, delimiter=';', index_col='Fecha',  parse_dates=['Fecha'])
#print(des)
#print(dch)
''' Creamos el formato de la fecha'''
#dch['Fecha'] = pd.to_datetime(dch['Fecha'], format='%d/%m/%Y')
#dch_top['Fecha'] = pd.to_datetime(dch_top['Fecha'], format='%d/%m/%Y')
#dch_right['Fecha'] = pd.to_datetime(dch_right['Fecha'], format='%d/%m/%Y')
#dch_top_right['Fecha'] = pd.to_datetime(dch_right['Fecha'], format='%d/%m/%Y')
#des['Fecha (UTC-05:00)'] = pd.to_datetime(des['Fecha (UTC-05:00)'], format='%d/%m/%Y %H:%M')

'''Sumamos la precipitación por día en la estación'''
#des.set_index('Fecha (UTC-05:00)', inplace=True)
des_dia = des.resample('D').sum()
#des_dia.reset_index(inplace=True)

#des.set_index('Fecha (UTC-05:00)', inplace=True)
#des_mes = des.resample('ME').sum()
#des_mes.reset_index(inplace=True)

#dch.set_index('Fecha', inplace=True)
#dch_mes = dch.resample('ME').sum()
#dch_mes.reset_index(inplace=True)

#dch_top.set_index('Fecha', inplace=True)
#dch_top_mes = dch_top.resample('ME').sum()
#dch_top_mes.reset_index(inplace=True)

#dch_right.set_index('Fecha', inplace=True)
#dch_right_mes = dch_right.resample('ME').sum()
#dch_right_mes.reset_index(inplace=True)

#dch_top_right.set_index('Fecha', inplace=True)
#dch_top_right_mes = dch_top_right.resample('ME').sum()
#dch_top_right_mes.reset_index(inplace=True)

title = f'CHIRPS vs Estación La Cumbre'
fig = go.Figure()

p_ch = dch['prcp'][:90]
p_ch_top = dch_top['prcp'][:90]
p_ch_right = dch_right['prcp'][:90]
p_ch_top_right = dch_top_right['prcp'][:90]
p_es = des_dia['Precipitacion'][:90]
time = dch.index

#fig = px.bar(dch, x='Fecha', y='prcp', color_discrete_sequence=['darkblue']) #['blue'] - px.colors.qualitative.Dark24
fig.add_trace(go.Bar(x=time, y=p_ch, name='Prec. CHIRPS', marker_color='#00ACC1'))
fig.add_trace(go.Bar(x=time, y=p_ch_top, name='Prec. CHIRPS Top', marker_color='#00796B'))
fig.add_trace(go.Bar(x=time, y=p_ch_right, name='Prec. CHIRPS Right', marker_color='#388E3C'))
fig.add_trace(go.Bar(x=time, y=p_ch_top_right, name='Prec. CHIRPS Top-Right', marker_color='#4DD0E1'))
fig.add_trace(go.Bar(x=time, y=p_es, name='Prec. Estación', marker_color='#EC407A'))
fig.update_layout(title = title,
                  xaxis = dict(title='Mes'),
                  yaxis = dict(title='Precipitación (mm/mes)'),
                  template = 'plotly_white',
                  title_x = 0.5)
fig.show()