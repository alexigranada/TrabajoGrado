# -*- coding: utf-8 -*-
"""
Created on Wed Mar  24 23:33:48 2024
Gestion de tablas para llenar vacios constantes y ajustar nombre de columnas,
Unión de registros
@author: Arturo A. Granada G.
"""

import pandas as pd #Leer datos
import plotly.graph_objects as go

#ruta = 'Datos/Estaciones/La Cumbre/DataSetExport-TEMPERATURA.TAMX2_AUT_60@5311500121-20240425201123.csv' #Ruta del archivo
#ruta = 'Datos/Estaciones/Juanchaco/.csv'
#ruta = 'Datos/Estaciones/Farallones/TEMPERATURA.TA2_AUT_60@26055100.csv'
#ruta = 'Datos/Estaciones/IMarina/TEMPERATURA.TA2_AUT_60@5311500147.csv'
#ruta = 'Datos/Estaciones/Colegio Vasco Nuñez/TEMPERATURA.TA2_AUT_60@5311500149.csv'
#ruta = 'Datos/Estaciones/UPacifico/DIR VIENTO.DVMX_AUT_60@5311500056.csv'
ruta = 'Datos/Estaciones/IDEAM/Hora/Hora/1. La Cumbre/Precipitacion_LaCumbre_Hora_MedDif1h_0.csv'
data = pd.read_csv(ruta, delimiter=';') #Cargamos archivo
#data2 = pd.read_csv(ruta, delimiter=',') #Cargamos archivo

data.info()
print(data)

''' Antes de concatenar ajustamos el formato de la fecha'''
data['Fecha (UTC-05:00)'] = pd.to_datetime(data['Fecha (UTC-05:00)'], format='%d/%m/%Y %H:%M')

''' Pasamos la columna de Texto a numerico'''
#data['Valor (Celsius)'] = pd.to_numeric(data['Valor (Celsius)'].str.replace(',','.'))

''' Crear un rango de fechas completo '''
#rango_completo_hora = pd.date_range(start='2017-04-25 17:00:00', end='2022-02-15 21:00:00', freq='h')

''' Crear un DataFrame con las fechas completas '''
#df_completo_estacion_hora = pd.DataFrame({'Fecha (UTC-05:00)': rango_completo_hora})
#df_hora = pd.merge(df_completo_estacion_hora, data, on='Fecha (UTC-05:00)', how='left')
#print('Estación hora:')
#print(df_hora)
#df_hora.info()

'''Promediamos o sumamos por hora'''
data.set_index('Fecha (UTC-05:00)', inplace=True)
data_hora = data.resample('H').sum()
data_hora.reset_index(inplace=True)
print(data_hora)

'''' Calculamos los valores nulos'''
#valores_nulos_hora = df_hora['Valor (Celsius)'].isnull().sum()
#print('Datos faltantes hora: ')
#print(valores_nulos_hora)

''' Ploteamos las graficas'''
var_hora = data_hora['Valor (Millimetres)']
time_hora = data_hora['Fecha (UTC-05:00)']

title = f'Patron velocidad del viento estación: La Cumbre'

fig = go.Figure()

#fig.add_trace(go.Scatter(x=time_hora, y=var_hora, mode='lines', name='Temp. Hora', line=dict(color='#EF553B')))

fig.add_trace(go.Bar(x=time_hora, y=var_hora, name='Prec. Hora', marker_color='#03A9F4'))


fig.update_layout(xaxis = dict(title='Horas'),
                  yaxis = dict(title='Vel. Viento (m/s)'),
                  title = title,
                  title_x = 0.5)

#figPolar = go.Figure(go.Barpolar(
#    r=frecuencias,
#    theta=direcciones,
#    marker_color='rgb(123, 123, 123)',  # Color de las barras
#    marker_line_color='black',  # Color de los bordes de las barras
#    marker_line_width=1,  # Ancho de los bordes de las barras
#))

fig.show()

''' Exportar el DataFrame a un archivo CSV '''
title = f'Precipitacion_LaCumbre_Hora_Suma.csv'
data_hora.to_csv(title, sep=';', index=False)





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