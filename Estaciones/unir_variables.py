# -*- coding: utf-8 -*-
"""
Created on Wed Mar  24 23:33:48 2024
Gestion de tablas para llenar vacios constantes y ajustar nombre de columnas,
Unión de registros por variables
@author: Arturo A. Granada G.
"""

import pandas as pd #Leer datos
import plotly.graph_objects as go

ruta1 = 'Datos/Hora/1. La Cumbre/Temperatura_LaCumbre_Hora_MD1h.csv' #Ruta del archivo
ruta2 = 'Datos/Hora/1. La Cumbre/TemMax_LaCumbre_Hora.csv'
ruta3 = 'Datos/Hora/1. La Cumbre/TemMin_LaCumbre_Hora.csv'
ruta4 = 'Datos/Hora/1. La Cumbre/HR_LaCumbre_Hora.csv'
ruta5 = 'Datos/Hora/1. La Cumbre/Presion_LaCumbre_Hora.csv'
ruta6 = 'Datos/Hora/1. La Cumbre/VVMax_LaCumbre_Hora.csv'
ruta7 = 'Datos/Hora/1. La Cumbre/DVMax_LaCumbre_Hora.csv'

data1 = pd.read_csv(ruta1, delimiter=';') #Cargamos archivo
data2 = pd.read_csv(ruta2, delimiter=';')
data3 = pd.read_csv(ruta3, delimiter=';') 
data4 = pd.read_csv(ruta4, delimiter=';')
data5 = pd.read_csv(ruta5, delimiter=';')
data6 = pd.read_csv(ruta6, delimiter=';')
data7 = pd.read_csv(ruta7, delimiter=';')

'''Eliminamos campos innecesarios'''
data1.drop(columns=['Cód. de calidad de datos', 'Nivel de aprobación', 'Tipo de interpolación', 'Marca horaria del evento'], inplace=True)
data1 = data1.rename(columns={'Valor (Celsius)': 'Temp Media'})

t_max = data2['Valor (Celsius)']
t_min = data3['Valor (Celsius)']
hr = data4['Valor (Percent)']
presion = data5['Valor (Hectopascals)']
vv = data6['Valor (Metres per second)']
dv = data7['Valor (Degrees)']

#print(t_max)
#print(t_min)

''' Añadir columna a DF'''
data1['Temp Max'] = t_max
data1['Temp Min'] = t_min
data1['HR'] = hr
data1['Patm'] = presion
data1['Vel Viento'] = vv
data1['Dir Viento'] = dv

''' Llenamos valores faltantes (Constantes)'''
name = 'La Cumbre'
norte = 894832.083
este = 1056968.871
altura = 1613

data1['Fecha (UTC-05:00)'] = pd.to_datetime(data1['Fecha (UTC-05:00)'], format='%d/%m/%Y %H:%M')

print(data1.head())
t_ma = data1['Temp Media']#[:720]
t_mx = data1['Temp Max']#[:720]
t_mn = data1['Temp Min']#[:720]
hr = data1['HR']#[:720]
time = data1['Fecha (UTC-05:00)']#[:720]

#fig = go.Figure()

#fig.add_trace(go.Scatter(x=time, y=t_ma, mode='lines', name='Temp. Media', line=dict(color='#2ECC71')))
#fig.add_trace(go.Scatter(x=time, y=t_mx, mode='lines', name='Temp. Max', line=dict(color='#FF5722')))
#fig.add_trace(go.Scatter(x=time, y=t_mn, mode='lines', name='Temp. Min', line=dict(color='#03A9F4')))

#fig.update_layout(xaxis = dict(title='Horas'),
#                  yaxis = dict(title='Vel. Viento (m/s)'),
#                  title = 'Temperatura Estación: La Cumbre',
#                  title_x = 0.5,
#                  template = 'plotly_white')

#fig.show()

''' Seleccionar condición en tres columnnas'''
#dmx = data1[(data1['Temp Media'] == data1['Temp Max']) & (data1['Temp Min'].notnull())]

#print('Brutos: ')
#print(dmx[:100:])
#print(temp_ma_mn)

#dmx.apply(lambda x: print(x['Temp Media']), axis=1)
'''
for i, row in data1.iterrows():
    
    if (row['Temp Media'] == row['Temp Max']) & (row['Temp Min'] != 'NaN'):
        tx = (row['Temp Max'] + row['Temp Min']) / 2
        data1.loc['Temp Media'] = tx
    
    if (row['Temp Media'] == row['Temp Min']) & (row['Temp Max'] != 'NaN'):
        tn = (row['Temp Max'] + row['Temp Min']) / 2
        data1.loc['Temp Media'] = tn
'''

#print('Suavizados: ')
#print(dmx[:100:])

condicion = ((data1['Temp Media'] >= (data1['Temp Max'] - 0.5)) & (data1['Temp Min'].notnull()))
tx = (data1['Temp Max'] + data1['Temp Min']) / 2
data1.loc[condicion, 'Temp Media'] = tx

condicion = ((data1['Temp Media'] <= (data1['Temp Min'] + 0.5)) & (data1['Temp Max'].notnull()))
tx = (data1['Temp Max'] + data1['Temp Min']) / 2
data1.loc[condicion, 'Temp Media'] = tx

t_ma = data1['Temp Media']#[:720]
t_mx = data1['Temp Max']#[:720]
t_mn = data1['Temp Min']#[:720]
time = data1['Fecha (UTC-05:00)']#[:720]

fig = go.Figure()

fig.add_trace(go.Scatter(x=time, y=t_ma, mode='lines', name='Temp. Media', line=dict(color='#2ECC71')))
fig.add_trace(go.Scatter(x=time, y=t_mx, mode='lines', name='Temp. Max', line=dict(color='#FF5722')))
fig.add_trace(go.Scatter(x=time, y=t_mn, mode='lines', name='Temp. Min', line=dict(color='#03A9F4')))

fig.update_layout(xaxis = dict(title='Horas'),
                  yaxis = dict(title='Vel. Viento (m/s)'),
                  title = 'Temperatura Suavizada Estación: La Cumbre',
                  title_x = 0.5,
                  template = 'plotly_white')

fig.show()

''' Exportar el DataFrame a un archivo CSV '''
title = f'Temperatura_LaCumbre_RL_Hora.csv'
data1.to_csv(title, sep=';', index=False)