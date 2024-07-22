# -*- coding: utf-8 -*-
"""
Created on Wed Mar  24 23:33:48 2024
Gestion de tablas para llenar vacios constantes y ajustar nombre de columnas,
Unión de registros
@author: Arturo A. Granada G.
"""

import pandas as pd #Leer datos
import plotly.graph_objects as go

ruta = 'Datos/Siloco.csv'
data = pd.read_csv(ruta, delimiter=',') #, index_col='Fecha', parse_dates=['Fecha']

#data.info()
print(data)


''' Antes de concatenar ajustamos el formato de la fecha'''
data['Fecha'] = pd.to_datetime(data['Fecha'], format="%Y-%m-%d  %H:%M:%S")

#data['Fecha_dia'] = data['Fecha'].dt.date #Seleccionar solo el valor del día (Sin hora)
#data['Fecha_dia'] = pd.to_datetime(data['Fecha_dia'], format="%Y-%m-%d")
#data['Fecha'] = data['Fecha_dia']
#print(data)

''' Eliminamos valores nulos'''
##data.dropna(inplace=True)

'''Concatenas registros'''
##d_t = pd.concat([data, data1, data2])

''' Pasamos la columna de Texto a numerico'''
##data['Valor'] = pd.to_numeric(data['Valor'])#.str.replace(',','.'))

''' Crear un rango de fechas completo '''
rango_completo_hora = pd.date_range(start='2015-01-01 00:00:00', end='2020-05-04 03:00:00', freq='h')

''' Crear un DataFrame con las fechas completas '''
df_completo_estacion_hora = pd.DataFrame({'Fecha': rango_completo_hora})

df_hora = pd.merge(data, df_completo_estacion_hora,  on='Fecha', how='right')
print('Estación hora:')
print(df_hora)
#df_hora.info()

'''Promediamos o sumamos por hora'''
#data.set_index('Fecha', inplace=True)
#data_hora = data.resample('h').mean()
#data_hora.reset_index(inplace=True)
#print(data_hora)

'''' Calculamos los valores nulos'''
#valores_nulos_hora = df_hora['Valor (Celsius)'].isnull().sum()
#print('Datos faltantes hora: ')
#print(valores_nulos_hora)

''' Ploteamos las graficas'''
#var_hora = d_t['temperature_2m']
#time_hora = d_t['datetime']

#title = f'Patron temperatura ERA5: U. Pacífico'

#fig = go.Figure()

#fig.add_trace(go.Scatter(x=time_hora, y=var_hora, mode='lines', name='Temp. Hora', line=dict(color='#EF553B')))

#fig.add_trace(go.Bar(x=time_hora, y=var_hora, name='Prec. Hora', marker_color='#03A9F4'))


#fig.update_layout(xaxis = dict(title='Horas'),
#                  yaxis = dict(title='Temperatura (Celcius)'),
#                  title = title,
#                  template = 'plotly_white',
#                  title_x = 0.5)

#figPolar = go.Figure(go.Barpolar(
#    r=frecuencias,
#    theta=direcciones,
#    marker_color='rgb(123, 123, 123)',  # Color de las barras
#    marker_line_color='black',  # Color de los bordes de las barras
#    marker_line_width=1,  # Ancho de los bordes de las barras
#))

#fig.show()

''' Exportar el DataFrame a un archivo CSV '''
title = f'Siloe_Hora_completo.csv'
df_hora.to_csv(title, sep=';', index=False)

'''' Calculamos los valores nulos'''
#valores_nulos_hora = estacion_hora['Valor'].isnull().sum()
#print('Datos faltantes hora: ')
#print(valores_nulos_hora)

''' Eliminamos columnas inecesarias'''
#data.drop(columns=['Entidad', 'AreaOperativa', 'Departamento', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion', 'Municipio'], inplace=True)
#data2.drop(columns=['Entidad', 'AreaOperativa', 'Departamento', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion', 'Municipio'], inplace=True)

''' Renombramos Columnas'''
#data = data.rename(columns={'NombreEstacion_x': 'NombreEstacion', 'Latitud_x':'Latitud', 'Longitud_x':'Longitud', 
#                            'Altitud_x':'Altitud', 'Valor_x':'ValorMin', 'Valor_y':'ValorMax'})

''' Llenamos valores faltantes (Constantes)'''
#name = str(data['NombreEstacion'][0])
#lat = data['Latitud'][0]
#lon = data['Longitud'][0]
#altura = data['Altitud'][0]

#data['NombreEstacion'] = data['NombreEstacion'].fillna(name)
#data['Latitud'] = data['Latitud'].fillna(lat)
#data['Longitud'] = data['Longitud'].fillna(lon)
#data['Altitud'] = data['Altitud'].fillna(altura)

''' Sumar las variables correspondientes (Crear promedio)'''
#data['ValorMedio'] = (data['ValorMax'] + data['ValorMin'])/2
#data.info()
#print(data.head())
#print(data)

''' Exportar el DataFrame a un archivo CSV '''
#title = f'Temperatura_1999-2000_{name}.csv'
#data.to_csv(title, sep=';', index=False)

''' UNIR AÑOS 1990 A 2023'''
#ruta1 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/VA_dia/Pluviometrico_dia_1990_QUEREMAL [53100040].csv' #Ruta del archivo
#ruta2 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/VA_dia/Pluviometrico_dia_QUEREMAL [53100040].csv'

#data1= pd.read_csv(ruta1, delimiter=';') #Cargamos archivo
#data2 = pd.read_csv(ruta2, delimiter=';') #Cargamos archivo

#print(data1['Fecha'])

'''Eliminamos columnas innecesarias'''
#data1.drop(columns=['CodigoEstacion', 'Entidad', 'AreaOperativa', 'Departamento', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion', 'Municipio', 'DescripcionSerie', 'IdParametro', 'Etiqueta'], inplace=True)
#data2.drop(columns=['Entidad', 'AreaOperativa', 'Departamento', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion', 'Municipio'], inplace=True)
#print(data1.head())
#print(data2.head())

''' Antes de concatenar ajustamos el formato de la fecha'''
#data1['Fecha'] = pd.to_datetime(data1['Fecha'], format='%Y-%m-%d')
#data2['Fecha'] = pd.to_datetime(data2['Fecha'], format='%m/%d/%Y %H:%M')

###d_1990_2000 = pd.merge(dato1, dato2, on='Fecha') #Unir si se tienen columnas diferentes
#d1_d2 = pd.concat([data1, data2])
#name = str(d1_d2['NombreEstacion'].iloc[650])

#print(d_1990_2000)

''' Exportar el DataFrame nulos max a un archivo CSV '''
#title = f'Pluviometrico_dia_{name}.csv'
#d1_d2.to_csv(title, sep=';', index=False)