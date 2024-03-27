# -*- coding: utf-8 -*-
"""
Created on Wed Mar  24 23:33:48 2024
Gestion de tablas para llenar vacios constantes y ajustar nombre de columnas
@author: Arturo A. Granada G.
"""

import pandas as pd #Leer datos

ruta = 'Estaciones/Temperatura estaciones dia/Temperatura_MISION LA [54075040].csv' #Ruta del archivo
data = pd.read_csv(ruta, delimiter=';') #Cargamos archivo

#data.info()
#print(data.head())
#print(data['Valor_x'])# Máx
#print(data['Valor_y'])# Mín

''' Eliminamos columnas inecesarias'''
data.drop(columns=['CodigoEstacion_y', 'CodigoEstacion_x', 'NombreEstacion_y', 'Latitud_y', 'Longitud_y', 
                   'Altitud_y', 'Municipio_y', 'Municipio_x', 'IdParametro_y', 'Etiqueta_y', 'DescripcionSerie_y',
                   'IdParametro_x', 'Etiqueta_x', 'DescripcionSerie_x'], inplace=True)

''' Renombramos Columnas'''
data = data.rename(columns={'NombreEstacion_x': 'NombreEstacion', 'Latitud_x':'Latitud', 'Longitud_x':'Longitud', 
                            'Altitud_x':'Altitud', 'Valor_x':'ValorMax', 'Valor_y':'ValorMin'})

''' Llenamos valores faltantes (Constantes)'''
name = str(data['NombreEstacion'][0])
data['NombreEstacion'] = data['NombreEstacion'].fillna(name)
data['Latitud'] = data['Latitud'].fillna(4.2225)
data['Longitud'] = data['Longitud'].fillna(-77.27633333)
data['Altitud'] = data['Altitud'].fillna(14.0)

data.info()
print(data.head())
print(data)

''' Exportar el DataFrame a un archivo CSV '''
title = f'Temperatura_{name}.csv'
data.to_csv(title, sep=';', index=False)