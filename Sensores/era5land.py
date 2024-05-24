# -*- coding: utf-8 -*-
"""
Created on Thu May 09 07:54:01 2024

Descarga de datos ERA5 Land Hours (Temperatura cerca a la superficie de la tierra)

@author: Arturo A. Granada G.
"""

import ee 
import pandas as pd

# Activa el flujo de autenticación.
ee.Authenticate() 
# Inicializa la biblioteca. project='modis'
ee.Initialize()
print(ee.String('Hello from the Earth Engine servers!').getInfo())

''' Importar la colección MODIS LST '''
lst = ee.ImageCollection( 'ECMWF/ERA5_LAND/HOURLY' )

''' Fecha inicial de interés (inclusive) '''
i_date = '2022-01-01' 

''' Fecha final de interés (exclusiva) '''
f_date = '2023-01-01' 

'''Selección de bandas y fechas apropiadas para LST '''
#   'temperature_2m'
banda = lst.select('total_precipitation_hourly').filterDate(i_date, f_date)

''' Definir la ubicación de interés como un punto. 
 Usaremos la ubicación de la Estación '''
punto_lon = -76.564722222
punto_lat = 3.64519444
cumbre_point = ee.Geometry.Point(punto_lon, punto_lat)

'''Descarga para Poligono'''
cuenca_dagua = ee.Geometry.Polygon(
    [[[-77.6, 4.3], 
      [-76.2, 4.3], 
      [-76.2, 3.2], 
      [-77.6, 3.2]]])

escala = 11132

#cumbre_full = banda.getRegion(cuenca_dagua, escala).getInfo()
cumbre_full = banda.getRegion(cumbre_point, escala).getInfo()
#print(cumbre_full[:50])# Preview the output

''' Convertimos a DF'''
df = pd.DataFrame(cumbre_full) 
#print(df)
headers = df.iloc[0]   # Rearrange the header.
df = pd.DataFrame(df.values[1:], columns=headers)   # Rearrange the header.
#print(df.head(50))
#df = df[['longitude', 'latitude', 'time', 'total_precipitation' ]].dropna() # Eliminar las filas con datos nulos.
df[ "total_precipitation_hourly"] = pd.to_numeric(df[ "total_precipitation_hourly"], errors='coerce')    # Convert to numeric values.
df['datetime'] = pd.to_datetime(df['time'], unit='ms')  # Convert datetime to datetime values.
df = df[['time', 'datetime',  'total_precipitation_hourly']] # take interest part
#df = df[['longitude', 'latitude','time', 'datetime',  'total_precipitation']] # take interest part
#print(df.head(60))

''' Convertir °K a °C'''
#def k_c (k):
#    c = k - 273.15
#    return c

''' Convertir metros cubicos a milimetros '''
def m_mm (m):
    mm = m / 0.01
    return mm

''' Aplicamos la función'''
#df['temperature_2m'] = df['temperature_2m'].apply(k_c)

df['total_precipitation_hourly'] = df['total_precipitation_hourly'].apply(m_mm)
print(df.head(50))

'''Exportamos a CSV'''
title = f'ERA5_Precipitacion_horly_LaCumbre_Hora_6.csv'
df.to_csv(title, sep=';', index=False)
print('Proceso Finalizado')
print('Finalizado sin errores')