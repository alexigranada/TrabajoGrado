# -*- coding: utf-8 -*-
"""
Created on Thu May 09 07:54:01 2024

Descarga de datos ERA5 Land Hours (Temperatura cerca a la superficie de la tierra)

@author: Arturo A. Granada G.
"""

import ee 
import pandas as pd
import xarray as xr
#import rioxarray

# Activa el flujo de autenticación.
ee.Authenticate() 
# Inicializa la biblioteca. project='modis'
ee.Initialize()
print(ee.String('Hello from the Earth Engine servers!').getInfo())

''' Importar la colección MODIS LST '''
lst = ee.ImageCollection( 'ECMWF/ERA5_LAND/HOURLY' ) #MODIS/061/MOD11A1 - MODIS/061/MOD21A1D - ECMWF/ERA5_LAND/HOURLY

''' Fecha inicial de interés (inclusive) '''
i_date = '2015-01-01' 

''' Fecha final de interés (exclusiva) '''
f_date = '2015-05-01' 

'''Selección de bandas y fechas apropiadas para LST '''
#   'temperature_2m' - 'total_precipitation_hourly' - 'LST_Day_1km'
banda = lst.select('temperature_2m').filterDate(i_date, f_date)

''' Definir la ubicación de interés como un punto. 
 Usaremos la ubicación de la Estación '''
punto_lon = -77.07027
punto_lat = 3.4
cumbre_point = ee.Geometry.Point(punto_lon, punto_lat)

'''Descarga para Poligono'''
cuenca_dagua = ee.Geometry.Polygon(
    [[[-77.7, 5], 
      [-76, 5], 
      [-76, 3], 
      [-77.7, 3]]])

escala_era = 11132
escala_modis = 1000
escala_terraclimate = 4638.3

#cumbre_full = banda.getRegion(cuenca_dagua, escala).getInfo()
cumbre_full = banda.getRegion(cuenca_dagua, escala_era).getInfo()
print(cumbre_full[:50])# Preview the output

''' Convertimos a DF'''
df = pd.DataFrame(cumbre_full) 
#print(df)
headers = df.iloc[0]   # Rearrange the header.
df = pd.DataFrame(df.values[1:], columns=headers)   # Rearrange the header.
##print(df.head(50))
df = df[['longitude', 'latitude', 'time', 'total_precipitation' ]].dropna() # Eliminar las filas con datos nulos.
df['temperature_2m'] = pd.to_numeric(df['temperature_2m'], errors='coerce')    # Convert to numeric values.
df['datetime'] = pd.to_datetime(df['time'], unit='ms')  # Convert datetime to datetime values.
df = df[['longitude', 'latitude', 'datetime',  'pr']] # take interest part
##df = df[['longitude', 'latitude','time', 'datetime',  'total_precipitation']] # take interest part
##print(df.head(60))

''' Convertir °K a °C ERA'''
def k_c (k):
    c = k - 273.15
    return c

''' Convertir °K a °C MODIS'''
def k_c_Scale (k):
    c = k * 0.1
    return c

''' Convertir metros cubicos a milimetros '''
def m_mm (m):
    mm = m / 0.01
    return mm

''' Aplicamos la función'''
df['temperature_2m'] = df['temperature_2m'].apply(k_c)

##df['pr'] = df['pr']#.apply(k_c_Scale)
print(df.head())

'''Exportamos a CSV'''
#title = f'IDAHO_Precipitacion_Dagua_005.csv'
#df.to_csv(title, sep=';', index=False)

print('Proceso Finalizado')
print('Finalizado sin errores')