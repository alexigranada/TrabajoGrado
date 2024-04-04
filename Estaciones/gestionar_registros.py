# -*- coding: utf-8 -*-
"""
Created on Wed Mar  24 23:33:48 2024
Gestion de tablas para llenar vacios constantes y ajustar nombre de columnas
@author: Arturo A. Granada G.
"""

import pandas as pd #Leer datos

ruta = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_1990-2000_COLPUERTOS [53115020].csv' #Ruta del archivo
data = pd.read_csv(ruta, delimiter=';') #Cargamos archivo

#data.info()
#print(data.head())
#print(data['Valor_x'])# Máx
#print(data['Valor_y'])# Mín

''' Eliminamos columnas inecesarias'''
data.drop(columns=['CodigoEstacion_y', 'CodigoEstacion_x', 'NombreEstacion_y', 'Latitud_y', 'Longitud_y', 
                   'Altitud_y', 'IdParametro_y', 'Etiqueta_y', 'DescripcionSerie_y',
                   'IdParametro_x', 'Etiqueta_x', 'DescripcionSerie_x'], inplace=True)

''' Renombramos Columnas'''
data = data.rename(columns={'NombreEstacion_x': 'NombreEstacion', 'Latitud_x':'Latitud', 'Longitud_x':'Longitud', 
                            'Altitud_x':'Altitud', 'Valor_x':'ValorMin', 'Valor_y':'ValorMax'})

''' Llenamos valores faltantes (Constantes)'''
name = str(data['NombreEstacion'][0])
lat = data['Latitud'][0]
lon = data['Longitud'][0]
altura = data['Altitud'][0]

data['NombreEstacion'] = data['NombreEstacion'].fillna(name)
data['Latitud'] = data['Latitud'].fillna(lat)
data['Longitud'] = data['Longitud'].fillna(lon)
data['Altitud'] = data['Altitud'].fillna(altura)

''' Sumar las variables correspondientes (Crear promedio)'''
data['ValorMedio'] = (data['ValorMax'] + data['ValorMin'])/2
data.info()
print(data.head())
print(data)

''' Exportar el DataFrame a un archivo CSV '''
title = f'Temperatura_1999-2000_{name}.csv'
data.to_csv(title, sep=';', index=False)

''' UNIR AÑOS 1990 A 2023'''
#ruta1 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_1999-2000_MISION LA [54075040].csv'
#ruta2 = 'Datos/Estaciones/IDEAM/Estaciones Dagua/Temperatura dia/Temperatura_dia_MISION LA [54075040].csv'
#dato1 = pd.read_csv(ruta1, delimiter=';')
#dato2 = pd.read_csv(ruta2, delimiter=';')

''' Antes de concatenar ajustamos el formato de la fecha'''
#dato1['Fecha'] = pd.to_datetime(dato1['Fecha'], format='%Y-%m-%d')
#dato2['Fecha'] = pd.to_datetime(dato2['Fecha'], format='%Y-%m-%d')

#d_1990_2000 = pd.merge(dato1, dato2, on='Fecha') #Unir si se tienen columnar diferentes
#d_1990_2000 = pd.concat([dato1, dato2])
#name = str(d_1990_2000['NombreEstacion'].iloc[0])

#print(d_1990_2000)

''' Exportar el DataFrame nulos max a un archivo CSV '''
#title = f'Temperatura_dia_{name}.csv'
#d_1990_2000.to_csv(title, sep=';', index=False)