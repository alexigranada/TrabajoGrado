# -*- coding: utf-8 -*-
"""
Created on Wed Mar  24 23:33:48 2024
Gestion de tablas para llenar vacios constantes y ajustar nombre de columnas,
Unión de registros
@author: Arturo A. Granada G.
"""

import pandas as pd #Leer datos

#ruta = 'Datos/Estaciones/IDEAM/Estaciones Dagua/dia pluvio 1 1990/excel.csv' #Ruta del archivo
#ruta2 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/dia pluvio 1 1990/excel.csv'

#data = pd.read_csv(ruta, delimiter=',') #Cargamos archivo
#data2 = pd.read_csv(ruta, delimiter=',') #Cargamos archivo

#data.info()
#print(data.head())
#print(data['Valor_x'])# Máx
#print(data['Valor_y'])# Mín

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
ruta1 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/VA_dia/Pluviometrico_dia_1990_QUEREMAL [53100040].csv' #Ruta del archivo
ruta2 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/VA_dia/Pluviometrico_dia_QUEREMAL [53100040].csv'

data1= pd.read_csv(ruta1, delimiter=';') #Cargamos archivo
data2 = pd.read_csv(ruta2, delimiter=';') #Cargamos archivo

print(data1['Fecha'])

'''Eliminamos columnas innecesarias'''
data1.drop(columns=['CodigoEstacion', 'Entidad', 'AreaOperativa', 'Departamento', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion', 'Municipio', 'DescripcionSerie', 'IdParametro', 'Etiqueta'], inplace=True)
#data2.drop(columns=['Entidad', 'AreaOperativa', 'Departamento', 'Categoria', 'FechaInstalacion', 'FechaSuspension', 'Frecuencia', 'Grado', 'Calificador', 'NivelAprobacion', 'Municipio'], inplace=True)
print(data1.head())
print(data2.head())

''' Antes de concatenar ajustamos el formato de la fecha'''
data1['Fecha'] = pd.to_datetime(data1['Fecha'], format='%Y-%m-%d')
data2['Fecha'] = pd.to_datetime(data2['Fecha'], format='%m/%d/%Y %H:%M')

###d_1990_2000 = pd.merge(dato1, dato2, on='Fecha') #Unir si se tienen columnas diferentes
d1_d2 = pd.concat([data1, data2])
name = str(d1_d2['NombreEstacion'].iloc[650])

#print(d_1990_2000)

''' Exportar el DataFrame nulos max a un archivo CSV '''
title = f'Pluviometrico_dia_{name}.csv'
d1_d2.to_csv(title, sep=';', index=False)