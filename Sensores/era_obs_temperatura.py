# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:29:17 2024

Extración variables ERA5-Land con coordenadas (estaciones meteorologicas)

@author: Arturo A. Granada G.
"""

import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

''' 1. Cargar el conjunto de datos CMIP6 (ejemplo: temperatura media diaria) '''

r = 'Datos/ERA5_Land_T_P/ERA5-Land_2015_2023_ValleDelCauca.nc'
ds = xr.open_dataset(r)

'''Transformar la fecha del netCDF'''
ds['time'] = ds.indexes['time']#.to_datetime().index()

''' 3. Cargamos los datos de temperatura del DataSet'''
tas = ds['t2m'] - 273.15
tas.attrs['units'] = '°C' #Cambiamos el argumento a °C

''' Seleccionamos pixel de interes'''
lon = -76.65138 #Longitud del pixel
lat = 3.41583 #Latitud del pixel (Mirarlo en en el DF cortado)

temp_estacion = tas.sel(longitude = lon, latitude = lat, method='nearest')

'''Convertimos a DF'''
df_temp = temp_estacion.to_dataframe().reset_index()

title = 'ERA5_Farallones.csv'
df_temp.to_csv(title, sep=';', index=True)
#print(df_temp)
print('Proceso finalizado.')