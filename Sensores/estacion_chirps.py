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

ch = 'Datos/CorrelacionPrecipitacion/LaCumbre/CH4cumbre.csv' #Ruta del archivo CHIRPS
es = 'Datos/Estaciones/Precipitacion/VLAlba_Dia_completo.csv' #Ruta del archivo Estatción

dch = pd.read_csv(ch, delimiter=',', index_col='Fecha',  parse_dates=['Fecha']) #Cargamos archivo
des = pd.read_csv(es, delimiter=';', index_col='Fecha',  parse_dates=['Fecha']) #
print(des)
print(dch)

''' Creamos el formato de la fecha'''
#des['Fecha'] = pd.to_datetime(des['Fecha'], format='%d/%m/%Y %H:%M')
#dch_top['Fecha'] = pd.to_datetime(dch_top['Fecha'], format='%d/%m/%Y')
#dch_right['Fecha'] = pd.to_datetime(dch_right['Fecha'], format='%d/%m/%Y')
#dch_top_right['Fecha'] = pd.to_datetime(dch_right['Fecha'], format='%d/%m/%Y')
#des['Fecha (UTC-05:00)'] = pd.to_datetime(des['Fecha (UTC-05:00)'], format='%d/%m/%Y %H:%M')

''' Seleccionar horizonte de tiempo por fecha'''
f_i = '2018-01-01' 
f_f = '2022-12-31'

data_chirps = dch.loc[f_i:f_f]
data_estacion = des.loc[f_i:f_f]

##p_estacion = des['Pacifico']

p_estacion = data_estacion['Precipitacion']
p_chirps = data_chirps['P_4_4']

print(p_chirps)
print(p_estacion)

'''Promediamos o sumamos por hora'''
##des.set_index('Fecha', inplace=True)
##data_dia = p_estacion.resample('D').sum()
##data_dia.reset_index(inplace=True)
##print(data_dia)
##print(p_chirps)

##e_d = data_dia['Pacifico']
''' Suma por día'''
#data_dia = p_estacion.resample('D').sum()

''' Suma semanal'''
estacion_sem = p_estacion.resample('W').sum()
##e_s = estacion_sem['Pacifico']
chirps_sem = p_chirps.resample('W').sum()
##print(chirps_sem)
##print(estacion_sem)

''' Suma Mensual'''
estacion_mes = p_estacion.resample('ME').sum()
chirps_mes = p_chirps.resample('ME').sum()

#print(estacion_mes)
#print(chirps_mes)

#correlacion_dia = p_chirps.corr(data_dia)
correlacion_dia = p_chirps.corr(p_estacion)
correlacion_sem = chirps_sem.corr(estacion_sem)
correlacion_mes = chirps_mes.corr(estacion_mes)
print(f'Correlación diaria estación AguaClara vs CHIRPS: {correlacion_dia}')
print(f'Correlación semanal estación AguaClara vs CHIRPS: {correlacion_sem}')
print(f'Correlación mensual estación AguaClara vs CHIRPS: {correlacion_mes}')

''' Seleccionar datos por mes '''
#ch_enero = dch[dch.index.month == 1]

#ch_febrero = dch[dch.index.month == 2]

#ch_marzo = dch[dch.index.month == 3]

#ch_abril = dch[dch.index.month == 4]

#ch_mayo = dch[dch.index.month == 5]

#ch_junio = dch[dch.index.month == 6]

#ch_julio = dch[dch.index.month == 7]

#ch_agosto = dch[dch.index.month == 8]

#ch_septiembre = dch[dch.index.month == 9]

#ch_oct = dch[dch.index.month == 10]

#ch_nov = dch[dch.index.month == 11]

#ch_dic = dch[dch.index.month == 12]

##fig = go.Figure()
##fig.add_trace(go.Box(y=ch_enero['P_1_1']))

#fig = px.histogram(ch_dic, x='P_1_1', marginal='box')

#fig.show()


'''Sumamos la precipitación por día en la estación'''
#des.set_index('Fecha (UTC-05:00)', inplace=True)
#des_dia = des.resample('D').sum()
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

#title = f'CHIRPS vs Estación La Cumbre'
#fig = go.Figure()

#p_ch = dch['prcp'][:90]
#p_ch_top = dch_top['prcp'][:90]
#p_ch_right = dch_right['prcp'][:90]
#p_ch_top_right = dch_top_right['prcp'][:90]
#p_es = des_dia['Precipitacion'][:90]
#time = dch.index

#fig = px.bar(dch, x='Fecha', y='prcp', color_discrete_sequence=['darkblue']) #['blue'] - px.colors.qualitative.Dark24
#fig.add_trace(go.Bar(x=time, y=p_ch, name='Prec. CHIRPS', marker_color='#00ACC1'))
#fig.add_trace(go.Bar(x=time, y=p_ch_top, name='Prec. CHIRPS Top', marker_color='#00796B'))
#fig.add_trace(go.Bar(x=time, y=p_ch_right, name='Prec. CHIRPS Right', marker_color='#388E3C'))
#fig.add_trace(go.Bar(x=time, y=p_ch_top_right, name='Prec. CHIRPS Top-Right', marker_color='#4DD0E1'))
#fig.add_trace(go.Bar(x=time, y=p_es, name='Prec. Estación', marker_color='#EC407A'))
#fig.update_layout(title = title,
#                  xaxis = dict(title='Mes'),
#                  yaxis = dict(title='Precipitación (mm/mes)'),
#                  template = 'plotly_white',
#                  title_x = 0.5)
#fig.show()

print('Proceso finalizado con exito.')