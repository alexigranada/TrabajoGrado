# -*- coding: utf-8 -*-
"""
Created on Thu May 09 07:54:01 2024

Descarga de datos MODIS LST (Temperatura superficial de la tierra)

@author: Arturo A. Granada G.
"""

import ee 
import pandas as pd

# Activa el flujo de autenticación.
ee.Authenticate() 
# Inicializa la biblioteca. project='modis'
ee.Initialize()
print(ee.String('Hello from the Earth Engine servers!').getInfo())

# Importar la colección MODIS LST.
lst = ee.ImageCollection( 'MODIS/061/MOD11A1' )

# Fecha inicial de interés (inclusive). 
i_date = '2017-04-25' 

# Fecha final de interés (exclusiva). 
f_date = '2022-02-15' 

# Selección de bandas y fechas apropiadas para LST. 
banda = lst.select( 'LST_Day_1km' , 'QC_Day' ).filterDate(i_date, f_date)

''' Definir la ubicación de interés como un punto. 
 Usaremos la ubicación de la Estación '''
Hamburg_lon = -76.56472222
Hamburg_lat = 3.64519444
Hamburg_point = ee.Geometry.Point(Hamburg_lon, Hamburg_lat)

escala = 1000   # escala en metros
lst_hamburg = banda.mean().sample(Hamburg_point, escala).first().get( 'LST_Day_1km' ).getInfo() 
print ( 'LST diurno promedio de Hamburgo:' , round (lst_hamburg* 0.02 - 273.15 , 2 ), '°C' ) 
# la salida es: LST diurno promedio de Hamburgo: 16,83 °C

lst_Hamburg_full = banda.getRegion(Hamburg_point, escala).getInfo()
print(lst_Hamburg_full[:3])# Preview the output.

'''Convertimos a DF'''
df = pd.DataFrame(lst_Hamburg_full) 
headers = df.iloc[0]   # Rearrange the header.
df = pd.DataFrame(df.values[1:], columns=headers)   # Rearrange the header.
df = df[['longitude', 'latitude', 'time', "LST_Day_1km" ]].dropna() # Eliminar las filas con datos nulos.
df[ "LST_Day_1km"] = pd.to_numeric(df[ "LST_Day_1km"], errors='coerce')    # Convert to numeric values.
df['datetime'] = pd.to_datetime(df['time'], unit='ms')  # Convert datetime to datetime values.
df = df[['time','datetime',  "LST_Day_1km"   ]] # take interest part
df.head()

def kelvin_to_celcius(t_kelvin):
    t_celsius =  t_kelvin*0.02 - 273.15
    return t_celsius
df['LST_Day_1km'] = df['LST_Day_1km'].apply(kelvin_to_celcius)
df.head()

'''Exportamos a CSV'''
title = f'MODIS_LaCumbre_Dia.csv'
df.to_csv(title, sep=';', index=False)

print('Finalizado')