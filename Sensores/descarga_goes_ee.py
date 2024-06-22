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

''' Importar la colección GOES LST '''
lst = ee.ImageCollection( 'NOAA/GOES/16/MCMIPF' ) #MODIS/061/MOD11A1 - MODIS/061/MOD21A1D - ECMWF/ERA5_LAND/HOURLY

''' Fecha inicial de interés (inclusive) '''
i_date = '2017-07-10' 

''' Fecha final de interés (exclusiva) '''
f_date = '2017-07-12' 

'''Selección de bandas y fechas apropiadas para LST '''
#   'temperature_2m' - 'total_precipitation_hourly' - 'LST_Day_1km'
banda = lst.select('CMI_C13').filterDate(i_date, f_date)

'''Descarga para Poligono'''
cuenca_dagua = ee.Geometry.Polygon(
    [[[-77.4, 3.999], 
      [-76.4, 3.999], 
      [-76.4, 3.4], 
      [-77.4, 3.4]]])

''' Definimos la escala '''
escala_goes = 2000

cumbre_full = banda.getRegion(cuenca_dagua, escala_goes).getInfo()

print(cumbre_full)

''' Convertimos a DF'''
#df = pd.DataFrame(cumbre_full) 
#print(df)