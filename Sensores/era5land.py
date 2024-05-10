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

''' Importar la colección MODIS LST '''
lst = ee.ImageCollection( 'ECMWF/ERA5_LAND/HOURLY' )

''' Fecha inicial de interés (inclusive) '''
i_date = '2017-04-25' 

''' Fecha final de interés (exclusiva) '''
f_date = '2017-12-31' 

'''Selección de bandas y fechas apropiadas para LST '''
banda = lst.select('temperature_2m').filterDate(i_date, f_date)

''' Definir la ubicación de interés como un punto. 
 Usaremos la ubicación de la Estación '''
punto_lon = -76.56472222
punto_lat = 3.64519444
cumbre_point = ee.Geometry.Point(punto_lon, punto_lat)

escala = 11132

cumbre_full = banda.getRegion(cumbre_point, escala).getInfo()
print(cumbre_full[:24])# Preview the output

print('Proceso Finalizado')